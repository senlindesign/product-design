# Error Display — 404 Page

> Source: 45 unique products (32 well-known, 13 studio/niche). Covers the "404" numeral, heading, body copy, and label — the core text content of a 404 page.

---

## 1. The "404" Numeral

The numeral is the most recognized signal that a page is a 404 error. It is visible in some form in **30/45** samples (67%). Showing it is optional — 15/45 rely entirely on heading copy.

### 1.1 Display Numeral (large, ≥ 100px)

**When to apply**: Archetype A when a visual anchor is wanted; Archetype C (Typographic) as the primary visual element.

**Implementation** (page-specific component token — not in the shared design system):

```css
.error-numeral {
    font-family: var(--font-display);     /* from shared/visual-style.md §2 */
    font-size: clamp(120px, 20vw, 200px); /* page-specific; evidence: median ~160px across 12 samples */
    font-weight: 500;                     /* from shared/visual-style.md §2: display weight */
    letter-spacing: -0.02em;              /* from shared/visual-style.md §2: tracking ≈ -2% of size */
    line-height: 1;                       /* tight — the numeral is a visual element, not reading text */
    color: var(--text);                   /* from shared/visual-style.md §1 */
}
```

**Variants**:

| Variant | Opacity | When to use | Evidence |
|---------|---------|-------------|----------|
| Full contrast | 1 | Numeral is the **sole** focal point (no text heading alongside) | Vucko, Butter, Slash, Fiasco — numeral replaces the heading |
| Low contrast | 0.10–0.15 | Numeral coexists with a text heading — demoted to texture | SpaceXAI (~0.11), Biograph (~0.10–0.15), Public |
| Watermark | 0.08 | Numeral sits **behind** content as a background layer | Parker (~0.06); footer giant-wordmark precedent 0.05–0.10 |

**Evidence**: 12/45 samples use a display numeral ≥ ~100px. Sizes at full viewport width: SpaceXAI ~160px, Public ~180px, Vucko ~120px (at 768px preview ≈ ~240px full), Figma ~200px, Butter ~300px, Fiasco ~450px tall, Zoox ~540px wide. The `clamp(120px, 20vw, 200px)` range covers the central cluster; Archetype C (Typographic) pages that want an extreme scale can override the upper bound.

**Evidence status**: Observed (sizes estimated from screenshots at known preview widths).

**When NOT to apply**: When the page relies on heading copy alone (Apple, Notion, Stripe pattern). When the product is consumer-facing and "404" would confuse non-technical users — use a text heading instead.

---

### 1.2 Mono Numeral

**When to apply**: Developer-oriented products. The "developer variant" of Archetype A (from the D reframing).

**Implementation**:

```css
.error-numeral-mono {
    font-family: var(--font-mono);        /* from shared/visual-style.md §2: DM Mono */
    font-size: clamp(120px, 20vw, 200px); /* same scale as display numeral */
    font-weight: 400;                     /* from shared/visual-style.md §2: mono weight */
    letter-spacing: 0.72px;               /* from shared/visual-style.md §2: mono tracking */
    line-height: 1;
    color: var(--text);
}
```

**Evidence**: 6/45 use a mono face for the code or label — Aqua (mono numeral), Figma (mono-style geometric face), Resend (monospace-like status line), Instrument (mono label), AI Report (mono label), Firecrawl (scrambled mono characters).

**Evidence status**: Observed.

---

### 1.3 Watermark Numeral

**When to apply**: Archetype A when a subtle background texture is wanted without a competing visual element.

**Implementation**:

```css
.error-content-block {
    position: relative;                   /* containing block for the watermark */
    overflow: hidden;                     /* REQUIRED: prevents the 500px numeral from creating
                                             horizontal scroll; the watermark is clipped to this box */
}

.error-numeral-watermark {
    font-family: var(--font-display);
    font-size: clamp(200px, 50vw, 500px); /* fills ~70% viewport width */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1;
    color: var(--text);
    opacity: 0.08;                        /* between footer wordmark 0.05–0.10 and logo-wall 0.15 */
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    pointer-events: none;
    user-select: none;
    z-index: 0;
    white-space: nowrap;                  /* prevent "404" from wrapping on narrow screens */
}
```

**Evidence**: 1/45 (Parker) uses a watermark numeral at ~0.06 opacity. The footer giant-wordmark precedent (`sections/footer/SKILL.md`) uses 0.05–0.10 opacity for a similar large background text element. The 0.08 value sits within this established range.

**Evidence status**: Observed (Parker); cross-sample inference (opacity value aligned with footer wordmark precedent).

---

### 1.4 Small Label

**When to apply**: Archetype A or B, as a secondary identifier above the heading. The label says "404" or "ERROR 404" while the heading carries the message.

**Implementation** — uses the system `.label` token verbatim from `shared/visual-style.md` §8:

```css
.error-label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 16px;   /* label → heading gap, from spacing scale */
}
```

**Copy variants**: `404` · `ERROR 404` · `404 ERROR` · `404 error` (lowercase). Mono label "ERROR CODE: 404" (Instrument).

**Evidence**: 8/45 use a small label — Mural, Orchid, Unify, Becane, KÖPPEN, Instrument, V7, Ada.

**Evidence status**: Observed.

---

## 2. Heading

A text heading exists in **34/45** samples (76%). The other 11 use the numeral or body text as the lead.

### 2.1 Heading Tone

| Tone | Count | Examples | When to use |
|------|-------|----------|-------------|
| Literal | 22/34 | "Page not found" · "This page couldn't be found" · "We can't find the page you're looking for" | Default for all archetypes |
| Apologetic | 6/34 | "Sorry, we can't find this page" · "Sorry, we couldn't find that page" | When the brand voice is warm/empathetic (Mercury, V7) |
| Humorous | 6/34 | "Oh no!" · "Oops… it did it again" · "This is awkward" | Only when the product domain provides a natural angle |

**Default**: Literal. Do not fabricate humor without a domain anchor (see anti-patterns.md §2.1).

**Evidence status**: Observed.

### 2.2 Heading Size

**Default**: use the system section heading scale from `shared/visual-style.md` §2:

```
Section heading:  clamp(32px, 4vw, 47px)    weight: 500   tracking: -0.02em   line-height: 1.1
```

**Oversized variant** (Archetype C, Typographic): when the heading IS the visual, scale up to hero or beyond:

```
Hero heading:     clamp(48px, 7vw, 80px)     weight: 500   tracking: -0.02em   line-height: 1.05
Extreme (C):      clamp(64px, 12vw, 200px)   weight: 500   tracking: -0.02em   line-height: 1
```

**Evidence**: 24/32 estimatable use section scale (28–56px); 6/32 use hero scale ≥ 90px (Instrument, Phantom, Shopify Editions, Deezer, Flighty, GSAP); 2/32 use body size ~16px (Notion, Linear — ultra-minimal pattern).

**Evidence status**: Observed (sizes estimated from screenshots).

### 2.3 Heading Copy Patterns

Short — averaging 3–7 words:

- **Literal**: "Page not found" · "This page could not be found" · "The page you're looking for can't be found" · "Not found"
- **Apologetic**: "Sorry, we can't find this page" · "Sorry, we couldn't find that page"
- **Humorous/product-referential**: "Pages are kind of our thing" (Craft) · "Whoops!" (Flighty) · "Oh no." (GSAP) · "Oops… it did it again" (Deezer)

---

## 3. Body Copy

Body text appears in **38/45** samples (84%). Length: 1–2 sentences. Size: 18px body or 16px body-secondary from the system type scale.

### 3.1 Body Size and Style

```css
.error-body {
    font-family: var(--font-body);        /* from shared/visual-style.md §2 */
    font-size: 18px;                      /* body text from type scale */
    font-weight: 400;                     /* body weight */
    line-height: 1.6;                     /* body line-height */
    color: var(--text);
    opacity: 0.5;                         /* subtitle/description tier from §1 */
    max-width: 540px;                     /* subtitle measure from §7 */
}
```

### 3.2 Body Content Patterns

| Pattern | Count | Example |
|---------|-------|---------|
| Cause explanation | 10/45 | "It could be any number of reasons: a broken link, a mistyped URL, or an out-of-service page." (Mercury) |
| Simple acknowledgment | 15/45 | "The page you are looking for doesn't exist or has been moved." (Unify) |
| Product-referential | 11/45 | "We haven't ghosted you!" (Phantom) · "Pages are kind of our thing, but this one doesn't seem to exist." (Craft) |
| Bridge to destinations | 6/45 | "Try one of the links below:" (Firecrawl) · "You might be looking for:" (Aave) |

**Default**: Simple acknowledgment. One sentence, literal tone, no fabricated details.

**Evidence status**: Observed.

### 3.3 Copy Rules

1. **Never fabricate product-specific references.** "Your data is safe" or "Your projects are still here" requires knowing the product's domain. If no product context is provided, use a generic message.
2. **Do not explain HTTP status codes.** "A 404 error means the server cannot find the requested resource" is developer documentation, not a 404 page. Only 0/45 samples explain the protocol.
3. **Cause sentences are optional.** "The page may have been moved, deleted, or the URL may be incorrect" adds little value — the user already knows they're lost. Use only when the apologetic tone benefits the brand.
4. **Subtitles change opacity, not color** — same `var(--text)` at opacity 0.5 (from `shared/visual-style.md` §2, Key Rule 4).

---

## 4. Status-Line Format (Developer Variant)

**When to apply**: Developer tools, API products, infrastructure platforms. Replaces the standard heading with a mono status line.

**Implementation**:

```css
.error-status-line {
    font-family: var(--font-mono);
    font-size: clamp(20px, 3vw, 32px);   /* larger than system label, smaller than section heading */
    font-weight: 400;
    letter-spacing: 0.72px;               /* mono tracking from system label */
    color: var(--text);
    /* no text-transform — the status format already reads as technical */
}
```

**Copy**: `404: Not Found` (Resend pattern) or `ERROR CODE: 404` (Instrument pattern).

**Evidence**: Resend formats the heading as "404: Not Found" in a monospace-like face. Instrument uses "ERROR CODE:   404" as a small mono label. Firecrawl uses scrambled mono characters. These are surface treatments, not standalone archetypes.

**Evidence status**: Observed.

**When NOT to apply**: Consumer products, non-technical audiences. The status-line format assumes the reader understands HTTP status codes.

---

## 5. Alignment

| Layout | Alignment | Evidence |
|--------|-----------|----------|
| Centered single block | `text-align: center` | 29/45 samples use centered layout |
| Left-aligned | `text-align: left` | 9/45 — Stripe, Mural, Handshake, Aave, Vucko, Becane, Fauna, Instrument, V7 |
| Two-column split | Text column: `text-align: left` | 5/45 — Mercury, KÖPPEN, SpaceXAI, Deezer, AI Report |

**Default**: Centered. Override to left-aligned when the archetype or layout calls for it (B with a destination list on the right, or C with an asymmetric composition).

**Evidence status**: Observed.

---

## 6. Element Stacking Order

Top to bottom within the centered content block:

```
[Label]          optional — "404" or "ERROR 404" (12px mono, system .label)
[Numeral]        optional — display numeral (clamp 120–200px) or watermark behind all
[Heading]        optional if numeral replaces it — section scale or oversized
[Body]           optional for C — 1–2 sentences at 18px / opacity 0.5
[Action]         button or text link — see recovery-actions.md
```

**Spacing** (from `section-composition.md` §6):
- Label/numeral → heading: 16px (24px if numeral is display-sized)
- Heading → body: 16px
- Body → action: 32px

These values are from the system spacing scale (`shared/visual-style.md` §3).

**Exception**: Figma places the body sentence ABOVE the numeral. This is a deliberate inversion for visual effect — not the default stacking order.
