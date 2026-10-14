# Evals

A golden test set and an automatic checker for the product-design skill. Use them to find out whether a change made the skill better or quietly broke something.

## What's here

| File | What it is |
| --- | --- |
| `evals.json` | 19 fixed requests in [skill-creator](https://github.com/anthropics/skills) format. Together they cover all 8 page types plus a single section, all 4 styles, light and dark, and depth levels 0–3. Cases 13–16 (`style-matrix-*`) give one brief to each style; cases 17–19 put non-Minimal styles and Minimal dark on Pricing, About and Blog. Each case has `expectations` (plain-language statements for a human or LLM judge) and `checks` (verified by script). |
| `run_evals.py` | Runs cases through headless Claude Code with this repo loaded as a plugin, then checks every page, runs the 390px audit, and records which skill files the agent read. |
| `screens.py` | Desktop (1440px) and mobile (390px) screenshots, and the 390px audit: sideways overflow, more than one nav visible, nav links with no menu toggle, a toggle that opens nothing. Finds Chrome on macOS and Linux (`$CHROME` overrides). The 390px screenshot and audit need Node with the `playwright` package (Chrome's CLI can't render below ~500px wide). Without it the audit is skipped with a warning and the judge can't run. |
| `judge_pages.py` | Screenshot judge: scores each page 1–10 on looks real, product visual, layout variety, copy, mobile, overall, and lists visible defects. Logs run averages to `SCORES.md`. |
| `audit_claims.py` | LLM claims audit (Haiku): lists claims on the page that the request doesn't support. Run automatically by `run_evals.py`. |
| `blind_test.py` | Blind A/B between two runs of the same cases: which version looks less AI-made. |
| `../skills/product-design/scripts/check_page.py` | The checker. The skill also runs it on its own output before delivering (Step 4.7 of `SKILL.md`). |

## Run

```bash
python3 evals/run_evals.py                          # smoke set: 4 cases
python3 evals/run_evals.py --cases all              # all 12
python3 evals/run_evals.py --cases 3,7              # by id or name
python3 evals/run_evals.py --model sonnet           # walk down: opus → sonnet → haiku
python3 evals/run_evals.py --check-only evals/runs/<run>   # re-check without regenerating
python3 evals/run_evals.py --cases 13,14,15,16 --judge opus   # style matrix + screenshot judge
python3 evals/judge_pages.py evals/runs/<run>        # judge an existing run
python3 evals/screens.py page.html --mobile-audit    # screenshots + 390px audit for any page
```

Each run writes to `evals/runs/<timestamp>-<model>/` (git-ignored): a `summary.md` table, `reads.md` (which skill files were opened and whether they were read to the last line), and per case `page.html`, `check.txt` (objective checks, including 390px audit errors), `mobile.json`, `delivery.md` (the delivery message and QA report), `claude.json` (cost, turns, tool denials), `claude.jsonl` (the full stream), and, with `--judge`, screenshots and `judge.json`.

**Cost**: each case is a full page generation. Measured on 2026-10-04 with the default model: $1.1–1.4 and 1–2 minutes per case, so about $5 for the smoke set and $20–30 for all 19 (larger pages cost more; the latest style-matrix pages cost about $2.70 each). The screenshot judge adds about $0.10–0.30 per page with opus. Use the smoke set for everyday changes and the full set before a release.

## When to run

- **Any change** to `SKILL.md`, a page or section skill, or a style file → smoke set.
- **After editing a style file** → `python3 skills/product-design/scripts/check_page.py --selftest` first. It confirms the values the checker expects still appear in the style files, and that the section names match `SKILL.md`.
- **Any change that affects how pages look** (style files, `shared/` craft files, hero or section layouts) → also the style matrix (cases 13–16) with `--judge opus`, and look at the screenshots yourself.
- **Before a release** → full set, then the same set on smaller models to see where quality drops.
- **Fixing a reported bad output** → first add a case that reproduces it and fails, then fix the skill, then confirm the case passes. Every fixed bug becomes a permanent test.

## What the checker covers

| Area | Checks |
| --- | --- |
| Structure | exactly one `<h1>`; viewport meta; required, forbidden, and recommended sections; section count |
| CSS correctness | `var()` used but never defined; `width: 100vw` |
| House rules | no left-edge stripe on cards; fixed nav has backdrop blur; animation guarded by `prefers-reduced-motion`; `:focus-visible`; 767px breakpoint |
| Style fidelity | display font; accent; button radius; zero shadow in Minimal; grid width; nav height; colors outside the style file |
| Content | given facts appear (prices, emails, install commands); fabricated ones don't ("Most Popular", "save 20%", invented version numbers and phone numbers) |

It doesn't judge visual quality, copy, or whether the archetype was a good choice. Those are the `expectations` in each case, for a human or an LLM judge; `judge_pages.py` scores the visual part from screenshots. The 390px audit (`screens.py`) adds layout errors on narrow screens.

Structure checks rely on the markup conventions in `SKILL.md` (`data-page`, `data-style`, `data-theme`, `data-archetype` on `<html>`, `data-section` on each section). In evals, `--strict` turns style deviations and unknown section names into errors.

## Adding a case

Copy an existing entry in `evals.json` and give it a new `id` and a descriptive `name`. Keep `checks` to things that must be true whatever creative choices the skill makes: facts the user gave, sections that must or must not exist, the requested style. Section names come from the vocabulary in `SKILL.md`. Set `"smoke": true` only when the case covers a seam the smoke set doesn't already cover.
