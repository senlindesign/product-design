---
name: product-design
description: Design and build marketing website pages — landing page, homepage, pricing, about, contact, product/features, blog index, 404, downloads — or a single section (hero, features, social proof, CTA, FAQ, how it works, comparison table, contact form, navigation, footer). Decides page structure from a short brief (audience, goal, barriers, available evidence), then renders it in one of 4 visual styles (Minimal, Business, Colorful, Editorial), light or dark. Use when the user asks to design, build, mock up, or redesign a product website, marketing site, landing page, homepage, features page, or a section of one — including requests to make a page look less generic or less AI-generated.
argument-hint: "[page-or-section] [minimal|business|colorful|editorial] [light|dark]"
user-invocable: true
allowed-tools: Read, Write, Edit, Glob, Bash(open:*), Bash(python3:*)
---

# Product Design

The goal: a first draft that looks like a shipped product page, not an AI template.

Everything here was learned from 400+ real product pages. The skill decides *who* the page is for and *which sections* earn their place, then builds it in a style with its own character — a signature hero, a real-looking product with motion, varied section layouts, real logos, and finished sample content where the user gave none. Before delivery it checks its own work and reports what it filled in.

Scope: **marketing website pages** (8 page types, 10 standalone sections). Not app UI, dashboards, or multi-page flows. All knowledge is embedded — works offline, no external services.

**Paths**: every path in this skill is relative to the folder containing this file. Inside a page skill, `references/...` means that page skill's own `references/` folder.

---

## Quick Start

```
/product-design                          → short design conversation, then a page
/product-design landing                  → generates right away (Minimal, light)
/product-design pricing editorial dark   → page type + style + theme
/product-design hero colorful            → a single section
```

Arguments can come in any order. Accepted values:

| Kind | Values |
|---|---|
| Page | `landing` (also: home, homepage), `pricing`, `contact`, `about`, `product`, `blog`, `404`, `downloads` |
| Section | `hero`, `features`, `social-proof`, `cta`, `faq`, `how-it-works`, `comparison-table`, `contact-form`, `navigation`, `footer` |
| Style | `minimal` (default), `business`, `colorful`, `editorial` |
| Theme | `light` (default), `dark` |

`product` is the Product page; `features` is the Features section.

### Depth: the user decides how much to give

Never ask for more than the current level needs. Each level uses everything the user already gave.

| Level | User gives | What happens |
|---|---|---|
| 0 | Just a page type (`/product-design landing`) | Page generated immediately with the default archetype, full sections, and tagged sample content |
| 1 | A sentence about the product ("landing page for a scheduling tool for clinics") | Archetype, style, and copy inferred from it |
| 2 | A brief — audience, goal, barriers, evidence, brand (or a pasted PRD / brand guideline) | Full structural decisions from the Step 2 signal table: sections added, skipped, reordered |
| 3 | Expert controls (below) | Applied as given; the skill fills in everything else |

**Expert controls** — honor any of these when the user states them, without asking for confirmation:
- **Archetype** by name or letter, e.g. "pricing, archetype B" or "usage-based pricing" (names below)
- **Sections**: include, exclude, or reorder ("no FAQ", "put social proof second", "add a comparison table")
- **Layout pattern** for a section, when the section skill offers several ("features as a bento grid")
- **Brand tokens**: accent hex, display font
- **Output**: standalone HTML or the project's stack (Step 4.7), file name, location
- **Motion**: "no animation" removes all optional motion

| Page | Archetypes |
|---|---|
| Landing | A SaaS Tool · B SaaS Platform · C Developer Tool · D Creative / Design Tool |
| Pricing | A Feature-Tiered · B Usage-Based · C Simple Binary · D Enterprise-First |
| Contact | A Simple Contact · B Department Routing · C Sales-Focused · D Support Hub |
| About | A Company Story · B Team-First · C Mission-Driven |
| Product | A Feature Showcase · B Platform Overview · C Product Deep-Dive |
| Blog | A Grid Index · B Editorial · C Minimal List |
| 404 | A Minimal Redirect · B Navigational Recovery · C Brand Moment |
| Downloads | A Platform Selector · B Multi-Product · C Developer Distribution |

---

## Step 1 — Pick the route

**Fast route** — the request names a page type or section (as an argument or in plain words). Do not ask questions first.
- Use whatever the conversation already says about the product, audience, and content.
- Style: the argument, else a recommendation from context (see Step 2 logic), else Minimal. Theme: the argument, else Light.
- Choose the archetype from available signals; with no signals, use the page skill's default archetype.
- Page skills list some inputs as "Required — ask". That applies to the guided route only; on the fast route, a missing required input (even the product name) becomes a labeled placeholder like `[Company]`.
- Generate (Step 4). Copy written from what the user said (headline, subtitle, feature framing) is fine. Material the user didn't give — testimonials, customer logos, metrics, certifications, team, feature specifics — becomes **sample content** (see *Sample content* in Design Rules), so the page is full and easy to react to.
- After delivery, offer the next level in two or three lines: the 2–3 questions from Step 2 whose answers would change *this* page's structure most (e.g., "No testimonials yet? I'll drop Social Proof and lead with How It Works."), plus one line noting that archetype, sections, style, and brand can be set directly.

**Guided route** — no page type and the request is too vague to act on (e.g., "make me a website", or just a product name).
- Ask **one round** of questions, grouped in a single message. Include the content questions from Step 3 in that same round. Never ask a second round before generating.
- After the answers, show the compact proposal (Step 2), then generate in the same turn. Ask instead only if the page type itself is still unclear.

Explicit user preferences always override recommendations.

---

## Step 2 — Brief and recommendation

### What to learn (ask or infer; skip anything already clear)

**1. What and who** — "What are you building, and who is this page for?"
→ page type, explanation depth, archetype, language register.

**2. Goal** — "What should someone do after seeing this page?"
→ primary CTA, page length, urgency. "Sign up free" and "book a demo with sales" produce different pages.

**3. Barriers** — "What might stop them?"
→ which objection-handling sections to include and where. Integration effort → How It Works / integrations. Trust → social proof early.

**4. Evidence** — "What real materials do you have — screenshots, customer quotes, metrics, case studies?"
→ what is real. Given material is used as-is. If the user says they have none of something ("no testimonials yet"), leave that section out. If the user doesn't mention it, include the section with tagged sample content.

**5. Brand** — "Any brand colors, fonts, or visual direction?"
→ style recommendation and overrides. Accept a hex code + font name, or a pasted brand guideline (extract automatically).

Don't ask design-jargon questions ("which archetype?"), questions whose answers wouldn't change the page, or anything already answered.

### Proposal format

```
Project:   [product] — [one-line description]
Audience:  [who visits, what they know]
Goal:      [primary action]
Barrier:   [main concern]
Evidence:  screenshots ✓ / testimonials ✗ / metrics ✗

Page:      Landing Page
Style:     Minimal · Dark
Approach:  Problem explanation → product visual → sequential workflow
           → integration section → FAQ → CTA
Skipping:  Social Proof (no testimonials), Stats (no real data)
Brand:     [#hex] · [font] (or "style defaults")
```

### Recommendation logic

**Page type** — from the user's goal:
- Presenting a product to new visitors → Landing
- Explaining plans and pricing → Pricing
- Collecting inquiries or support requests → Contact
- Telling a company/team story → About
- Deep-diving into features for evaluators → Product
- Publishing articles → Blog
- Handling missing routes → 404
- Distributing installs → Downloads
- Several pages requested → build them one at a time with shared brand context.

**Style** — from audience and tone, not product category:
- Technical precision, developer audience, "let the product speak" → **Minimal**
- Enterprise B2B, trust and reassurance, warm professionalism → **Business**
- Creative tools, consumer products, personality and warmth → **Colorful**
- AI/research, editorial authority, content depth → **Editorial**
- "B2B" alone doesn't mean Business. A developer tool sold to enterprises may be Minimal; a consumer AI product may be Editorial.

**Theme** — Light unless the product is developer- or code-heavy, or the user wants dark. Editorial has built-in dark hero/CTA sections in either theme.

**Section decisions** — where the brief earns its value:

| Brief signal | Design consequence |
|---|---|
| Audience unfamiliar with the category | Explanation section early (problem/solution or How It Works) |
| Main barrier is trust or credibility | Social proof near the top; security/compliance if B2B |
| Main barrier is complexity or effort | How It Works, integration walkthrough |
| User says there are no testimonials or case studies | Leave Social Proof out — say so in the delivery note |
| User says there are no real numbers | Leave Stats out |
| User says nothing about evidence | Include the archetype's evidence sections (social proof, logos, stats, security) with tagged sample content |
| Value is sequential (step 1 → 2 → 3) | How It Works workflow instead of parallel feature cards |
| Multiple distinct audiences | Use Cases / "Who it's for" section |
| Competitor comparison matters | Comparison Table |
| High-intent traffic (email campaigns, known users) | Shorter page, fewer sections, direct CTA |
| Real product screenshots available | Use them as the hero visual — beats any synthetic mock |

Carry these decisions into the page skill's archetype selection and section composition. They change what the page contains and its order, not just its copy.

---

## Step 3 — Content (asked inside the Step 1 question round, never separately)

Everything not provided becomes tagged sample content (Design Rules → *Sample content*), except what the user said they don't have.

- **Landing**: 3 key features (name + one sentence). Optional: company names for a logo strip.
- **Pricing**: 2–3 plan names and prices, 3–5 features per plan. Optional: billing toggle, trial language.
- **Contact**: primary email. Optional: location, phone, department names.
- **About**: mission (1–2 sentences). Optional: team (name + role, up to 8), stats, founding year.
- **Product**: 3–4 capabilities. Optional: audiences, integration names.
- **Blog**: 4–6 article titles with categories. Optional: featured article.
- **404**: nothing needed.
- **Downloads**: platforms (macOS / Windows / Linux / iOS / Android). Optional: install command.

---

## Step 4 — Generate

1. **Read the active style file in full, to the last line** (Appendix). It is the visual foundation. Its last section, **Style Signature**, is mandatory, not decoration:
   - The hero uses the style's **Hero showcase** (its backgrounds and textures come from `shared/atmosphere.md`) unless the user asks for a different hero or the page skill's archetype has no hero (404, single sections other than hero). Start from the showcase's HTML example and keep its class names (`.specimen-field`, `.biz-stage`, `.hero-scene`, `.ed-stage`); the self-check looks for them. The Style Signature replaces the page skill's hero layout (its centered stack, M3, etc.); keep the page skill's hero content rules (headline, CTAs, archetype copy).
   - Use at least two of the style's **Signature details** across the page.
   - Follow its **Motion personality** and **Drift guard**; before delivering, run its **Screenshot test** against the page.

2. **Apply Style precedence** (below) before opening the page skill.

3. **Plan the page's craft before writing code** — do this once the page skill (item 5) has chosen the archetype and section list, and before any section is built:
   - Read `shared/signature-moves.md`. Choose the page's signature moves (§5 selection guide) and write a section plan: each section with its `data-layout`, `data-bg`, and `data-bold`. The plan must pass rules R2–R6: no two adjacent sections share a layout, background changes at roughly every other boundary, 1–2 bold sections (0–1 on Pricing, Contact, 404, Downloads), at most one equal-card grid. **Layout precedence**: when a page skill's default layout would repeat the previous section's layout, use that section's alternative pattern or a catalog move instead.
   - **Style layout defaults.** Styles must differ in structure, not only in color. Unless the brief or the user says otherwise, build the main sections with the active style's defaults (moves from `shared/signature-moves.md`):

     | Section role | Minimal | Business | Colorful | Editorial |
     |---|---|---|---|---|
     | Hero | Specimen Field (§12.2) | Framed product stage, M4 + M3 (§10) | Scene panel, M4 (§10) | Full-bleed dark stage, M4 (§10) |
     | Features | Numbered specimen rows: `split-left` / `split-right` alternating, mono index numbers, one product fragment per row | M5 bento, lead tile as a small gradient stage | Scene chapters: one major feature per `split-left` / `split-right` section, alternating sides, the second chapter inside a scene | M7 big-type list or M8 sticky chapter tabs (`walkthrough`), with the 260px margin column |
     | Steps / how it works | `list` with index rules | M9 step rail (`split-left`) | `card-grid` of paper cards | `list` in the margin-column layout |
     | Proof | `logo-row` in mono labels; quote as plain `big-quote` | M11 stat bento or shadowed testimonial cards | M10 poster quote in the second scene | M10 poster quote on `alt` |
     | Closing | `centered-stack` CTA + M14 wordmark footer | `centered-stack` CTA | CTA inside a scene | Dark stage CTA |

     Then apply R2–R6. If a default would repeat the previous section's layout, take the next row's layout or swap split sides.
   - If the page has a product visual (hero, features, bento), read `shared/product-visuals.md` and pick a recipe for each visual. No grey skeleton bars or empty boxes as a main visual.
   - Read `shared/copy.md` before writing any headline, heading, or button label.

4. **Read `shared/interaction-patterns.md` selectively**: §1 Motion Tokens, §1.5 Product-Serving Motion (whenever there is a `data-mock` visual), §13 Page-Type Animation Map, and §11 Mobile Nav Toggle (every page with a nav needs it), then only the recipe sections the map lists for the sections on this page (and §14 Combined Script Template when using three or more patterns). All motion is a progressive enhancement inside `prefers-reduced-motion`.

5. **Read the page or section skill** (Appendix) and follow its workflow, carrying the brief forward. After its archetype and section-composition steps, do item 3 (craft plan), then continue with its build steps:
   - Archetype selection uses the brief's audience and goal signals, not just product category.
   - Section composition applies the Step 2 decisions: skip sections whose evidence is missing; add sections that answer stated barriers.
   - Where a section has several layout patterns, pick the one that fits the brief (workflow layout for sequential value, card grid for parallel features).

6. **Brand overrides** (only if provided):
   - Color → `--accent: [hex]; --accent-text: [white or black for contrast]`
   - Font → `--font-display: '[Name]', [fallback]` + Google Fonts `<link>`
   - None → keep the style preset's values exactly.

7. **Output**:
   - Default: one self-contained `.html` file (all CSS in `<style>`, all JS in `<script>`, responsive, no dependencies except Google Fonts), named `[product]-[page-type]-[theme].html`, in the working directory unless the user names a location.
   - If the user asks to add the page to their project (React, Next.js, Vue, Svelte, Astro, Tailwind…), build it in that stack instead: style tokens as CSS custom properties in the global stylesheet (or the Tailwind theme when Tailwind is present), one component per section, same structure and design rules.
   - Single-section requests: output that section alone inside a minimal HTML shell (fonts, tokens, base styles), with no nav or footer unless the user asks; measure the hero's top whitespace from the top of the page.
   - If the working directory is clearly a frontend project and the user didn't ask for integration, deliver the HTML file and offer the port in one line.
   - **Markup conventions** (they let the self-check verify structure; harmless in production):
     - `<html lang="en" data-page="pricing" data-archetype="A" data-style="business" data-theme="dark">`. For a single section, use `data-page="section"` and omit `data-archetype`.
     - Put `data-section="<name>"` on the nav, on every top-level section, and on the footer. Names: `nav`, `hero`, `page-header`, `logo-wall`, `problem`, `features`, `feature-showcase`, `how-it-works`, `use-cases`, `integrations`, `security`, `social-proof`, `stats`, `comparison`, `pricing`, `billing-toggle`, `enterprise`, `faq`, `cta`, `newsletter`, `story`, `team`, `values`, `timeline`, `careers`, `contact-form`, `contact-info`, `departments`, `featured`, `filter`, `articles`, `pagination`, `error`, `recovery`, `platforms`, `install`, `versions`, `footer`. Testimonials and customer quotes are `social-proof`; customer logos are `logo-wall`. A section mainly about security or compliance is `security`; one that explains the problem before the product is `problem`.
     - Put `data-logo-source` on every logo (see *Real logos only* in Design Rules).
     - Put `data-layout`, `data-bg`, and (for signature moves) `data-bold="true"` on every content section. Use only the tags in `shared/signature-moves.md` §2.2 and the roles in §2.3 — never a custom name (`grid-3col`, `split`, `default` fail the self-check).
     - Put `data-mock` on the outer frame of every synthetic product visual. Data inside a mock (rows, counts, timestamps) is illustrative UI, not a claim.

8. **Verify** — before showing anything to the user:
   - If `python3` is available, run `python3 <this skill's base directory>/scripts/check_page.py <file> --style <style>` as a single command — absolute path, no `cd` first, so it matches the pre-approved `python3` permission. Fix every ERROR. Fix each WARN too unless it is deliberate (a brand override, colors inside a synthetic product mock) — then say why in the QA report.
   - Run the page skill's Step 6 checks. With project-stack output, run the checks that apply by reading the code.
   - **Copy check**: run the self-check list at the end of `shared/copy.md` (sentence case, concrete nouns, no banned phrases, at most one AI word per headline).
   - **Claims check**: list every factual claim on the page — numbers, customers, certifications, integrations, awards, speed/ease/result promises. For each, point to where the user said it. Any claim without a source must be inside a `data-sample` element; otherwise tag it or remove it.

9. **Deliver**: open the HTML file in the browser when running locally (`open <file>` on macOS, `xdg-open` on Linux, `start "" <file>` on Windows). Then give:
   - the file name, and a 2–3 sentence note on the key design decisions (archetype, what was skipped and why);
   - a short **QA report**:
     ```
     QA
     - Self-check: 21 passed · 0 errors · 1 warning (product mock uses 3 colors outside the style file — intentional)
     - Claims check: 9 claims · 6 from your brief · 3 tagged as sample
     - Sample content to replace or remove: testimonials (3, fictional), logo wall (5 fictional wordmarks), "SOC 2" card
     - Placeholders to replace: [Company], plan descriptions
     - Left out: Stats (you said there are no real numbers yet)
     - Values with no style role: price 48px (kept from the page skill)
     ```
     If Python isn't available, write "Self-check: not run (no Python 3); page skill checklist reviewed".
   - on the fast route, the brief offer from Step 1.

---

## Style precedence

Page and section skills were written against Minimal. Their inline token blocks, Step 6 checks, and `references/anti-patterns.md` files contain Minimal values (2px buttons, zero shadow, 180px section rhythm, DM Sans 500 headings, "no pill buttons"). When Business, Colorful, or Editorial is active:

1. **Visual values come from the active style file** — fonts (including its Google Fonts `<link>`), weights, colors, radius, shadow, spacing rhythm, transition timings (§6), and button / input / nav / card styling. Map each Minimal value to the role with the same name in the active style file (§2 type scale, §3 spacing, §4 radius, §5 shadow, §6 transitions, §8 components). Example: a page skill's "feature card 8px radius" becomes Business "Feature card: 16px". References to `visual-style.md` §10 (brand customization) mean the active style file's Brand Customization section.
   - **Page frame**: the grid max-width and side padding (§7) and the nav height `--nav-h` (§8) come from the style file. A page skill's "1080px container" means "the style's main grid". Narrower measures a page skill sets inside that frame (a 720px reading column, a 540px subtitle) stay.
   - **Page headers** on pages other than Landing (pricing, blog, contact, about, downloads headers) use the style's hero top whitespace and its "Cross-page hero" size when the style defines one (Editorial does); otherwise its section heading size, unless the page skill explicitly asks for hero scale.
   - **Section padding** in every style file is the top and bottom padding of each section, as in Minimal; the visual gap between two sections is twice that value.
   - **Borrowed Minimal values**: when a page skill reuses a named Minimal token for another gap (58px = heading to content, 128px = hero top / footer top, 180px = section padding, 32px = card padding), map it to the same role in the active style (e.g., a 58px CTA-to-visual gap becomes Business 48px).
   - **Buttons**: Minimal's `.btn-lg` (16px · `12px 24px`) exists because Minimal's default button is 14px. Business, Colorful, and Editorial default buttons are already 16px — use their default button where a page skill asks for `.btn-lg`.
   - **Product visual frame**: the Synthetic Product Visual's outer frame takes the style's content-card role (Business content card 24px, Colorful scene frame 24px, Editorial product stage 22px). Business's 48px "product stage panel" is for large nested containers, not screenshot frames.
   - **Dark bands**: `.section-dark` / a `var(--text)` background is a Minimal technique. In other styles, use the style file's own section-background rules (Business "Section Backgrounds", Colorful "Scene Section", Editorial "Section Background Switching"). On a dark-theme page, never flip a footer or CTA into a `var(--text)` band — that color is light there.
2. **Structure comes from the page skill** — archetype, section list and order, content rules, layout (column counts, component anatomy), interactions, and page-specific measurements with no role in the style file (e.g., the Downloads 64px app icon). The Synthetic Product Visual recipe in `shared/visual-style.md` §8 is structure too: use its frame / chrome bar / panel layout in any style, with the active style's surfaces, radius, and shadow.
3. **Minimal-only rules are replaced, not combined.** Zero-shadow, no-pill-button, 2px-button, sans-only-heading, 180px-rhythm, and achromatic-color rules (in page skills, checklists, and anti-patterns files) give way to the active style file's own rules. So do generic palette bans (e.g., "no cream + terracotta") when the active style defines that palette on purpose. Content and structure rules — no fabricated evidence, section order, nav present — apply in every style.
4. **No matching role?** Keep the page skill's value and mention it in the delivery note. Don't invent a new value.

Lookup aid — the style file is authoritative:

| Role (style file §) | Minimal | Business | Colorful | Editorial |
|---|---|---|---|---|
| Display font (§2) | `'DM Sans'`, weight 500 | `'Plus Jakarta Sans'`, hero/section weight 600 | `'Playfair Display'` serif, weight 400 | `'Cormorant Garamond'` serif, hero 400 / section 500 |
| Accent / CTA (§1, light) | `#141414` (= `--text`) | `#071A31` | `#030302` | `#20808D` teal, hardcoded |
| Section padding, per side (§3) | 180px | 120px | 120px | 96px–120px (default 96px) |
| Heading to content (§3) | 58px | 48px | 48px | 48px |
| Hero top (§3) | 128px | 120px | 120px | 128px |
| Main grid (§7) | 1080px · side 32px | 1200px · side 32px | 920px · side 32px | 1440px · side 64px |
| Nav height `--nav-h` (§8) | 68px | 72px | 94px (floating pill) | 64px |
| Button (§8) | 2px radius · 14px · `8px 16px` | 8px radius · 16px · `12px 24px` | 9999px pill · 16px · `14px 28px` | 9999px pill · 16px · `10px 22px` |
| Cards (§4) | feature 8px · content 16px | feature 16px · content 24px | inner panel 16px · scene frame 24px | panel 16px · product stage 22px |
| Shadow (§5) | zero everywhere | soft blue-gray on cards (light); inset 1px ring (dark) | four-layer paper shadow on cards | layered on interactive/floating surfaces; static cards none |

---

## Design Rules

These override any competing instruction in referenced files, in every style:

- **No left-border accents on cards.** Never use `border-left` as a status or category indicator — it reads as AI-generated. Use opacity or background color.
- **Sample content fills gaps; the QA report names it.** Material the user didn't give is never passed off silently. That covers testimonials, customer names and logos, user counts, revenue, metrics, certifications (SOC 2, HIPAA, ISO), security specifics (TLS 1.3, AES-256, SSO, SCIM), awards, integration names and counts, trial lengths and plan terms, deployment options, data-center regions, and claims about speed, ease, or results ("set up in minutes", "no learning curve", "2× faster"). When such material is missing:
  - If the user said they don't have it, leave the section out.
  - Otherwise, fill the section with **sample content** so the page is not empty: realistic in shape, obviously fictional in substance. Use fictional companies (Northwind, Contoso, Fabrikam, Globex, Initech) and people, round illustrative numbers, and wordmarks — never real customer logos.
  - Sample content must look finished — same polish as real content, no visible "sample" labels, no grey boxes or `[brackets]` where real-looking content fits. Completeness and visual quality of the first draft come first; the user edits the content afterwards.
  - Put an invisible `data-sample` attribute on every sample section or element (including product claims inside otherwise real sections, e.g. a "SOC 2 certified" card or a "100+ connectors" line).
  - List every sample item in the QA report so the user knows exactly what to replace or remove.
- **Tokens are quoted, not authored.** Spacing, type scale, colors, and radii come from the active style file. If a value is missing, flag it — don't invent one.
- **Fixed nav requires backdrop blur.** `backdrop-filter: blur(12px)` on every fixed nav.
- **Directional padding only.** Use `padding-top` (not the `padding` shorthand) when overriding one direction on an element that inherits `.container`'s horizontal padding.
- **Respect `prefers-reduced-motion`.** All CSS animation inside `@media (prefers-reduced-motion: no-preference) { ... }`.
- **Real logos only — never draw one.** This covers every third-party mark: integration logos, customer logo walls, platform icons, social icons. Take each logo from the first source that has it:
  1. If an icon MCP is connected (e.g. better-icons), fetch the SVG from the Iconify `logos` collection (full color) or `simple-icons` (monochrome) and inline it.
  2. Otherwise use an image URL: `https://api.iconify.design/logos/<name>.svg` (full color, e.g. `logos/slack-icon`, `logos/notion-icon`) or `https://cdn.simpleicons.org/<slug>` (brand color; append `/<hex>` for one color, e.g. a grayscale logo wall). If you can run commands, confirm each URL returns 200 first. Give every logo `<img>` a wordmark fallback: `onerror="this.replaceWith(Object.assign(document.createElement('span'),{textContent:this.alt,className:'logo-wordmark'}))"`.
  3. If neither library has the brand, set the brand name as a text wordmark in the display font.
  Mark every logo element with `data-logo-source`: `iconify:<collection>:<name>`, `simple-icons:<slug>`, `user` (a file the user supplied), or `wordmark`.

---

## Appendix — File Routing

### Style files

| Style | Path |
|-------|------|
| Minimal (default) | `shared/visual-style.md` |
| Business | `shared/visual-style-business.md` |
| Colorful | `shared/visual-style-colorful.md` |
| Editorial | `shared/visual-style-editorial.md` |

### Page skills

| Page | Path |
|------|------|
| Landing | `pages/landing-page/SKILL.md` |
| Pricing | `pages/pricing-page/SKILL.md` |
| Contact | `pages/contact-page/SKILL.md` |
| About | `pages/about-page/SKILL.md` |
| Product | `pages/product-page/SKILL.md` |
| Blog | `pages/blog-page/SKILL.md` |
| 404 | `pages/404-page/SKILL.md` |
| Downloads | `pages/downloads-page/SKILL.md` |

### Section skills

Use when the user asks for a single section rather than a full page.

| Section | Path |
|---------|------|
| Hero | `sections/hero/SKILL.md` |
| Features | `sections/features/SKILL.md` |
| Social Proof | `sections/social-proof/SKILL.md` |
| CTA | `sections/cta/SKILL.md` |
| FAQ | `sections/faq/SKILL.md` |
| How It Works | `sections/how-it-works/SKILL.md` |
| Comparison Table | `sections/comparison-table/SKILL.md` |
| Contact Form | `sections/contact-form/SKILL.md` |
| Navigation | `sections/navigation/SKILL.md` |
| Footer | `sections/footer/SKILL.md` |

### Shared

| File | Use |
|------|-----|
| `shared/interaction-patterns.md` | Motion tokens and animation recipes (read selectively, Step 4.4) |
| `shared/signature-moves.md` | Signature moves catalog and section-rhythm rules (Step 4.3) |
| `shared/product-visuals.md` | Recipes for synthetic product visuals, mock status colors, realism checklist (Step 4.3) |
| `shared/copy.md` | Headline formulas, measured targets, phrase rules (Step 4.3) |
| `shared/atmosphere.md` | Backgrounds and texture: mesh gradient, sky with grain, halftone dots (CSS default, optional Paper Shaders), paper collage, floating app icons (used by the styles' Hero showcases) |
| `shared/navigation.md` | Navigation component knowledge |
| `shared/footer.md` | Footer component knowledge |
| `shared/quality-checklist.md` | Verification checklist (visual items assume Minimal — see Style precedence) |
