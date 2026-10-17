[English](README.md) | [中文](README.zh-CN.md)

# Proof

![Proof — a product design skill](docs/images/cover.png)

### A product design skill

[![Website](https://img.shields.io/badge/Website-proofdesign.pages.dev-1F5EFF?style=flat-square)](https://proofdesign.pages.dev)
[![Made for Claude Code](https://img.shields.io/badge/Made%20for-Claude%20Code-blueviolet?style=flat-square&logo=anthropic)](https://docs.anthropic.com/en/docs/claude-code)
[![Made for Codex](https://img.shields.io/badge/Made%20for-Codex-000000?style=flat-square&logo=openai)](https://openai.com/index/introducing-codex/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![8 Page Types](https://img.shields.io/badge/8-Page%20Types-141414?style=flat-square)](#page-types)
[![10 Sections](https://img.shields.io/badge/10-Sections-5DDFD7?style=flat-square)](#sections)
[![4 Styles](https://img.shields.io/badge/4-Styles-CF9FFC?style=flat-square)](#styles)
[![400+ Real Product Pages](https://img.shields.io/badge/400+-Real%20Product%20Pages-E9E9E9?style=flat-square)](#how-it-was-built)

**Product pages that look shipped, not generated — built from patterns in 400+ real product pages.**

Proof is a product design skill for Claude Code and Codex. Tell it which page you need. It builds a complete, responsive page with a real-looking product showcase, a distinct visual style, and motion that shows your product at work. The first draft looks like a shipped product, not an AI template.

**See it live → [proofdesign.pages.dev](https://proofdesign.pages.dev)** — the four styles, nine page configurations, and ten sections, each a real page the skill generated. Open any of them and scroll, hover, click.

```bash
/proof landing
```


---

## Why it is different

**1. Learned from real products, not from the model's taste.**
We studied 400+ pages of real, shipped products through the [Mobbin](https://mobbin.com) MCP. From them we wrote down what works: what goes in the hero, how real sites show their product, where proof goes, how layouts change from section to section, and how real headlines are written. Each pattern gives its reason and tells you when not to use it.

**2. Four styles with real character.**
Minimal, Business, Colorful, and Editorial are complete design systems, each extracted from a real product site. Each style has its own signature hero, its own textures and details, and its own motion. The same page in two styles is two different designs, not a recolor.

**3. A hero that stops the scroll.**
Every page leads with a product showcase built for its style: a mesh-gradient stage with feature tabs, a sky with halftone clouds and a paper product sheet, a newspaper-style dark front page, or a precise specimen grid. The product inside is full of real-looking content — names, statuses, numbers — never grey placeholder boxes.

**4. The whole site, section by section.**
8 page types and 10 sections cover what a product site needs. Ask for a full landing page or only a pricing table, an FAQ, or a footer.

**5. Your brand, your content.**
Give it your colors, fonts, audience, and real material — as much or as little as you have. The structure adapts to who your visitors are. Anything you do not give is filled with finished-looking sample content, so the first draft is complete, and the QA report lists every sample item to replace.

**6. Checked before you see it.**
Before delivery the skill checks its own page: layout rhythm, style fidelity, real logos, no invented facts presented as real. It then tells you what passed.

**What it avoids** — the usual signs of an AI-made page:

- the same centered template repeated down the page
- three identical feature cards
- grey placeholder boxes and drawn logos
- a two-color blue-to-purple gradient
- invented facts presented as real
- everything fading up on scroll

---

## Styles

*The same brief — "Relay, a shared inbox for support teams" — in each style (click an image to open the live page):*

| Minimal | Business |
| --- | --- |
| [![Minimal](docs/images/style-minimal.png)](https://proofdesign.pages.dev/style-minimal-relay) | [![Business](docs/images/style-business.png)](https://proofdesign.pages.dev/style-business-relay) |
| **Colorful** | **Editorial** |
| [![Colorful](docs/images/style-colorful.png)](https://proofdesign.pages.dev/style-colorful-relay) | [![Editorial](docs/images/style-editorial.png)](https://proofdesign.pages.dev/style-editorial-relay) |

| Style | Character | Signature hero |
| --- | --- | --- |
| **Minimal** (default) | Black, white, and gray; no shadows; sharp edges; much space | A hairline-grid "specimen field" with a focal product view and scattered real-content cards |
| **Business** | Warm and trustworthy; soft shadows; rounded corners | A rounded product stage in a multi-hue mesh gradient, with feature tabs that turn it into a product tour; gradient mats under every product visual below |
| **Colorful** | Playful and crafted; serif headlines; paper-like cards | A sky with grain and halftone clouds; a paper product sheet rises from its edge; warm pastel scenes below |
| **Editorial** | Authored and calm; large serif; one teal accent | A dark "front page": serif masthead, hairline rule, and a paper product window with a margin column of evidence |

Each style has a light theme and a dark theme and works with every page type. Each was extracted from a real product site with [Taste Lab](https://github.com/senlindesign/taste-skill), a skill that measures a site's style into exact values (colors, type scale, spacing, radius, shadow) and the design principles behind them.

---

## Why "Proof"

In printing, a *proof* is the first copy off the press: close enough to the final product to ship, and the moment for last adjustments. That is the goal here: a first draft good enough to ship, which you then adjust in minutes. A proof is also evidence, and every pattern in this skill comes from a real, shipped product page.

### Five layers of product design

Most design skills decide only how a page looks. Proof works through all five layers of product design, from Jesse James Garrett's *The Elements of User Experience*.

| Layer | What the skill decides |
| --- | --- |
| **Strategy** | Who the page is for, and what the page must get them to do |
| **Scope** | Which sections to include, and which sections to omit |
| **Structure** | The order of the sections, and how their layouts alternate |
| **Skeleton** | The layout in each section |
| **Surface** | The style, textures, and motion |

So one product can get two different pages:

- **Visitors are developers who want to try the product now.** You get a short page: hero, features, and sign-up.
- **Visitors are IT directors who do not know the category and worry about security.** The skill adds an explanation, a how-it-works section, and a security section. You said you have no testimonials, so the page shows none.

---

## Install

### Claude Code

1. Clone the repository:

   ```bash
   git clone https://github.com/senlindesign/proof.git
   ```

2. Copy the skill folder into your skills folder:

   ```bash
   cp -R proof/skills/proof ~/.claude/skills/
   ```

3. In any project, type `/proof`.

### Claude Code plugin

The plugin version updates with `/plugin update`.

1. Add the marketplace and install the plugin:

   ```bash
   /plugin marketplace add senlindesign/proof
   /plugin install proof@proof
   ```

2. Type `/proof:proof`. Claude Code puts the plugin name before each plugin skill.

### skills.sh

One command with the [skills](https://skills.sh) CLI; it asks which agent to install to.

```bash
npx skills add senlindesign/proof
```

Then type `/proof` in your agent.

### Codex

1. Clone the repository:

   ```bash
   git clone https://github.com/senlindesign/proof.git
   ```

2. Copy the skill folder into the Codex skills folder:

   ```bash
   cp -R proof/skills/proof ~/.codex/skills/
   ```

### Other agents

For Cursor, Windsurf, or another agent that reads files: tell the agent to read `skills/proof/SKILL.md`.

The skill needs no build step and no dependencies. If Python 3 is installed, the skill checks each page before it gives the page to you.

---

## Usage

| You want | Type |
| --- | --- |
| A landing page now | `/proof landing` |
| A page in a specific style and theme | `/proof pricing editorial dark` |
| One section only | `/proof hero colorful` |
| A page that fits your product | `/proof landing — Patchwork, a shared moodboard for design studios` |
| A page for your audience | Add four facts: who visits, what they must do, what worries them, and what real material you have. You can also paste a PRD or a brand guide. |
| Your brand | `/proof landing business — accent #E4572E, display font Manrope` |
| Full control | `/proof blog editorial dark — archetype B, no newsletter, as a Next.js page in this project` |
| Help to decide | Type only `/proof`. The skill asks one round of questions. Then it builds the page. |

The default output is one HTML file. Open it in a browser. If you ask, the skill writes code for your project's stack instead.

---

## What you can build

![8 page types × 10 sections × 4 styles](docs/images/overview.png)

### Page types

Each page type has 3 or 4 archetypes. An archetype is a layout for one kind of product or goal.

| Page type | Use it for | Archetypes |
| --- | --- | --- |
| **Landing** | Your product, for new visitors | SaaS Tool · SaaS Platform · Developer Tool · Creative Tool |
| **Pricing** | Plans and billing | Feature-Tiered · Usage-Based · Simple Binary · Enterprise-First |
| **Product** | Features in depth, for people who evaluate your product | Feature Showcase · Platform Overview · Product Deep-Dive |
| **About** | The story of your company and team | Company Story · Team-First · Mission-Driven |
| **Contact** | Questions, support, and demo requests | Simple Contact · Department Routing · Sales-Focused · Support Hub |
| **Blog** | A list of articles and changelogs | Grid Index · Editorial · Minimal List |
| **Downloads** | Desktop apps, CLIs, and SDKs | Platform Selector · Multi-Product · Developer Distribution |
| **404** | A way back for lost visitors | Minimal Redirect · Navigational Recovery · Brand Moment |

### Sections

`hero` · `features` · `social-proof` · `cta` · `faq` · `how-it-works` · `comparison-table` · `contact-form` · `navigation` · `footer`

### Built into every page

- **Real product showcases**: 8 recipes (layered cards, a product rising from the fold, a bento of UI tiles, a code window, an AI chat, and more), filled with real-looking content.
- **Signature moves**: 17 bold layouts seen on real sites, such as edge-to-edge headlines, a bento with a lead tile, step tiles with product, and a quote wall. Each page uses one or two.
- **Atmosphere**: mesh gradients, grain, halftone dots, and paper collage, from the style's own palette.
- **Motion that shows the product**: rows stream in, a cursor clicks, a reply types itself, a chart draws — all respect "reduce motion".
- **Real logos only**: integration, customer, and platform logos come from icon libraries, never drawn by the AI.
- **Real copy patterns**: headlines follow formulas measured on 72 real headlines — short, specific, sentence case.

---

## How it was built

- **Research on real products.** Through the [Mobbin](https://mobbin.com) MCP we wrote 410 detailed records of real product pages (28 to 63 per page type), then 55 product showcases, 32 signature moves, and 72 headlines.
- **Patterns with reasons.** Each pattern tells when it applies, how to build it, and when to skip it. A common pattern is not always a correct pattern.
- **A second agent checked the work.** A separate agent compared each knowledge file with the research records and fixed the contradictions it found before they got into the skill.
- **Styles from real sites.** [Taste Lab](https://github.com/senlindesign/taste-skill) measured each style on a real product site. The values came first; the principles explain the values.
- **A golden test set.** 19 fixed requests together cover all 8 page types, all 4 styles, and both themes. A script checks each result, including a 390px narrow-screen pass, a second model audits every page for invented claims, and a screenshot judge scores how real each page looks. See [`evals/`](evals/).
- **Blind tests.** New versions of the skill are compared with old ones in blind A/B tests, judged on realism, product showcase, layout variety, and copy.

---

## Repository layout

```txt
skills/proof/              the skill — install this folder
├── SKILL.md               entry point
├── pages/                 8 page types, each with its knowledge files
├── sections/              10 sections
├── scripts/               the page self-check
└── shared/                4 styles, product showcases, signature moves, atmosphere, copy, motion

evals/                     golden test set, page checker, claims audit, screenshot judge, blind test
```

## License

[MIT](LICENSE)
