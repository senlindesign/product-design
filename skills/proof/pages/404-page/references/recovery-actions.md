# Recovery Actions — 404 Page

> Source: 45 unique products (32 well-known, 13 studio/niche). Covers buttons, text links, search, suggested destinations, and destination formats.

---

## 1. Action Format Overview

| Format | Count | When to use |
|--------|-------|-------------|
| Button(s) | 25/45 | Default for Archetype A and C. Clear, prominent recovery path |
| Text link(s) only | 16/45 | When the action is embedded in a sentence, or when buttons feel heavy for minimal pages |
| None in content block | 4/45 | Ultra-minimal pattern (Notion, Biograph, Figma, Linear) — relies on navigation for recovery |

**Default**: One `.btn-dark` button. Evidence: 23/25 pages with buttons use exactly one. Two buttons appear in only 2/25 (Mercury, Greptile).

**Evidence status**: Observed.

---

## 2. Primary CTA Button

Use the system `.btn-dark` token verbatim from `shared/visual-style.md` §8:

```css
.btn-dark {
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 500;
    font-family: var(--font-display);
    line-height: 20px;
    background: var(--accent);
    color: var(--accent-text);
    border: none;
    border-radius: 2px;
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}
.btn-dark:hover { transform: translateY(-1px); }
```

**Button copy** — choose based on the product's audience:

| Copy | When to use | Evidence |
|------|-------------|----------|
| "Go home" / "Go Home" | Generic default | Instrument, Deezer, Tines, Butter |
| "Back to home" / "Back to homepage" | Slightly warmer | SpaceXAI, Resend, Greptile |
| "Return home" / "Return to homepage" | Formal | Public |
| "Go to Homepage" | Explicit | Slash, SIGMA |
| Context-aware destination | When the audience likely has a specific intent | Vercel "Sign into Vercel", Mixpanel "Your Dashboard", KÖPPEN "Shop All" |

**Evidence**: 32/45 samples include a home link (71%). 9/45 substitute a context-aware destination instead of generic "Go home."

**Evidence status**: Observed.

---

## 3. Secondary Action (Two-Button Pattern)

Rare — only 2/25 pages with buttons use two buttons. When needed:

```css
/* Primary */
.btn-dark { /* system token, as above */ }

/* Secondary */
.btn-outline {
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 500;
    font-family: var(--font-display);
    line-height: 20px;
    background: transparent;
    color: var(--text);
    border: 1px solid var(--surface-2);
    border-radius: 2px;
    cursor: pointer;
    transition: border-color 0.3s linear;
}
.btn-outline:hover { border-color: var(--text); }
```

**Button group layout**: horizontal, gap `16px` (from spacing scale), centered or left-aligned matching the content block.

**Evidence**: Mercury: "Go Home" (primary) + "Visit Help Center" (secondary). Greptile: "See examples" (primary) + "Back to home" (secondary).

**When to apply**: Only when two genuinely different actions exist (home + help center, home + product showcase). Do not create a secondary button just to fill space.

**When NOT to apply**: A + C archetypes — one button is enough. B archetype already has a destination list; a second button competes with it.

**Evidence status**: Observed.

---

## 4. Text Link Alternative

**When to apply**: When the page is minimal and a button feels heavy. When the action is embedded in body copy as an inline link.

**Implementation**:

```css
.error-link {
    font-family: var(--font-display);
    font-size: 14px;                      /* matches nav link size from shared/visual-style.md §8 */
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    text-decoration: underline;
    transition: opacity 0.3s linear;
}
.error-link:hover { opacity: 1; }
```

**Inline link pattern**: The link is embedded in a sentence — "Expected to find something here? [Let us know.]()" (Craft) · "Head back to [Oura home]() for more content." (Oura).

**Standalone link pattern**: The link sits below the body text as a separate line — "Back to home page" (Jitter) · "Go back home" (Fauna).

**Trailing arrow**: Some links append `→` or `›`. Examples: "Back to home ›" (SpaceXAI), "Go to home →" (Parker), "Or see our site map ›" (Apple).

**Evidence**: 16/45 use text links only. Inline links appear in 8/16; standalone links in 8/16.

**Evidence status**: Observed.

---

## 5. "Report Broken Link" Action

**When to apply**: When the product wants users to report dead links. Always secondary to the primary recovery action.

**Implementation**: An inline text link in the body copy, not a button.

**Copy**: "Let us know" (Craft) · "drop us a line" (Stripe) · "Pop us a message" (GSAP).

**Evidence**: 3/45 — Craft, Stripe, GSAP. All use inline text links, not buttons.

**Evidence status**: Observed.

**When NOT to apply**: When there is no real destination for the report (no support email, no feedback form). Do not fabricate a contact target.

---

## 6. Search Input

**When to apply**: Archetype B only. The product has a searchable content library (docs, blog, help articles). Rare — only 3/45 use search.

**Implementation** — uses the system input token from `shared/visual-style.md` §4 and §8:

```css
.error-search {
    width: 100%;
    max-width: 500px;                     /* evidence: Apple ~500px */
    padding: 8px 16px;                    /* system input padding */
    font-family: var(--font-display);
    font-size: 16px;                      /* body-secondary size from type scale */
    font-weight: 400;
    color: var(--text);
    background: var(--bg);
    border: 1px solid var(--surface-2);
    border-radius: 4px;                   /* system input radius, NOT 160px pill */
    transition: border-color 0.3s linear;
}
.error-search:focus {
    border-color: var(--text);
    outline: none;
}
.error-search::placeholder {
    color: var(--text);
    opacity: 0.3;                         /* placeholder tier from contact-form knowledge */
}
```

**Placeholder copy**: Name the product's content types, not a generic "Search…":
- "Search apple.com" (Apple)
- "Search for an artist, album or track" (Deezer)
- "Search docs, blog, and help articles" (template)

**Shape**: All 3/3 observed search inputs on 404 pages are rectangular with 4–6px radius. 0/3 use a pill. The system's 160px pill search-bar radius is for nav search bars, not form inputs.

**Evidence**: Apple (~500px wide, rectangle ~4–6px, thin border), Deezer (dark filled, ~6px radius), Tines (full column width, ~6px radius, pre-filled with "404").

**Evidence status**: Observed.

**When NOT to apply**: When the product has no searchable content library. When the 404 audience is unlikely to search (e.g., consumer apps where users landed via a direct link). Adding search to a product with 5 pages is unhelpful.

---

## 7. Suggested Destinations

**When to apply**: Archetype B. The product has multiple important destinations and users may be looking for a specific subpage. 9/45 offer ≥ 2 suggested destinations.

### 7.1 List Rows (Recommended for the System)

The strongest B pattern for a minimal design system. Title + description + arrow, separated by 1px dividers.

```css
.destination-list {
    max-width: 540px;                     /* system subtitle measure from §7 */
    width: 100%;
}
.destination-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;                      /* from spacing scale */
    border-bottom: 1px solid var(--surface-2);  /* system divider */
    text-decoration: none;
    transition: opacity 0.3s linear;
}
.destination-row:first-child {
    border-top: 1px solid var(--surface-2);
}
.destination-row { opacity: 0.5; }
.destination-row:hover { opacity: 1; }        /* system direction: dim → bright on hover */

.destination-title {
    font-family: var(--font-display);
    font-size: 16px;                      /* body-secondary from type scale */
    font-weight: 500;
    color: var(--text);
}
.destination-desc {
    font-family: var(--font-body);
    font-size: 14px;                      /* button/nav size from type scale */
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    margin-top: 6px;                      /* smallest system spacing value */
}
.destination-arrow {
    color: var(--text);
    opacity: 0.4;
    font-size: 16px;
    flex-shrink: 0;
    margin-left: 24px;                    /* from spacing scale */
}
```

**Evidence**: SpaceXAI uses 6 list rows with title + description + arrow, separated by 1px dividers, under a "Helpful links" label.

**Recommended count**: 4–6 destinations. Fewer than 3 doesn't justify a list; more than 8 becomes a sitemap.

**Lead-in**: Use a label or sentence above the list: "Helpful links" (SpaceXAI style, system `.label`), or "You might be looking for:" (inline in body copy).

**Evidence status**: Observed (SpaceXAI pattern); cross-sample inference (token values derived from system tokens, not independently measured from SpaceXAI).

### 7.2 Destination Cards

```css
/* Uses system .card token from shared/visual-style.md §8 */
.destination-card {
    padding: 32px;                        /* system card padding */
    background: var(--surface-1);         /* system card background */
    border-radius: 8px;                   /* system feature card radius */
    text-decoration: none;
    display: block;
    transition: transform 0.2s ease-in-out;
}
.destination-card:hover { transform: translateY(-4px); }  /* system card hover lift from §6 */

/* Card grid */
.destination-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 24px;                            /* system card gap (list) */
    max-width: 1080px;                    /* system container */
    margin: 0 auto;
    padding: 0 32px;                      /* system container padding */
}
```

**When to apply**: 2–4 destinations where each has a title + 1–2 line description. Cards provide stronger visual separation than list rows.

**Evidence**: Aave (2–3 cards, title + description + ↗ arrow), V7 (3 cards with generative graphics), Ada (4 cards in 2×2 grid with photos).

**Evidence status**: Observed.

### 7.3 Inline Text Links

```css
.destination-inline {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    text-decoration: underline;
    transition: opacity 0.3s linear;
}
.destination-inline:hover { opacity: 1; }
```

**When to apply**: 3–5 destinations, minimal presentation. Links are comma- or dot-separated in a single line after a colon.

**Copy pattern**: "There is nothing at this URL. Try checking the address or go to: [Your Dashboard](), [Help Center](), [Community]()" (Mixpanel pattern).

**Evidence**: Orchid (4 underlined links: Home · Pricing · Use cases · Writing), Mixpanel (3 inline links after a colon).

**Evidence status**: Observed.

### 7.4 Bulleted Link List

A simple vertical list of text links. No descriptions, no cards.

```css
.destination-bullet-list {
    list-style: disc;
    padding-left: 20px;
}
.destination-bullet-list li {
    margin-bottom: 12px;                  /* system column link gap */
}
.destination-bullet-list a {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    text-decoration: underline;
    transition: opacity 0.3s linear;
}
.destination-bullet-list a:hover { opacity: 1; }
```

**When to apply**: 5–8 destinations where no descriptions are needed.

**Evidence**: Firecrawl (8 bulleted text links: Blog, Playground, Docs, Pricing, Use Cases, Changelog, GitHub, Glossary).

**Evidence status**: Observed.

---

## 8. Destination Types

Observed across 9 samples with ≥ 2 suggested destinations:

| Destination | Occurrences |
|-------------|-------------|
| Blog / News | 4 |
| Docs / Documentation | 3 |
| Help Center / Support | 3 |
| Homepage | 3 |
| Pricing | 2 |
| Community | 2 |
| Product / App | 2 |
| Case Studies | 2 |
| Careers | 1 |
| Contact | 1 |
| Changelog / GitHub | 2 |

**Selection guidance**: Choose 4–6 from the product's most important pages. Prioritize pages the user was most likely trying to reach. If the product has documentation, docs should be first — broken doc links are the most common cause of 404s on multi-product sites.

**Evidence status**: Observed.
