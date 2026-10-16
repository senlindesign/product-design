# Section Composition Rules — 404 Page

> Source: Mobbin research synthesis from 45 unique products (32 well-known, 13 studio/niche)

---

## 1. Page Structure: Single Content Block, Not a Section Stack

A 404 page is fundamentally different from Landing, Pricing, and Contact pages. It is **a single content block** on a viewport-filling canvas, not a vertical stack of sections separated by 180px rhythm.

- No "section rhythm" of 180px applies. The 404 page has at most 1-2 content areas (error block + optional destination list), not 4-8 sections
- The content block is a compact cluster of elements (label, heading, body, button) with tight internal spacing
- Evidence: 30/45 samples present all content within a single visual group. Only Archetype B with many destination cards extends beyond one screen

---

## 2. Viewport-Fill Layout

For Archetypes A and C (single content block), the content should be vertically centered in the available viewport space.

```css
.error-page {
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 32px;   /* matches system .container side padding */
}
```

- Evidence: 15/25 samples where vertical position is explicit are vertically centered
- `var(--nav-h)` is `68px` (from `shared/visual-style.md` navigation token: `16px padding x 2 + 36px button = 68px`)
- When nav uses `position: fixed`, the body already has `padding-top: var(--nav-h)` — the `min-height` calculation accounts for this

**Exception — Archetype B with many links**: When the destination list or card grid pushes content beyond one viewport, do not force viewport-fill. Use natural document flow with standard top padding instead. The content block starts at the top offset and the page scrolls.

---

## 3. Navigation

**Keep the site's standard navigation.** The nav is the user's primary escape route from a 404 page.

- Evidence: 13/17 samples where nav is observable use the full site nav. 3/17 use logo-only (Notion, Mixpanel, Jitter). Only 0/17 remove nav entirely
- Reuse `shared/navigation.md` and `sections/navigation/SKILL.md` without modification
- No "active" link highlight in the nav — the 404 page is not a regular navigation destination
- The nav CTA button (e.g., "Get started") remains present — it provides a productive exit

---

## 4. Footer

**Optional.** For viewport-fill layouts (A, C), the footer sits below the fold and is not visible on initial load. For Archetype B with scrollable content, the footer flows naturally after the last content block.

- Evidence: Footer is observable in only 5/45 samples (capture cropping); of those, 3 use full multi-column footer (Mercury, Craft, Figma) and 2 use a minimal single row (Notion, AI Report)
- Reuse `shared/footer.md` and `sections/footer/SKILL.md` without modification
- Decision: include the footer by default (it provides navigation links), but do not add vertical padding above it beyond the standard `128px` footer top padding from `shared/visual-style.md`

---

## 5. Content Width

| Archetype | Content max-width | Rationale |
|-----------|------------------|-----------|
| A (centered) | `540px` | System subtitle measure from `shared/visual-style.md` section 7. A's content (heading + 1-2 sentences + button) is equivalent to a subtitle block |
| C (centered, typographic) | `540px` for copy; the giant numeral/heading may exceed this | The giant element fills the viewport; the supporting copy stays within the reading measure |
| B (destination list/cards) | System `.container`: `max-width: 1080px; padding: 0 32px` | Cards and list rows need the full content width |
| Two-column split | System `.container` (1080px). Each column `flex: 1`. Gap: `58px` | Matches system heading-to-content gap from `shared/visual-style.md` section 3 |

---

## 6. Content Block Internal Spacing

The content block is a compact cluster. These are **internal element spacings**, not section rhythm:

```
Label/numeral --> heading:       16px
                                 (24px if the numeral is display-sized, >= 80px)
Heading --> body text:           16px
Body text --> action button(s):  32px
```

These values come from the system spacing scale (`6 / 8 / 12 / 16 / 24 / 32 / 58 / 128 / 180px` from `shared/visual-style.md` section 3). The content block as a whole is vertically centered; these spacings control the rhythm within it.

**Evidence for the 32px body-to-action gap**: Hero subheading-to-CTA is `48px` in the system, but the 404 content block is smaller than a Hero — the body text is 1-2 sentences, not a full subtitle. 32px provides separation without making the block feel disjointed. Observed: Unify, SIGMA, and Resend all use gaps in the 24-32px range between body and button.

---

## 7. Two-Column Split Layout

For products that combine error messaging with a visual or destination list (Mercury, SpaceXAI, Deezer, KOPPEN pattern):

```css
.error-page-split {
    min-height: calc(100vh - var(--nav-h));
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 58px;                            /* system heading-to-content distance from §3 */
    padding: 0 32px;
    max-width: 1080px;
    margin: 0 auto;
}
.error-page-split > .error-text {
    flex: 1;
}
.error-page-split > .error-visual {
    flex: 1;
}
```

- Gap between columns: `58px` (system heading-to-content distance from `shared/visual-style.md` section 3)
- Text column: heading + body + button, aligned left
- Visual/links column: display numeral, destination list, or brand visual
- Evidence: 5/45 samples use a two-column split (Mercury, KOPPEN, SpaceXAI, Deezer, AI Report)
- On narrow screens (< 768px): stack vertically. Text above, visual/links below

---

## 8. Background Color Rules

```
Navigation:       var(--bg)          transparent / page background
Error content:    var(--bg)          the viewport-filling area
Footer:           var(--bg) or var(--surface-1)   follows footer default
```

**The entire 404 page uses a single background color**: `var(--bg)`.

- No section background switching. A 404 page does not have alternating `var(--bg)` / `var(--surface-1)` sections
- Destination cards in Archetype B use `var(--surface-1)` background (consistent with the system card token: `background: var(--surface-1); border-radius: 8px; padding: 32px`)
- No colored backgrounds, no gradients, no brand-color fills. Evidence: Monte's full brand-color background is a counterexample explicitly outside our system
- Dark theme: `var(--bg)` = `#0A0A0A`. All other tokens follow the dark theme values in `shared/visual-style.md`

---

## 9. Decision Guide: Content Elements to Include / Exclude

### Always Include

| Element | Reason |
|---------|--------|
| Navigation | User's primary escape route (13/17 observable keep it) |
| Heading or numeral | The page must communicate "this page does not exist" — at minimum through a heading |
| At least one recovery action | A page with no way out is a dead end. 41/45 samples have at least one link or button |

### Include by Archetype

| Element | Condition |
|---------|-----------|
| Display numeral ("404") | A or C, when the numeral contributes to the visual composition. Not required — 15/45 show no numeral |
| Small label ("404" / "ERROR 404") | A, when using a literal heading that does not itself contain the code. Style: system `.label` (12px, mono, uppercase, +0.72px tracking, opacity 0.4) |
| Body text (1-2 sentences) | A or B. Explains the cause or bridges to destinations. Optional for C (the visual speaks) |
| Destination list/cards | B only. 2-8 destinations. Format chosen by content (see archetypes.md) |
| Search input | B only, and only when the product has a searchable content library. Rare: 3/45 |
| Giant numeral or heading | C only. The type IS the visual |
| Footer | Default yes. Can be omitted for ultra-minimal A (Notion, Linear pattern) |

### Never Include on a 404 Page

| Element | Reason |
|---------|--------|
| Multiple stacked sections (Features, Social Proof, CTA, FAQ) | A 404 is not a landing page. It has one job: acknowledge the error and offer recovery |
| Newsletter signup form | Out of context. The user arrived by mistake; do not capture leads on an error page |
| Product pricing or feature comparison | Wrong page for conversion content |
| Testimonials or social proof | The 404 page has no trust-building role |
| Status page or uptime indicators | A 404 (page not found) is not a service outage. Do not conflate them |

---

## 10. Minimum Page vs. Full Page

### Minimum (Archetype A)

```
Navigation --> Error Content Block (heading + body + button, centered) --> [Footer optional]
```

One content area. Fills the viewport. Evidence: Notion, Linear, Unify, Jitter.

### Standard (Archetype A with numeral)

```
Navigation --> Error Content Block (label/numeral + heading + body + button, centered) --> Footer
```

One content area with a visual element (numeral). Fills the viewport. Evidence: SpaceXAI, Public, Butter, Slash, Resend.

### Extended (Archetype B)

```
Navigation --> Error Content Block (heading + body + button) + Destination List/Cards --> Footer
```

Two content areas. May scroll. Evidence: Aave, Ada, SpaceXAI, Firecrawl, Tines.

### Expressive (Archetype C)

```
Navigation --> Giant Visual/Type + Minimal Copy + Button --> [Footer optional]
```

One content area dominated by a visual element. Fills the viewport. Evidence: Vucko, Figma, Instrument, Flighty.

---

## 11. Shared Components

| Component | Source | Notes |
|-----------|--------|-------|
| Navigation | `shared/navigation.md` | Fully reused; no "active" link |
| Footer | `shared/footer.md` | Fully reused |
| Button styles | `shared/visual-style.md` section 8 | `.btn-dark` for primary CTA; `.btn-outline` if a secondary action exists |
| Label styles | `shared/visual-style.md` section 8 | `.label` for "404" / "ERROR 404" small labels |
| Card styles | `shared/visual-style.md` section 8 | `.card` for Archetype B destination cards |
| Focus states | `shared/visual-style.md` section 8 | `:focus-visible` outline style |
