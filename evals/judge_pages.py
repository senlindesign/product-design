#!/usr/bin/env python3
"""Screenshot judge: scores each page on a fixed visual rubric, so visual quality is measured on every run.

The checker (check_page.py) sees structure and values; it cannot see an empty hero, a cutout covering the
product, or a squashed mobile layout. This script screenshots each page (1440px and 390px), asks a judge model
to score it against the rubric below, and logs averages to evals/SCORES.md so runs can be compared over time.

  python3 evals/judge_pages.py evals/runs/<run>                 # every case in a run
  python3 evals/judge_pages.py evals/runs/<run> --cases 13,14   # some cases
  python3 evals/judge_pages.py path/to/page.html --brief "landing page for ..."

Cost: one judge call per page (about $0.10–0.30 with opus). Keep the judge model fixed when comparing runs.
"""
import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from screens import audit_problems, mobile_audit, shoot_both  # noqa: E402

REPO = Path(__file__).resolve().parent.parent
CASES_FILE = REPO / "evals" / "evals.json"
SCORES = REPO / "evals" / "SCORES.md"
CRITERIA = ["looks_real", "product_visual", "layout_variety", "copy", "mobile", "overall"]

PROMPT = """You are a senior product designer reviewing one generated website page. Judge only what you see.

BRIEF the page was built from:
---
{brief}
---

Read both screenshots with the Read tool:
- Desktop, 1440px wide (top of a tall page): {desktop}
- Mobile, 390px wide (first three screens): {mobile}

Score 1–10 with these anchors (10 = indistinguishable from a top product site such as Linear, Stripe or Notion;
7 = a competent shipped site; 5 = a typical AI template; 3 = visibly broken or empty):
- looks_real: would a designer believe this is a real, shipped product site rather than an AI draft?
- product_visual: does the main product visual look like a real product (specific content, real-looking data,
  one focused state), visible in the first screen, not covered or cropped, not grey placeholder boxes?
- layout_variety: do sections vary in layout and background, with one or two memorable moments?
- copy: are headlines specific and human (concrete nouns, short), not generic AI phrasing?
- mobile: at 390px, is everything readable, stacked sensibly, nothing cut off or overlapping, one nav?
- overall: how close is this to something you would ship?

Then list every visible defect you can point to (empty or sparse hero, product visual below the fold, element
covering the product, overlapping text, unreadable contrast, broken image, duplicated nav, sideways overflow,
placeholder boxes). Use an empty list if there are none.

Reply with JSON only:
{{"scores": {{"looks_real": n, "product_visual": n, "layout_variety": n, "copy": n, "mobile": n, "overall": n}},
  "defects": ["<short description, where on the page>", ...],
  "summary": "<one sentence>"}}"""


def judge(brief, desktop, mobile, model):
    out = subprocess.run(["claude", "-p", PROMPT.format(brief=brief, desktop=desktop, mobile=mobile),
                          "--model", model, "--allowedTools", "Read", "--add-dir", str(desktop.parent),
                          "--output-format", "json"],
                         capture_output=True, text=True, timeout=600, stdin=subprocess.DEVNULL)
    res = json.loads(out.stdout)
    raw = res.get("result") or ""
    data = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
    data["cost_usd"] = res.get("total_cost_usd")
    data["model"] = model
    return data


def judge_page(page, brief, model, out_dir=None):
    """Screenshot, audit, and judge one page. Writes judge.json next to the screenshots and returns it."""
    page = Path(page)
    out_dir = Path(out_dir or page.parent)
    desktop, mobile = shoot_both(page, out_dir)
    if not desktop:
        return {"error": "screenshot failed"}
    result = judge(brief, desktop, mobile, model)
    audit = mobile_audit(page)
    if audit is not None:
        result["mobile_audit"] = audit
        result["mobile_problems"] = audit_problems(audit)
    (out_dir / "judge.json").write_text(json.dumps(result, indent=2, ensure_ascii=False))
    return result


def log_run(label, model, rows):
    """Append one line per judged run to evals/SCORES.md (averages per criterion)."""
    scored = [r for _, r in rows if "scores" in r]
    if not scored:
        return
    avg = {k: sum(r["scores"][k] for r in scored) / len(scored) for k in CRITERIA}
    if not SCORES.exists():
        SCORES.write_text("# Screenshot judge scores\n\nOne row per judged run, written by `evals/judge_pages.py`. "
                          "Scores are 1–10 averages; compare rows only when the judge model is the same.\n\n"
                          "| Date | Run | Judge | Pages | " + " | ".join(CRITERIA) + " | Defects |\n"
                          "| --- | --- | --- | --- | " + " | ".join("---" for _ in CRITERIA) + " | --- |\n")
    defects = sum(len(r.get("defects", [])) for r in scored)
    with SCORES.open("a") as f:
        f.write(f"| {datetime.now():%Y-%m-%d} | {label} | {model} | {len(scored)} | "
                + " | ".join(f"{avg[k]:.1f}" for k in CRITERIA) + f" | {defects} |\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="an eval run directory, or one HTML file")
    ap.add_argument("--cases", default="all", help="with a run directory: all, or comma-separated ids/names")
    ap.add_argument("--brief", help="with an HTML file: the request the page was built from")
    ap.add_argument("--model", default="opus")
    ap.add_argument("--no-log", action="store_true", help="don't append to evals/SCORES.md")
    args = ap.parse_args()

    target = Path(args.target)
    if target.is_file():
        r = judge_page(target, args.brief or "(no brief given)", args.model)
        print(json.dumps(r, indent=2, ensure_ascii=False))
        return

    cases = json.loads(CASES_FILE.read_text())["evals"]
    if args.cases != "all":
        wanted = {c.strip() for c in args.cases.split(",")}
        cases = [c for c in cases if str(c["id"]) in wanted or c["name"] in wanted]
    rows = []
    for case in cases:
        page = target / case["name"] / "page.html"
        if not page.exists():
            continue
        try:
            r = judge_page(page, case["prompt"], args.model)
        except Exception as exc:
            r = {"error": str(exc)[:200]}
        rows.append((case, r))
        s = r.get("scores")
        print(f"  {case['name']}: " + (f"overall {s['overall']} · {len(r.get('defects', []))} defects" if s else f"error: {r.get('error')}"))

    if not rows:
        print("no pages found")
        return
    lines = [f"# Screenshot judge — {target.name}", "", f"Judge: {args.model}", "",
             "| Case | " + " | ".join(CRITERIA) + " | Defects | 390px audit |",
             "| --- | " + " | ".join("---" for _ in CRITERIA) + " | --- | --- |"]
    for case, r in rows:
        if "scores" not in r:
            lines.append(f"| {case['name']} | " + " | ".join("—" for _ in CRITERIA) + f" | error: {r.get('error')} | |")
            continue
        mob = "; ".join(r.get("mobile_problems", [])) or ("clean" if "mobile_audit" in r else "not run")
        lines.append(f"| {case['name']} | " + " | ".join(str(r["scores"][k]) for k in CRITERIA)
                     + f" | {'; '.join(r.get('defects', [])) or '—'} | {mob} |")
    (target / "judge.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    if not args.no_log:
        log_run(target.name, args.model, rows)


if __name__ == "__main__":
    main()
