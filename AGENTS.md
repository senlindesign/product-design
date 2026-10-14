# Working on this repo

Rules for anyone, human or agent, who changes the product-design skill. Each one comes from a mistake that reached a generated page at least once.

## What lives where

- `skills/product-design/` is the skill: the only folder loaded at runtime and copied on install. Files in it must never reference anything outside it.
  - `SKILL.md`: the entry point (routing, brief, Style precedence, design rules, QA report)
  - `pages/<type>/`: 8 page skills; `sections/<name>/`: 10 section skills
  - `shared/`: the four style files (`visual-style.md` = Minimal, `visual-style-{business,colorful,editorial}.md`) and the craft files (product visuals, signature moves, copy, atmosphere, motion)
  - `scripts/check_page.py`: the self-check the skill runs before delivery, also used by the evals
- `evals/`: the golden test set and its tools (see `evals/README.md`)
- `README.md` / `README.zh-CN.md`: the Chinese README is written natively, not translated. Change both together.

Published files are only: `skills/`, `README*.md`, `LICENSE`, `AGENTS.md`, `.claude-plugin/`, `docs/images/`, `evals/` (scripts and cases). The maintainer keeps research notes, validation pages and internal docs locally; `.gitignore` excludes them (`CLAUDE.md`, `docs/*.md`, `research/`, `validation/`). Never commit those paths, and never link to them from published files. Before committing, run:

```bash
grep -rnE "research/|validation/|docs/[A-Za-z-]+\.md|CLAUDE\.md" skills README*.md evals .claude-plugin
```

The only acceptable hits are lines that explain the split, like this one.

## Rules for changing the skill

1. **Shared values are quoted, never invented.** Any spacing, font size, color, radius, shadow or button size in a page or section skill must appear in the style file (Minimal values in `shared/visual-style.md`). If a value is missing, add it to the style file first, then quote it. When several files independently invent the same value, the system is missing a token. Add it once to the style file.
2. **The style file wins.** Page and section skills are written in Minimal values. With another style active, visual values come from that style file and structure comes from the page skill (*Style precedence* in `SKILL.md`). Label new token blocks as Minimal defaults. Never hard-code a Minimal-only rule (zero shadow, 2px buttons, 180px rhythm) as universal.
3. **A global rule change is swept through every file.** When a rule in `SKILL.md` or `shared/` changes, grep `pages/`, `sections/`, `shared/` and `evals/evals.json` for the old wording and update every hit. A local "almost always" in one page skill silently overrides a global rule.
4. **No invented facts, in pages or in docs.** Generated pages use tagged sample content (`data-sample`) for missing material and never pass it off as fact. Public numbers (sample counts, case counts, costs) must come from a source you can point to.
5. **Real logos only.** Iconify / Simple Icons / a text wordmark, marked with `data-logo-source`. Never draw a logo.
6. **When a rule keeps being skipped, make it checkable.** Agents skip rules near the end of long files. Put mandatory parts first or add a check to `check_page.py`; don't just repeat the rule more loudly.
7. **Recurring CSS traps.** These have broken generated pages before:
   - The `padding` shorthand on an element that also gets `.container` padding: use `padding-top` instead.
   - A light component reused on a dark band without an override, so it disappears.
   - `backdrop-filter` on a fixed nav creates a containing block that mis-positions the mobile menu.
   - `var()` names that are never defined.
8. **English** for every file except `README.zh-CN.md`.

## Pass bar for any change

A change is done when all of the following pass. Report each result; don't summarize it as "tested".

| Change touches | Required |
| --- | --- |
| Anything in `skills/` | `python3 skills/product-design/scripts/check_page.py --selftest` and the smoke set: `python3 evals/run_evals.py` |
| A style file, `shared/` craft files, or hero/section layouts | Also the style matrix with the screenshot judge: `python3 evals/run_evals.py --cases 13,14,15,16 --judge opus`. Open the desktop and mobile screenshots and look at them. |
| A page skill | Also that page's cases in `evals.json`, including at least one non-Minimal style in dark mode |
| A reported bad output | First add a case to `evals/evals.json` that reproduces it and fails, then fix, then show it passes |
| `check_page.py` or eval tools | Run them against a known-good page (no false positives) and a deliberately broken one (each check fires) |

A run passes when every case passes the checker, including the 390px audit, and the judge reports no visible defect in the hero. Record full runs in `evals/RESULTS.md`; judge averages go to `evals/SCORES.md` automatically.

**Environment.** The runner needs the `claude` CLI (headless, `claude -p`) and Chrome or Chromium. The 390px audit also needs Node with the `playwright` package. Each generated page costs about $1–3, so the smoke set costs about $5 and the full set $20–30. Get the maintainer's budget before running more than the smoke set. A usage-limit stop is reported as SKIPPED, not FAIL; rerun those cases later and never count them as skill failures. Record the model used with every result.
