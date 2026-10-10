# Integrations / Ecosystem Section Patterns — Product Page

> Source: 8 integration section observations across Product pages (Threads, Slack, Notion x2, Miro, Harvest, 7shifts, Shopify). All tokens validated against `shared/visual-style.md`.

---

## Two Audiences, One Section

Integration sections serve two distinct audiences (observed across all 8 samples):

| Audience | What they ask | Served by |
|----------|--------------|-----------|
| **End users** | "Does it work with my tools?" | Logo grids, "works with" framing, tool names |
| **Developers / Partners** | "Can I build on it?" | API section, "Build your own" CTA, documentation links |

The best-observed sections (Miro, Harvest) explicitly address **both** audiences in the same section: featured integrations above, API/developer CTA below. Sections that only show a logo wall (7shifts) or only narrate the ecosystem (Slack) serve one audience at the expense of the other.

**Default recommendation**: Use Pattern 1 (Featured Grid) for most products. Add an API sub-section (see "API / Build Your Own" below) only for Archetype B (Platform Overview) or products with a public API.

---

## Pattern 1: Featured Integration Grid (3/8 — default)

**When to use**:
- Product has 6-12 notable integrations to highlight
- Each integration benefits from a brief description (not just a logo)
- Standard product page that needs to communicate ecosystem breadth
- All three archetypes

**Execution**:
- 3-col grid of integration cards
- Each card: logo + name + description
- Section heading centered above
- Optional "View all integrations" link below the grid

```css
.integrations-section {
    padding: 180px 0;                   /* section rhythm */
}

.integrations-header {
    text-align: center;
    margin-bottom: 58px;               /* heading to content */
}

.integrations-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px); /* section heading scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

.integrations-subtitle {
    font-family: var(--font-body);
    font-size: 18px;                    /* body text scale */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;                   /* subtitle max-width */
    margin: 24px auto 0;
}

.integrations-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;                          /* list card gap */
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;                    /* grid side padding */
}

@media (max-width: 767px) {
    .integrations-section {
        padding: 96px 0;               /* narrow: 180px -> 96px */
    }

    .integrations-header {
        margin-bottom: 40px;           /* narrow: 58px -> 40px */
    }

    .integrations-grid {
        grid-template-columns: 1fr;
        padding: 0 20px;               /* narrow: 32px -> 20px */
    }
}
```

**Integration card tokens**:
```css
.integration-card {
    background: var(--surface-1);
    border-radius: 8px;                /* feature card radius */
    padding: 32px;                     /* card internal padding */
    /* zero shadow */
}

/* Logo source: see "Real logos only" in the master SKILL.md — Iconify `logos` (full color) first,
   then Simple Icons, then a text wordmark. Never draw a logo. */
.integration-card-logo {
    height: 32px;
    width: auto;                       /* natural aspect ratio */
    margin-bottom: 16px;
    /* Logo is displayed in its natural colors, not grayscale.
       Grayscale is only for social-proof logo walls. */
}

.integration-card-name {
    font-family: var(--font-display);
    font-size: 16px;                    /* body secondary scale */
    font-weight: 500;
    color: var(--text);
    margin-bottom: 6px;
}

.integration-card-author {
    font-family: var(--font-mono);
    font-size: 12px;                    /* label scale */
    font-weight: 400;
    letter-spacing: 0.72px;
    color: var(--text);
    opacity: 0.4;                       /* label opacity */
    margin-bottom: 8px;
}

.integration-card-description {
    font-family: var(--font-body);
    font-size: 16px;                    /* body secondary scale */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                       /* description opacity */
}
```

**"View all" link tokens**:
```css
.integrations-view-all {
    text-align: center;
    margin-top: 32px;
}

.integrations-view-all a {
    font-family: var(--font-display);
    font-size: 14px;                    /* button/nav scale */
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
}
.integrations-view-all a::after { content: ' \2192'; }
.integrations-view-all a:hover { opacity: 0.7; }
```

**Section heading copy patterns**:
- "Integrations" (neutral, default)
- "Works with [count]+ tools" (breadth-first, e.g., "Works with 100+ tools")
- "[Product] works with the tools you already love" (user-empathy framing)

**Variants**:
- **6-9 cards** (Threads, Notion directory): Use 3-col grid with 2-3 rows. Add a "View [N] more" expand button below the grid if the full list exceeds 9
- **3 featured cards only** (Miro, Harvest): Extreme restraint. Only show the top 3 integrations. Links to a full directory page. Use when a comprehensive integration page exists elsewhere
- **Categorized grid** (Notion): Two groups — "By [Product]" (first-party) and "By our partners" (third-party) — each with its own 3-col grid. Use when the distinction between first-party and third-party integrations matters

**When not to use**:
- Fewer than 3 integrations (mention them in the features section instead)
- Integrations are only logo-deep with no meaningful description (use Pattern 2 logo wall instead)

**Evidence**: Threads (9 cards, dark, gradient border), Notion (13 cards, categorized), Miro (3 cards + API)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Logo Wall (2/8)

**When to use**:
- 12+ integrations to display, each needing only logo recognition (not description)
- The goal is "ecosystem breadth" signaling, not explaining what each integration does
- Supplements a Featured Grid above — showing the long tail after the highlights

**Execution**:
- Flex-wrap grid of integration logos
- Logos displayed at consistent height, natural aspect ratio
- Full-color logos (not grayscale — grayscale is reserved for social-proof "trusted by" walls)
- Optional: category filter tags above the grid

```css
.integration-logo-wall {
    display: flex;
    flex-wrap: wrap;
    gap: 24px;                          /* list card gap */
    justify-content: center;
    align-items: center;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.integration-logo-wall img {
    height: 24px;                       /* smaller than featured card logos */
    width: auto;
    opacity: 0.5;                       /* not as faded as social-proof 0.15 */
    transition: opacity 0.3s linear;
}
.integration-logo-wall img:hover {
    opacity: 1;
}
```

**Distinction from social-proof logo walls**: Social-proof logos use opacity 0.15 and communicate "these companies trust us." Integration logos use higher opacity (0.5 hover to 1) and communicate "we connect with these tools." Do not combine them into one section.

**When not to use**:
- Fewer than 6 integrations (too sparse; use Pattern 1 card grid)
- Each integration needs a description (use Pattern 1)
- The product's integration story is about depth, not breadth (use Pattern 3)

**Evidence**: Notion ecosystem (18 logos, 3 rows), 7shifts (6 logos, category filters)
**Evidence status**: Cross-sample inference

---

## Pattern 3: Featured + API / "Build Your Own" (2/8)

**When to use**:
- Product has a public API and wants to attract developer/partner integrations
- Archetype B (Platform Overview) — the product positions itself as a platform
- Both end-user integrations and developer tools need representation

**Execution**:
- Two-part section: featured integration cards above, API/developer section below
- Separator between the two parts (visual gap or thin border)
- API section: heading + description + CTA button

```css
/* Featured integration cards use Pattern 1 tokens above */

.api-section {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;                          /* list card gap */
    max-width: 1080px;
    margin: 32px auto 0;
    padding: 32px;
    border-top: 1px solid var(--surface-2);
}

@media (max-width: 767px) {
    .api-section {
        grid-template-columns: 1fr;
        padding: 24px 20px;            /* narrow: 32px -> 24px, 32px -> 20px */
    }
}
```

**API sub-section tokens**:
```css
.api-block-heading {
    font-family: var(--font-display);
    font-size: 20px;                    /* card heading scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 8px;
}

.api-block-description {
    font-family: var(--font-body);
    font-size: 16px;                    /* body secondary */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    margin-bottom: 24px;
}

/* CTA uses .btn-dark (standard):
   padding: 8px 16px; font-size: 14px; border-radius: 2px */
```

**Two common sub-section framings** (observed):
1. **"Build your own"** (Harvest): heading "Build your own [Product] integration" + description about API capabilities + CTA "Browse options" or "Get started with API"
2. **"Request + Build"** (Miro): Two side-by-side blocks — "Looking for something else?" (submit a request for end users) + "Want to build your own?" (API docs for developers)

**When not to use**:
- Product does not have a public API
- The product is not positioned as a platform (Archetype A Feature Showcase rarely needs this)
- A dedicated API/developer page already exists and is linked from the navigation

**Evidence**: Miro (3 featured + dual API CTA), Harvest (3 featured + "Build your own" puzzle icon)
**Evidence status**: Cross-sample inference

---

## Integration Count Guidelines

| Integration count available | Recommended approach |
|----------------------------|---------------------|
| 0-2 | No dedicated section. Mention integrations in the features section |
| 3-6 | Pattern 1 (Featured Grid) — show all as cards |
| 7-12 | Pattern 1 (Featured Grid) — show 6, "View all" link for the rest |
| 13+ | Pattern 1 (3-6 featured) + Pattern 2 (logo wall for the rest) |
| Any + public API | Add Pattern 3 (API sub-section) below the featured grid |

---

## Content Fabrication Warning

Do NOT invent integration names or logos. If the user does not specify which integrations to feature:
- Use placeholder cards with "[Integration 1]", "[Integration 2]", "[Integration 3]"
- Or omit the section entirely and note it in the output as "Integration section omitted — no integration data provided"

A section with fabricated integration logos is worse than no section at all — it creates false expectations about product capabilities.
