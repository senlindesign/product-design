# Eval results log

One entry per full run. Newest first. Raw outputs live in `evals/runs/` (git-ignored).

Entries record the rules as they were on that date. Some have changed since. Example: the 2026-10-04 Contact fix ("social proof only with real logos/testimonials") was replaced on 2026-10-08 by the sample-content rule: missing evidence is filled with tagged sample content unless the user says they have none. The skill files are authoritative.

Screenshot-judge scores (`evals/judge_pages.py`) are logged separately in `evals/SCORES.md`.

## 2026-10-08/09 — after Steps 1–4 (sample content, real logos, product visuals, signature moves, copy, motion)

- **Change under test**: sample-content rule + claims check; real logos only; `shared/product-visuals.md`, `shared/signature-moves.md`, `shared/copy.md`, Product-Serving Motion; rhythm/copy/logo checks in the checker
- **Result**: 9/12 confirmed pass across three partial runs (`20261008-145338`, `20261008-195622`, `20261009-005526`). Not re-run: `product-colorful-light-integrations`, `downloads-editorial-light-cli`, `landing-business-light-brand` — usage limit three times; product and downloads passed the logo-rule run on 2026-10-08 (`20261008-085454`)
- **Unsupported claims (Haiku audit)**: 0–6 per page, down from 14+ on the old Pipewise page. Remaining types: invented integration lists, security specifics (TLS/AES), trial length → added to the master fabrication rule
- **Fixes during the runs**: Blog used custom layout tags (`grid-3col`, `split`) → markup errors are now strict and SKILL.md forbids custom names; contact phone regex false positive on "51-200 / 201-1000"; copyright lines excluded from the audit; one run hung for 7 min at the quota reset → runner timeout
- **Visual check (IT-directors page, old vs new)**: real-looking hero mock with colored status pills and non-round numbers; bento with a lead tile instead of four identical 3-card sections; sentence-case headlines; CTA no longer a question. Still restrained in Minimal; only the hero is a memorable moment
- **Cost**: ≈ $34 for generation + audits
- **Pending**: blind A/B test (4 pairs, Sonnet judge) after quota reset

## 2026-10-04 (night) — smoke set after the STE rewrite of SKILL.md rules

- **Change under test**: vague rule sentences in SKILL.md files rewritten as explicit conditions (ASD-STE100 style)
- **Result**: 4/4 pass after two tooling fixes
- `404-minimal-dark-bare` first "produced no HTML": the agent wrote to a path it guessed (`404-minimal-dark/`). Runner now gives the exact absolute output path
- `pricing-business-dark-agency` first "missed $19": `<span>$</span> <span>19</span>`. Checker now matches required text ignoring whitespace
- Pricing used a FAQ entry instead of a How It Works section for the switching barrier, and wrote unsupported claims ("setup in minutes", "no learning curve"). Pricing rule now says include How It Works; the master fabrication rule now covers speed/ease/result claims
- **Cost**: $8.43

## 2026-10-04 (evening) — re-run of the three open cases

- **Result**: **12/12 pass** across both runs
- `blog-editorial-dark-expert` PASS — no pagination for the six listed articles
- `contact-business-light-sales` PASS — sales email shown, no placeholder logos, social proof left out with a stated reason. First flagged a false positive: `border-left: 4px solid transparent` in a CSS dropdown-arrow triangle; the generating agent called it out as a false positive in its own QA report. Checker now ignores transparent borders
- `landing-business-light-brand` PASS — accent `#E4572E` and Manrope applied
- **Cost**: $4.89

## 2026-10-04 — first full run

- **Model**: Claude Code default in headless mode (`claude-opus-4-5` per `modelUsage`)
- **Coverage**: 11 of 12 cases ran; `landing-business-light-brand` was skipped twice by the account usage limit
- **Result**: 9/11 pass after fixing two checker/case issues (below); 2 real skill defects found and fixed, not yet re-run
- **Cost**: ≈ $25 across two sessions (≈ $1.1–2.9 per case)

| Case | Result | Notes |
| --- | --- | --- |
| landing-minimal-dark-developers | PASS | 5 syntax-highlight colors outside the style file, declared intentional in the QA report |
| landing-minimal-light-it-directors | PASS | security content was labeled `features`, not `security` → SKILL.md now says when to use `security` / `problem` |
| pricing-business-dark-agency | PASS | first failed on `$19` — checker bug: `<span>$</span>19` read as "$ 19"; fixed |
| blog-editorial-dark-expert | FAIL → fixed | "Load more" on a 6-article blog. Rule was ambiguous (no count → assume 10+); now a listed set of articles is the whole blog |
| landing-colorful-dark-oneliner | PASS | product mock colors outside the style file (intentional) |
| about-editorial-light-bare | PASS | |
| hero-business-section | PASS | used `max-width: 768px`; all remaining 768px mentions in skill files changed to 767px |
| contact-business-light-sales | FAIL → fixed | sales email omitted ("form-first archetype") and placeholder customer logos added. Contact skill said Sales-Focused "almost always" needs social proof; now only with real logos/testimonials, and given contact details must appear |
| product-colorful-light-integrations | PASS | |
| 404-minimal-dark-bare | PASS | |
| downloads-editorial-light-cli | PASS | first failed on missing `install` section — case was too strict (install block in a split hero is the intended pattern); case now accepts `install` or `hero` |
| landing-business-light-brand | not run | usage limit |

**Follow-up**: all three re-run in the evening entry above.
