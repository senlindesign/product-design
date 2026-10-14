# Newsletter Section — Design Knowledge

> Source: Mobbin research across 8 newsletter/email-capture sections on blog pages (Round 4, 2026-10-02)

---

## Overview

The newsletter section is an email capture component that appears in three positions on blog pages: at the bottom of the page (3/8), in the sidebar (3/8), or inline between content (2/8). It uses a single email field in 6/8 cases.

Newsletter sections on blog pages differ from general landing-page newsletter captures: here, the visitor is already engaged (reading the blog), so copy should acknowledge that context ("stay updated on future posts") rather than making a broad product pitch.

**Position guide**:
- **Bottom section** — reaches everyone who reads to the end; safe default
- **Inline within grid** — intercepts mid-browse; high visibility but may disrupt scanning
- **Sidebar** — persistent alongside article list; higher surface area but requires sidebar layout

---

## Pattern 1: Bottom Full-Width Section

**When to use**:
- All archetypes (A, B, C) — the safe default position
- Does not require a sidebar layout
- 3/8 products place the newsletter at the bottom

**Layout A — 2-column (heading left, form right)**:
```
┌──────────────────────────────────────────────────────┐
│  Heading text                 [Email field] [Submit] │
│  Subtitle (optional)                                  │
└──────────────────────────────────────────────────────┘
```

**CSS tokens**:
```css
/* Section container */
.newsletter-section {
    padding: 180px 32px;                 /* section rhythm — from visual-style.md §3 */
    max-width: 1080px;
    margin: 0 auto;
}

/* 2-column layout: heading left, form right */
.newsletter-inner {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 58px;                           /* standard column gap — from visual-style.md §3 */
    align-items: center;
    border-top: 1px solid var(--surface-2);   /* divides from article grid above */
    padding-top: 58px;                   /* heading-to-content gap — visual-style.md §3 */
}

/* Heading */
.newsletter-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading — from visual-style.md §2 */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.2;
    color: var(--text);
    margin-bottom: 12px;
}

/* Subtitle */
.newsletter-subtitle {
    font-family: var(--font-body);
    font-size: 16px;                     /* body secondary — from visual-style.md §2 */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                        /* subtitle opacity — from visual-style.md §1 */
    max-width: 400px;
}
```

**Layout B — Centered single-column** (Hashnode, OpenTable):
```
           [ Heading ]
        [ Short subtitle ]
  [ Email input ]  [ Subscribe ]
  [ Privacy note / unsubscribe ]
```

```css
.newsletter-section--centered {
    padding: 180px 32px;
    text-align: center;
}

.newsletter-section--centered .newsletter-heading {
    font-family: var(--font-display);
    font-size: 27px;
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.2;
    color: var(--text);
    margin-bottom: 16px;
}

.newsletter-section--centered .newsletter-subtitle {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    max-width: 480px;
    margin: 0 auto 32px;
}
```

**Evidence**: ClassPass (2-col blue band), Clockwise (2-col white bar), Hashnode (centered minimal), OpenTable (centered with subtitle)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Inline Card Within Article Grid

**When to use**:
- Archetype A (Grid Index) — occupies one card slot in the grid
- Blog has a 3- or 4-column grid where one slot can be converted to the capture card
- Higher visibility than bottom placement; appears before the user finishes browsing

**Layout**:
```
┌──────────────────────────────────┐
│  Heading                         │  ← card heading scale
│  Description (1-2 lines)         │  ← body secondary
│  ┌───────────────────────────┐   │
│  │ Enter email        [Btn]  │   │
│  └───────────────────────────┘   │
└──────────────────────────────────┘
```

**CSS tokens**:
```css
/* Newsletter card — same dimensions as an article card in the grid */
.newsletter-card {
    background: var(--surface-1);
    border-radius: 16px;                 /* content card — from visual-style.md §4 */
    padding: 32px;                       /* card internal padding — from visual-style.md §3 */
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.newsletter-card-heading {
    font-family: var(--font-display);
    font-size: 20px;                     /* card heading — from visual-style.md §2 */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 8px;
}

.newsletter-card-description {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    margin-bottom: 24px;
}
```

**When not to use**:
- 2-column grid — the card takes up 50% of the row, which feels heavy
- Archetype C (Minimal List) — no grid exists; use bottom section instead

**Evidence**: Apollo (newsletter card inside 4-col dark article grid)
**Evidence status**: Single source observation

---

## Pattern 3: Sidebar Card

**When to use**:
- Archetype A or C with a sidebar layout (see `blog-header.md` Pattern 1 sidebar variant)
- Newsletter capture is persistent alongside the article list as users scroll

**Layout**:
```
┌─────────────────┐
│  Heading        │  ← card heading scale
│  Description    │  ← value proposition, 2-3 lines
│  [Email input]  │
│  [Subscribe]    │
│  Privacy note   │
│  --- social --- │  ← optional social links
└─────────────────┘
```

**CSS tokens**:
```css
.newsletter-sidebar {
    background: var(--surface-1);
    border-radius: 16px;
    padding: 32px;
    position: sticky;
    top: calc(var(--nav-h) + 24px);     /* clear fixed nav — from visual-style.md §8 */
}

.newsletter-sidebar-heading {
    font-family: var(--font-display);
    font-size: 20px;                     /* card heading — from visual-style.md §2 */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 12px;
}

.newsletter-sidebar-description {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    margin-bottom: 24px;
}
```

**Complex sidebar forms (lead gen)**: ClassPass uses a 5-field sidebar form (first name, last name, email, company, dropdown). This is a B2B lead-gen form disguised as a newsletter — appropriate for enterprise-focused blogs. For standard product blogs, single email field is sufficient.

**Evidence**: Sprig (sidebar with description + social links), ClassPass (sidebar B2B multi-field)
**Evidence status**: Cross-sample inference

---

## Email Form Component

All three patterns share the same form component. Copy this block — do not invent input tokens:

```css
/* Email form container */
.newsletter-form {
    display: flex;
    gap: 8px;
    align-items: center;
}

/* Email input */
.newsletter-input {
    flex: 1;
    height: 36px;                        /* matches btn-dark line-height + padding: 8+20+8=36px */
    padding: 8px 16px;                   /* from visual-style.md §8 button tokens */
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    line-height: 20px;
    color: var(--text);
    background: var(--bg);
    border: 1px solid var(--surface-2);
    border-radius: 4px;                  /* input radius — from visual-style.md §4 */
    outline: none;
    transition: border-color 0.3s linear;
}
.newsletter-input::placeholder {
    color: var(--text);
    opacity: 0.4;
}
.newsletter-input:focus-visible {
    border-color: var(--text);
    outline: 2px solid var(--text);      /* focus-visible — from visual-style.md §8 */
    outline-offset: 2px;
}

/* Submit button — uses standard .btn-dark from visual-style.md */
.newsletter-submit {
    padding: 8px 16px;
    font-size: 14px;
    font-weight: 500;
    font-family: var(--font-display);
    line-height: 20px;
    background: var(--accent);
    color: var(--accent-text);
    border: none;
    border-radius: 2px;                  /* button radius — from visual-style.md §4 */
    cursor: pointer;
    white-space: nowrap;
    transition: transform 0.2s ease-in-out;
}
.newsletter-submit:hover { transform: translateY(-1px); }

/* Alternative: stacked form (input above, button below — use when width is constrained) */
.newsletter-form--stacked {
    display: flex;
    flex-direction: column;
    gap: 8px;
}
.newsletter-form--stacked .newsletter-input {
    width: 100%;
}
.newsletter-form--stacked .newsletter-submit {
    width: 100%;
}
```

---

## Copy Strategies

**Heading approaches by frequency**:
- **Functional** (5/8): "Subscribe to our newsletter", "Subscribe for weekly updates", "Sign up for email updates". Clear, direct, no friction.
- **Value-forward** (2/8): "Get insights, event info and more" (ClassPass), "Get the best content on user insights..." (Sprig). Justifies the email exchange with a benefit.
- **Brand-creative** (1/8): "Hungry for more?" (OpenTable). Works when there is a strong brand voice — risky without it.

**Recommendation**: For product blogs, use functional headings. Explain what the subscriber gets and how often ("weekly updates", "monthly newsletter").

**CTA button text**:
- Subscribe (3 products)
- Sign up (2 products)
- Submit (1 product — generic, avoid)
- Custom ("Get on the list!", "SIGN ME UP") — only if it fits brand voice

**Privacy/consent note** (4/8 include it):

```html
<p class="newsletter-privacy">
    You can unsubscribe at any time.
    <a href="/privacy">Privacy policy</a>
</p>
```

```css
.newsletter-privacy {
    font-family: var(--font-body);
    font-size: 12px;                     /* label scale — from visual-style.md §2 */
    font-weight: 400;
    color: var(--text);
    opacity: 0.4;
    margin-top: 12px;
    line-height: 1.5;
}
.newsletter-privacy a {
    color: var(--text);
    opacity: 0.4;
    text-decoration: underline;
    text-underline-offset: 2px;
}
```

Include the privacy note if: GDPR-relevant audience (European users), enterprise product, or the form includes name/company fields. Omit for minimal developer-focused blogs where it adds visual noise.

---

## Color Treatment

**Default (achromatic)**: Use `var(--surface-1)` for cards, `var(--bg)` for the section background — stays within the color silence principle. Input border `var(--surface-2)`. Submit button uses `var(--accent)` = `var(--text)` by default.

**Colored band variant** (ClassPass, Apollo): Use a distinct background only when the newsletter section needs clear separation from the article grid. Avoid brand colors without user specification — the achromatic defaults are always safe.

```css
/* Avoid unless user provides a brand color */
.newsletter-section--dark {
    background: var(--surface-1);        /* achromatic dark band */
    padding: 128px 32px;                 /* large breathing space — visual-style.md §3 (narrow: 80px) */
}
```

---

## Spacing Tokens

```
Newsletter section padding:           180px top/bottom (section rhythm — from visual-style.md §3)
2-column gap (heading + form):        58px  (from visual-style.md §3)
Form gap (input + button):            8px   (from visual-style.md §3 base scale)
Card internal padding:                32px  (from visual-style.md §3)
Heading-to-form gap:                  24px  (from visual-style.md §3)
Privacy note top margin:              12px  (from visual-style.md §3 base scale)
```

---

## Responsive Behavior (≤767px)

```css
@media (max-width: 767px) {
    .newsletter-section {
        padding: 80px 20px;              /* 128px → 80px — from visual-style.md narrow-screen table */
    }

    /* 2-column → stacked */
    .newsletter-inner {
        grid-template-columns: 1fr;
        gap: 32px;
        padding-top: 40px;               /* 58px → 40px — from visual-style.md narrow-screen table */
    }

    /* Input + button → stacked */
    .newsletter-form {
        flex-direction: column;
    }
    .newsletter-input {
        width: 100%;
    }
    .newsletter-submit {
        width: 100%;
    }

    /* Sidebar → not sticky, full width above footer */
    .newsletter-sidebar {
        position: static;
        margin-top: 32px;
    }
}
```

---

## Evidence

| Pattern | Position | Products | Archetype |
|---------|----------|----------|-----------|
| 2-column bottom band | Bottom | ClassPass | A |
| 2-column horizontal bar | Inline (header-content) | Clockwise | A |
| Centered minimal | Bottom | Hashnode | A/B |
| Centered with subtitle + social | Bottom | OpenTable | B |
| Inline grid card | Within article grid | Apollo | A |
| Sidebar card (single field) | Sidebar | Sprig | A/B |
| Sidebar multi-field (B2B) | Sidebar | ClassPass | A (enterprise) |
