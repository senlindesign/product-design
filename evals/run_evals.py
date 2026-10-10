#!/usr/bin/env python3
"""Run the product-design golden test set through headless Claude Code, then check every page.

  python3 evals/run_evals.py                      # smoke set, default model
  python3 evals/run_evals.py --cases all          # full set
  python3 evals/run_evals.py --cases 3,7 --model sonnet
  python3 evals/run_evals.py --check-only evals/runs/<run-dir>   # re-check existing outputs
"""
import argparse
import concurrent.futures as cf
import json
import subprocess
import sys
import threading
import time
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL = REPO / "skills" / "product-design"
CHECKER = SKILL / "scripts" / "check_page.py"
CASES_FILE = REPO / "evals" / "evals.json"
RUNS = REPO / "evals" / "runs"
sys.path.insert(0, str(REPO / "evals"))

PROMPT = """Use the product-design skill (invoke it with the Skill tool; its name is `product-design:product-design`) to handle the request below.

This is a non-interactive evaluation run:
- Never ask questions. Follow the route the skill prescribes for this request.
- Save the page to exactly this path: `{page_path}`. Do not open it in a browser.
- Finish with the delivery message exactly as you would show the user, including the QA report.

Request:
{request}"""

TOOLS = "Skill,Read,Write,Edit,Glob,Grep,Bash(python3:*)"
LIMIT_HIT = threading.Event()  # set once the account hits a usage limit; remaining cases are skipped


def select(cases, spec):
    if spec == "smoke":
        return [c for c in cases if c.get("smoke")]
    if spec == "all":
        return cases
    wanted = {s.strip() for s in spec.split(",")}
    return [c for c in cases if str(c["id"]) in wanted or c["name"] in wanted]


def check(case, case_dir):
    pages = [case_dir / "page.html"] + sorted(case_dir.glob("*.html"))
    page = next((p for p in pages if p.exists()), None)
    if page is None:
        return {"passed": False, "errors": [{"rule": "run.no-page", "message": "no HTML file was produced"}], "warnings": []}
    out = subprocess.run(
        [sys.executable, str(CHECKER), str(page), "--case-file", str(CASES_FILE), "--case-id", case["name"],
         "--strict", "--json", str(case_dir / "check.json")],
        capture_output=True, text=True)
    (case_dir / "check.txt").write_text(out.stdout + out.stderr)
    return json.loads((case_dir / "check.json").read_text())


def generate(case, case_dir, model, timeout):
    case_dir.mkdir(parents=True, exist_ok=True)
    cmd = ["claude", "-p", PROMPT.format(request=case["prompt"], page_path=case_dir / "page.html"),
           "--plugin-dir", str(REPO), "--add-dir", str(SKILL),
           "--allowedTools", TOOLS, "--output-format", "json"]
    if model:
        cmd += ["--model", model]
    start = time.time()
    meta = {"case": case["name"], "model": model or "default"}
    try:
        proc = subprocess.run(cmd, cwd=case_dir, capture_output=True, text=True, timeout=timeout,
                              stdin=subprocess.DEVNULL)  # an inherited stdin can block headless claude
        (case_dir / "claude.json").write_text(proc.stdout)
        if proc.stderr.strip():
            (case_dir / "stderr.txt").write_text(proc.stderr)
        res = json.loads(proc.stdout)
        (case_dir / "delivery.md").write_text(res.get("result") or "")
        meta.update(cost_usd=res.get("total_cost_usd"), turns=res.get("num_turns"),
                    denials=len(res.get("permission_denials") or []), is_error=res.get("is_error"))
        if res.get("is_error"):
            meta["error"] = (res.get("result") or "claude returned an error")[:160]
            if "limit" in meta["error"].lower():
                meta["infra"] = True
                LIMIT_HIT.set()
    except subprocess.TimeoutExpired:
        meta["error"] = f"timed out after {timeout}s"
    except json.JSONDecodeError:
        meta["error"] = "claude did not return JSON (see claude.json / stderr.txt)"
    meta["seconds"] = round(time.time() - start)
    (case_dir / "meta.json").write_text(json.dumps(meta, indent=2))
    return meta


def audit(case, case_dir):
    page = case_dir / "page.html"
    if not page.exists():
        return None
    try:
        from audit_claims import audit as run_audit
        data = run_audit(page, case["prompt"])
        (case_dir / "claims.json").write_text(json.dumps(data, indent=2, ensure_ascii=False))
        return len(data.get("unsupported", []))
    except Exception as exc:  # the audit is advisory; never fail the run on it
        (case_dir / "claims.json").write_text(json.dumps({"error": str(exc)}))
        return None


def summarize(run_dir, rows):
    lines = [f"# Eval run — {run_dir.name}", "",
             "| Case | Result | Errors | Warnings | Unsupported claims | Cost | Time | Notes |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for case, meta, result in rows:
        cost = f"${meta['cost_usd']:.2f}" if meta.get("cost_usd") is not None else "—"
        secs = f"{meta['seconds']}s" if meta.get("seconds") is not None else "—"
        notes = meta.get("error") or (f"{meta['denials']} tool denials" if meta.get("denials") else "")
        first = result["errors"][0]["message"] if result.get("errors") else ""
        status = "PASS" if result.get("passed") else ("SKIPPED" if meta.get("infra") else "FAIL")
        lines.append(f"| {case['name']} | {status} | {len(result.get('errors', []))} | "
                     f"{len(result.get('warnings', []))} | {meta.get('claims', '—') if meta.get('claims') is not None else '—'} | {cost} | {secs} | {notes or first} |")
    passed = sum(1 for _, _, r in rows if r.get("passed"))
    skipped = sum(1 for _, m, _ in rows if m.get("infra"))
    ran = len(rows) - skipped
    total_cost = sum(m.get("cost_usd") or 0 for _, m, _ in rows)
    skip_note = f" · {skipped} skipped (usage limit — rerun them later with --cases)" if skipped else ""
    lines += ["", f"**{passed}/{ran} passed**{skip_note} · total cost ${total_cost:.2f}", "",
              "Details per case: `<case>/check.txt` (objective checks), `<case>/delivery.md` (QA report), `<case>/page.html`."]
    (run_dir / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    return passed == ran


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cases", default="smoke", help="smoke (default), all, or comma-separated ids/names")
    ap.add_argument("--model", help="e.g. opus, sonnet, haiku (default: Claude Code's default)")
    ap.add_argument("--parallel", type=int, default=3)
    ap.add_argument("--timeout", type=int, default=1200, help="seconds per case")
    ap.add_argument("--check-only", help="re-run checks on an existing run directory")
    ap.add_argument("--no-audit", action="store_true", help="skip the claims audit (Haiku, a few cents per case)")
    args = ap.parse_args()

    cases = json.loads(CASES_FILE.read_text())["evals"]

    if args.check_only:
        run_dir = Path(args.check_only)
        rows = []
        for case in cases:
            d = run_dir / case["name"]
            if d.exists():
                meta = json.loads((d / "meta.json").read_text()) if (d / "meta.json").exists() else {}
                rows.append((case, meta, check(case, d)))
        sys.exit(0 if summarize(run_dir, rows) else 1)

    chosen = select(cases, args.cases)
    if not chosen:
        ap.error(f"no cases match {args.cases!r}")
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    run_dir = RUNS / f"{stamp}-{args.model or 'default'}"
    run_dir.mkdir(parents=True)
    print(f"Running {len(chosen)} case(s) → {run_dir.relative_to(REPO)}")

    def one(case):
        d = run_dir / case["name"]
        if LIMIT_HIT.is_set():
            d.mkdir(parents=True, exist_ok=True)
            meta = {"case": case["name"], "infra": True, "error": "skipped: usage limit reached earlier in this run"}
            (d / "meta.json").write_text(json.dumps(meta, indent=2))
            print(f"  {case['name']}: SKIPPED")
            return case, meta, {"passed": False, "errors": [], "warnings": []}
        meta = generate(case, d, args.model, args.timeout)
        if meta.get("infra"):
            print(f"  {case['name']}: SKIPPED ({meta['error']})")
            return case, meta, {"passed": False, "errors": [], "warnings": []}
        result = check(case, d)
        if not args.no_audit:
            meta["claims"] = audit(case, d)
            (d / "meta.json").write_text(json.dumps(meta, indent=2))
        print(f"  {case['name']}: {'PASS' if result.get('passed') else 'FAIL'} ({meta.get('seconds')}s, unsupported claims: {meta.get('claims', '—')})")
        return case, meta, result

    with cf.ThreadPoolExecutor(max_workers=args.parallel) as pool:
        rows = list(pool.map(one, chosen))
    sys.exit(0 if summarize(run_dir, rows) else 1)


if __name__ == "__main__":
    main()
