#!/usr/bin/env python3
"""Run the product-design golden test set through headless Claude Code, then check every page.

  python3 evals/run_evals.py                      # smoke set, default model
  python3 evals/run_evals.py --cases all          # full set
  python3 evals/run_evals.py --cases 3,7 --model sonnet
  python3 evals/run_evals.py --check-only evals/runs/<run-dir>   # re-check existing outputs
  python3 evals/run_evals.py --judge opus         # also score screenshots (evals/judge_pages.py)

Every case also gets a 390px audit (evals/screens.py; needs node + playwright, skipped otherwise) and a
record of which skill files the agent read and whether it reached their end (reads.json, run-level reads.md).
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
from screens import audit_problems, mobile_audit  # noqa: E402

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
           "--allowedTools", TOOLS, "--output-format", "stream-json", "--verbose"]
    if model:
        cmd += ["--model", model]
    start = time.time()
    meta = {"case": case["name"], "model": model or "default"}
    try:
        proc = subprocess.run(cmd, cwd=case_dir, capture_output=True, text=True, timeout=timeout,
                              stdin=subprocess.DEVNULL)  # an inherited stdin can block headless claude
        (case_dir / "claude.jsonl").write_text(proc.stdout)
        if proc.stderr.strip():
            (case_dir / "stderr.txt").write_text(proc.stderr)
        res, reads = parse_stream(proc.stdout)
        (case_dir / "claude.json").write_text(json.dumps(res, indent=2))
        (case_dir / "reads.json").write_text(json.dumps(reads, indent=2))
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


def parse_stream(text):
    """Split stream-json output into the final result event and the list of files the agent read."""
    res, reads = None, []
    for line in text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("type") == "result":
            res = event
        elif event.get("type") == "assistant":
            for item in event.get("message", {}).get("content", []):
                if item.get("type") == "tool_use" and item.get("name") in ("Read", "Skill"):
                    reads.append(read_record(item["name"], item.get("input", {})))
    if res is None:
        raise json.JSONDecodeError("no result event", text[-200:], 0)
    return res, reads


def read_record(tool, args):
    if tool == "Skill":
        return {"file": "SKILL.md (via Skill tool)", "whole": True}
    path = Path(args.get("file_path", ""))
    try:
        rel = str(path.resolve().relative_to(SKILL))
    except ValueError:
        return {"file": str(path), "outside_skill": True}
    total = sum(1 for _ in path.open()) if path.exists() else None
    start = args.get("offset") or 1
    end = start - 1 + (args.get("limit") or 2000)  # Read's default limit is 2000 lines
    return {"file": rel, "lines": total, "from": start, "to": min(end, total or end),
            "whole": total is not None and start <= 1 and end >= total}


def summarize_reads(run_dir, rows):
    """reads.md: for every skill file, how many cases opened it and how many read it to the last line."""
    stats = {}
    for case, _, _ in rows:
        f = run_dir / case["name"] / "reads.json"
        if not f.exists():
            continue
        per_case = {}
        for r in json.loads(f.read_text()):
            if r.get("outside_skill"):
                continue
            seen = per_case.setdefault(r["file"], {"lines": r.get("lines"), "max_to": 0, "whole": False})
            seen["whole"] |= bool(r.get("whole"))
            seen["max_to"] = max(seen["max_to"], r.get("to") or 0)
        for name, seen in per_case.items():
            s = stats.setdefault(name, {"lines": seen["lines"], "opened": 0, "to_end": 0})
            s["opened"] += 1
            s["to_end"] += seen["whole"] or (seen["lines"] and seen["max_to"] >= seen["lines"])
    if not stats:
        return
    n = len(rows)
    lines = [f"# Files read — {run_dir.name}", "", f"{n} case(s). \"Read to end\" counts cases that reached the file's last line.", "",
             "| File | Lines | Opened | Read to end |", "| --- | --- | --- | --- |"]
    for name, s in sorted(stats.items(), key=lambda kv: (-kv[1]["opened"], kv[0])):
        lines.append(f"| {name} | {s['lines'] or '—'} | {s['opened']}/{n} | {s['to_end']}/{s['opened']} |")
    (run_dir / "reads.md").write_text("\n".join(lines) + "\n")


def mobile(case_dir, result):
    """390px audit; its problems count as check errors so a page that breaks on phones fails."""
    page = case_dir / "page.html"
    if not page.exists():
        return
    data = mobile_audit(page)
    if data is None:
        result.setdefault("warnings", []).append({"rule": "mobile.skipped", "message": "390px audit skipped (needs node + playwright)"})
        return
    (case_dir / "mobile.json").write_text(json.dumps(data, indent=2))
    for problem in audit_problems(data):
        result.setdefault("errors", []).append({"rule": "mobile.layout", "message": problem})
    if data.get("error"):
        result.setdefault("warnings", []).append({"rule": "mobile.error", "message": data["error"][:160]})
    result["passed"] = not result.get("errors")
    (case_dir / "check.json").write_text(json.dumps(result, indent=2))
    with (case_dir / "check.txt").open("a") as f:
        f.writelines(f"ERROR mobile.layout: {p}\n" for p in audit_problems(data))


def judge(case, case_dir, model):
    page = case_dir / "page.html"
    if not page.exists():
        return None
    try:
        from judge_pages import judge_page
        return judge_page(page, case["prompt"], model)
    except Exception as exc:  # the judge is advisory; never fail the run on it
        (case_dir / "judge.json").write_text(json.dumps({"error": str(exc)[:200]}))
        return None


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
             "| Case | Result | Errors | Warnings | Unsupported claims | Judge overall | Cost | Time | Notes |",
             "| --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
    for case, meta, result in rows:
        cost = f"${meta['cost_usd']:.2f}" if meta.get("cost_usd") is not None else "—"
        secs = f"{meta['seconds']}s" if meta.get("seconds") is not None else "—"
        notes = meta.get("error") or (f"{meta['denials']} tool denials" if meta.get("denials") else "")
        first = result["errors"][0]["message"] if result.get("errors") else ""
        status = "PASS" if result.get("passed") else ("SKIPPED" if meta.get("infra") else "FAIL")
        lines.append(f"| {case['name']} | {status} | {len(result.get('errors', []))} | "
                     f"{len(result.get('warnings', []))} | {meta.get('claims', '—') if meta.get('claims') is not None else '—'} | {meta.get('judge_overall') or '—'} | {cost} | {secs} | {notes or first} |")
    passed = sum(1 for _, _, r in rows if r.get("passed"))
    skipped = sum(1 for _, m, _ in rows if m.get("infra"))
    ran = len(rows) - skipped
    total_cost = sum(m.get("cost_usd") or 0 for _, m, _ in rows)
    skip_note = f" · {skipped} skipped (usage limit — rerun them later with --cases)" if skipped else ""
    lines += ["", f"**{passed}/{ran} passed**{skip_note} · total cost ${total_cost:.2f}", "",
              "Details per case: `<case>/check.txt` (objective checks), `<case>/delivery.md` (QA report), `<case>/page.html`."]
    (run_dir / "summary.md").write_text("\n".join(lines) + "\n")
    summarize_reads(run_dir, rows)
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
    ap.add_argument("--judge", metavar="MODEL", help="also score screenshots with this judge model, e.g. opus")
    args = ap.parse_args()

    cases = json.loads(CASES_FILE.read_text())["evals"]

    if args.check_only:
        run_dir = Path(args.check_only)
        rows = []
        for case in cases:
            d = run_dir / case["name"]
            if d.exists():
                meta = json.loads((d / "meta.json").read_text()) if (d / "meta.json").exists() else {}
                result = check(case, d)
                mobile(d, result)
                rows.append((case, meta, result))
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
        mobile(d, result)
        if not args.no_audit:
            meta["claims"] = audit(case, d)
        if args.judge:
            verdict = judge(case, d, args.judge)
            meta["judge_overall"] = (verdict or {}).get("scores", {}).get("overall")
        (d / "meta.json").write_text(json.dumps(meta, indent=2))
        print(f"  {case['name']}: {'PASS' if result.get('passed') else 'FAIL'} ({meta.get('seconds')}s, unsupported claims: {meta.get('claims', '—')})")
        return case, meta, result

    with cf.ThreadPoolExecutor(max_workers=args.parallel) as pool:
        rows = list(pool.map(one, chosen))
    if args.judge:
        from judge_pages import log_run
        log_run(run_dir.name, args.judge, [(c, json.loads((run_dir / c["name"] / "judge.json").read_text()))
                                           for c, _, _ in rows if (run_dir / c["name"] / "judge.json").exists()])
    sys.exit(0 if summarize(run_dir, rows) else 1)


if __name__ == "__main__":
    main()
