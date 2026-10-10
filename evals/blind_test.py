#!/usr/bin/env python3
"""Blind A/B test: does a newer version of the skill produce pages that look less AI-made?

Screenshots the same case from two eval runs, shows them to a judge in random order, and
decodes the result afterwards.

  python3 evals/blind_test.py --before evals/runs/<old-run> --after evals/runs/<new-run>
  python3 evals/blind_test.py --before ... --after ... --cases 2,3,9 --model opus
"""
import argparse
import json
import random
import subprocess
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CASES_FILE = REPO / "evals" / "evals.json"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
CRITERIA = ["looks_real", "product_visual", "layout_variety", "copy", "overall"]

PROMPT = """You are a senior product designer judging two landing-page drafts for the same brief.

BRIEF:
---
{brief}
---

Read both screenshots with the Read tool:
- Page A: {a}
- Page B: {b}

Score each page 1–10 on:
- looks_real: would a designer believe this is a real, shipped product site rather than an AI draft?
- product_visual: does the product visual look like a real product (specific content, real-looking data, one focused state) rather than grey placeholder boxes?
- layout_variety: do sections vary in layout and rhythm, with one or two memorable moments, rather than repeating one template?
- copy: are headlines specific and human (concrete nouns, short) rather than generic AI phrasing?
- overall: which would you rather ship?

Judge only what you see. Reply with JSON only:
{{"A": {{"looks_real": n, "product_visual": n, "layout_variety": n, "copy": n, "overall": n}},
  "B": {{...same keys...}},
  "winner": "A" | "B" | "tie",
  "reason": "<one sentence>"}}"""


def screenshot(page, out, height=6000):
    subprocess.run([CHROME, "--headless=new", "--hide-scrollbars", "--disable-gpu",
                    f"--window-size=1440,{height}", "--virtual-time-budget=6000",
                    f"--screenshot={out}", page.resolve().as_uri()],
                   capture_output=True, timeout=120)
    return out.exists()


def judge(brief, a, b, model):
    out = subprocess.run(["claude", "-p", PROMPT.format(brief=brief, a=a, b=b), "--model", model,
                          "--allowedTools", "Read", "--add-dir", str(a.parent),
                          "--output-format", "json"], capture_output=True, text=True, timeout=600,
                         stdin=subprocess.DEVNULL)
    res = json.loads(out.stdout)
    raw = res.get("result") or ""
    data = json.loads(raw[raw.find("{"): raw.rfind("}") + 1])
    data["cost_usd"] = res.get("total_cost_usd")
    return data


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--before", required=True, nargs="+", help="one or more older run dirs (latest page per case wins)")
    ap.add_argument("--after", required=True, nargs="+", help="one or more newer run dirs")
    ap.add_argument("--cases", default="all")
    ap.add_argument("--model", default="opus")
    ap.add_argument("--seed", type=int, default=7)
    args = ap.parse_args()

    def latest(dirs, name):
        found = [Path(d) / name / "page.html" for d in dirs if (Path(d) / name / "page.html").exists()]
        return found[-1] if found else None

    cases = json.loads(CASES_FILE.read_text())["evals"]
    if args.cases != "all":
        wanted = {c.strip() for c in args.cases.split(",")}
        cases = [c for c in cases if str(c["id"]) in wanted or c["name"] in wanted]

    out_dir = REPO / "evals" / "runs" / f"blind-{datetime.now():%Y%m%d-%H%M%S}"
    out_dir.mkdir(parents=True)
    rng = random.Random(args.seed)
    rows = []
    for case in cases:
        old, new = latest(args.before, case["name"]), latest(args.after, case["name"])
        if not (old and new):
            continue
        flip = rng.random() < 0.5
        a_src, b_src = (new, old) if flip else (old, new)
        a, b = out_dir / f"{case['name']}-A.png", out_dir / f"{case['name']}-B.png"
        if not (screenshot(a_src, a) and screenshot(b_src, b)):
            print(f"  {case['name']}: screenshot failed")
            continue
        try:
            verdict = judge(case["prompt"], a, b, args.model)
        except Exception as exc:
            print(f"  {case['name']}: judge failed ({exc})")
            continue
        new_key = "A" if flip else "B"
        old_key = "B" if flip else "A"
        winner = verdict.get("winner")
        result = {"case": case["name"], "new_is": new_key, "verdict": verdict,
                  "new_won": winner == new_key, "tie": winner == "tie",
                  "delta": {k: verdict[new_key][k] - verdict[old_key][k] for k in CRITERIA}}
        rows.append(result)
        (out_dir / f"{case['name']}.json").write_text(json.dumps(result, indent=2))
        print(f"  {case['name']}: new {'WON' if result['new_won'] else 'tie' if result['tie'] else 'lost'} · Δoverall {result['delta']['overall']:+d}")

    if not rows:
        print("no comparable cases")
        return
    lines = [f"# Blind test — {out_dir.name}", "", f"Before: {', '.join(args.before)}  ", f"After: {', '.join(args.after)}  ",
             f"Judge: {args.model}, pages shown in random order", "",
             "| Case | Winner | " + " | ".join(f"Δ {k}" for k in CRITERIA) + " | Reason |",
             "| --- | --- | " + " | ".join("---" for _ in CRITERIA) + " | --- |"]
    for r in rows:
        w = "new" if r["new_won"] else "tie" if r["tie"] else "old"
        lines.append(f"| {r['case']} | {w} | " + " | ".join(f"{r['delta'][k]:+d}" for k in CRITERIA) + f" | {r['verdict'].get('reason', '')} |")
    n = len(rows)
    avg = {k: sum(r["delta"][k] for r in rows) / n for k in CRITERIA}
    lines += ["", f"**New version won {sum(r['new_won'] for r in rows)}/{n}** (ties {sum(r['tie'] for r in rows)}). "
              "Average change: " + ", ".join(f"{k} {avg[k]:+.1f}" for k in CRITERIA)]
    (out_dir / "summary.md").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
