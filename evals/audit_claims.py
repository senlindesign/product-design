#!/usr/bin/env python3
"""Claims audit: list factual claims on a generated page that the user's request never supported.

Content marked `data-sample` is excluded — it is declared filler and is listed in the QA report.

  python3 evals/audit_claims.py <page.html> --case-id <name>      # prints JSON
"""
import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CASES_FILE = REPO / "evals" / "evals.json"
CHECKER = REPO / "skills" / "proof" / "scripts" / "check_page.py"

PROMPT = """You audit a generated marketing page for invented facts.

USER REQUEST (the only source of truth):
---
{request}
---

PAGE TEXT (visible text, excluding content the page itself declared as sample filler):
---
{text}
---

List every factual claim in PAGE TEXT that USER REQUEST does not support. Factual claims are:
numbers and metrics, prices, customer or company names, people, testimonials, certifications or
compliance (SOC 2, HIPAA, ISO, GDPR), security specifics (encryption standards), awards, integration
names or counts, dates, and concrete promises about speed, ease, or results ("set up in minutes",
"no learning curve", "2x faster").

Do NOT list: data that is clearly part of a product UI mockup (table rows, dashboard counts, timestamps,
sample records), the product name and its description from the request, generic benefit phrasing that
restates the request, navigation/footer labels, copyright lines, button text, section headings that make no factual
claim, or text in [brackets].

Reply with JSON only: {{"unsupported": [{{"claim": "<exact text>", "type": "<metric|customer|certification|security|integration|promise|other>"}}]}}"""


def page_text(page):
    spec = importlib.util.spec_from_file_location("check_page", CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    p = mod.PageParser()
    p.feed(Path(page).read_text(encoding="utf-8", errors="replace"))
    return mod.norm("".join(p.text))


def audit(page, request, model="haiku"):
    text = page_text(page)[:12000]
    out = subprocess.run(["claude", "-p", PROMPT.format(request=request, text=text),
                          "--model", model, "--output-format", "json", "--max-turns", "1"],
                         capture_output=True, text=True, timeout=300, stdin=subprocess.DEVNULL)
    res = json.loads(out.stdout)
    raw = (res.get("result") or "").strip()
    start, end = raw.find("{"), raw.rfind("}")
    data = json.loads(raw[start:end + 1]) if start != -1 else {"unsupported": [], "error": raw[:200]}
    data["cost_usd"] = res.get("total_cost_usd")
    return data


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page")
    ap.add_argument("--case-id", required=True)
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--json", help="write the result to this path")
    args = ap.parse_args()
    case = next(c for c in json.loads(CASES_FILE.read_text())["evals"] if c["name"] == args.case_id or str(c["id"]) == args.case_id)
    result = audit(args.page, case["prompt"], args.model)
    if args.json:
        Path(args.json).write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
