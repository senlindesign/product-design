# Downloads Page — Section Composition

> Source: 42 section observations across 21 unique products. All spacing/color tokens validated against `shared/visual-style.md`.

---

## Default Section Order by Archetype

### A. Platform Selector (3-5 sections)

```
Nav
Hero / Header (product icon + heading + auto-detect CTA + compatibility note)
Platform List (manual platform selection below the fold)
[Optional: Mobile Section — separated from Desktop]
Footer
```

**Optional additions** (insert at marked positions):
- Mobile Section: after Platform List, when both desktop and mobile apps exist (Linear, Craft, Frontify, ClickUp — 4/21 products separate Desktop and Mobile)

### B. Multi-Product (4-6 sections)

```
Nav
Header ("APPS" mono label + heading)
Featured Products (2-column cards: Desktop + Mobile)
[Optional: Secondary Products (3-column cards: Extensions, Add-ons)]
[Optional: Developer Tools (CLI, SDK — card grid)]
Footer
```

**Optional additions**:
- Secondary Products: when the company ships browser extensions, add-ons, or integrations (ClickUp: Chrome Extension, Voice Assistants, Email Add-ons)
- Developer Tools: when a separate developer audience exists (1Password Dev: 3x3 tool grid)

### C. Developer Distribution (3-5 sections)

```
Nav
Hero / Header (heading + install command in code block)
[Optional: IDE Extension (split layout with install button)]
[Optional: Version Archive (version-grouped architecture matrix)]
[Optional: Feature Summary (brief feature grid)]
Footer
```

**Optional additions**:
- IDE Extension: when the tool has both CLI and IDE extension (Height: VSCode + CLI split)
- Version Archive: when users need access to previous versions (Cursor: full version history)
- Feature Summary: brief grid below install command (Height: feature grid explaining CLI)

---

## Page Width and Layout

Downloads pages are structurally simpler than Landing or Pricing pages. Most observations show narrower content widths and fewer sections.

### Content Width

```css
.container {
    max-width: 1080px;                /* system grid — shared/visual-style.md section 7 */
    margin: 0 auto;
    padding: 0 32px;
}
```

Many Downloads pages use narrower content within the standard container:

```css
.downloads-content {
    max-width: 720px;                 /* centered within container — used when content is just
                                         heading + buttons + compatibility note (no side-by-side layout) */
    margin: 0 auto;
    text-align: center;
}
```

Evidence: Linear, Notion, Tailscale, Windsurf, Giga, SpaceXAI, TIDAL all center their download content within a narrower column. The full 1080px grid is used only for card layouts (Archetype B: ClickUp, 1Password Dev) or platform tab bars (1Password: 7 tabs).

### Single-Viewport Pages

Most Archetype A pages fit on a single viewport or within one scroll. Evidence: OpenAI (single card), SpaceXAI (2-row list), Windsurf (heading + 2 buttons + link), Linear hero (icon + heading + CTA + note).

Do not stretch a simple 3-platform Downloads page to fill multiple viewports with padding. The page should be as long as its content requires — nothing more.

---

## Section Rhythm and Spacing

All spacing values from `shared/visual-style.md` section 3.

### Hero / Header Area

```css
.downloads-hero {
    padding-top: 128px;               /* hero top whitespace — system */
    padding-bottom: 58px;             /* heading-to-content, not full section rhythm —
                                         because the platform list follows immediately */
    text-align: center;
}
```

Note: Downloads pages do NOT use the 180px section rhythm between hero and platform list. The platform list is part of the hero's content area, not a separate section. Using 180px padding between the heading and the download buttons creates an awkward gap. Evidence: Linear, Tailscale, Notion, Windsurf all position the platform selection immediately below the heading with minimal spacing.

### Between Hero Content and Platform List

```css
.downloads-hero .heading {
    margin-bottom: 24px;              /* hero heading to subtitle — system */
}

.downloads-hero .subtitle {
    margin-bottom: 48px;             /* subtitle to CTA — system (subheading to CTA) */
}

.platform-list {
    margin-top: 32px;                /* below primary CTA to manual platform list */
}
```

### Optional Mobile Section (when separated from Desktop)

```css
.mobile-section {
    padding-top: 128px;              /* large breathing space between Desktop and Mobile */
    padding-bottom: 128px;
}
```

Evidence: Linear uses "Linear Desktop" and "Linear Mobile" as separate sections with their own descriptions. Craft, Frontify, and ClickUp also separate Desktop and Mobile.

### Footer Spacing

```css
.footer {
    padding-top: 128px;              /* footer top padding — system */
}
```

### Narrow Screen (< 768px)

```css
@media (max-width: 767px) {
    .downloads-hero {
        padding-top: 80px;           /* 128px -> 80px — system */
    }
    .downloads-hero .subtitle {
        margin-bottom: 32px;         /* tighter on narrow */
    }
    .container {
        padding: 0 20px;             /* 32px -> 20px — system */
    }
    .mobile-section {
        padding-top: 80px;           /* 128px -> 80px — system */
        padding-bottom: 80px;
    }
}
```

---

## Background Rules

Downloads pages follow the same background rules as all page types (`shared/visual-style.md` section 8).

| Section | Background | Rationale |
|---------|-----------|-----------|
| Hero / Header | `var(--bg)` | Always page background |
| Platform List | `var(--bg)` | Same section as hero content |
| Mobile Section | `var(--bg)` | Default |
| Product Cards (B) | `var(--surface-1)` | Cards use surface-1 per system card token |
| Code Block (C) | `var(--surface-1)` | Code blocks use surface-1 per system |
| Version Archive (C) | `var(--bg)` | Rows with subtle dividers, not card backgrounds |

**Rules**:
- At most 1 section uses `var(--surface-1)` background. Downloads pages are too short for multiple background switches
- No colored backgrounds per platform card (see anti-patterns.md: Airtable's gradient cards)
- No per-platform accent colors
- All neutral colors must be pure achromatic (zero hue shift)

---

## Nav and Footer

Reuse shared components without modification:
- **Navigation**: `shared/navigation.md` + `sections/navigation/SKILL.md`
- **Footer**: `shared/footer.md` + `sections/footer/SKILL.md`

Nav height is `68px` (`var(--nav-h)`). When using `position: fixed`, add `body { padding-top: var(--nav-h); }` to prevent the hero heading from sitting under the nav.

---

## Component Patterns

### Platform Card (Archetype A, equal-weight pattern)

Used when showing 3-5 platforms as equal-weight options (OpenPhone, Airtable, Tailscale, Spline tabs).

```css
.platform-card {
    padding: 32px;                    /* card internal padding — system */
    background: var(--surface-1);     /* card background — system */
    border-radius: 8px;              /* feature card radius — system */
    text-align: center;
    /* zero shadow — system section 5 */
}

.platform-card-icon {
    width: 32px;
    height: 32px;
    margin-bottom: 16px;
    color: var(--text);
    opacity: 0.5;                    /* platform icon at description tier */
}

.platform-card-name {
    font-family: var(--font-display);
    font-size: 20px;                 /* card heading — system */
    font-weight: 500;
    letter-spacing: -0.4px;          /* card heading tracking — system */
    line-height: 1.3;
    color: var(--text);
}

.platform-card-type {
    font-family: var(--font-mono);
    font-size: 12px;                 /* label scale — system */
    font-weight: 400;
    letter-spacing: 0.72px;          /* label tracking — system */
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                    /* label opacity — system */
    margin-top: 6px;
}
```

Grid layout:

```css
.platform-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 24px;                       /* grid gutter — system */
    max-width: 720px;
    margin: 0 auto;
}

@media (max-width: 767px) {
    .platform-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}
```

### Platform Row (Archetype A, auto-detect pattern)

Used when auto-detect CTA is primary and manual selection is a secondary list below (Linear, Cursor).

```css
.platform-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;
    border-bottom: 1px solid var(--surface-2);   /* divider — system */
}

.platform-row-label {
    font-family: var(--font-display);
    font-size: 16px;                 /* body secondary — system */
    font-weight: 500;
    color: var(--text);
}

.platform-row-arch {
    font-family: var(--font-mono);
    font-size: 12px;                 /* label scale — system */
    font-weight: 400;
    color: var(--text);
    opacity: 0.4;                    /* label opacity — system */
}
```

### Product Card (Archetype B)

Used for multi-product layouts (ClickUp, 1Password Dev).

```css
.product-card {
    padding: 32px;                   /* card internal padding — system */
    background: var(--surface-1);    /* card background — system */
    border-radius: 16px;            /* content card radius — system */
    /* zero shadow — system section 5 */
}

.product-card-label {
    font-family: var(--font-mono);
    font-size: 12px;                 /* label — system */
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 16px;
}

.product-card-heading {
    font-family: var(--font-display);
    font-size: 20px;                 /* card heading — system */
    font-weight: 500;
    letter-spacing: -0.4px;          /* card heading tracking — system */
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 8px;
}

.product-card-description {
    font-family: var(--font-display);
    font-size: 16px;                 /* body secondary — system */
    font-weight: 500;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;                    /* subtitle tier — system */
    margin-bottom: 24px;
}
```

### Install Command Block (Archetype C)

Used for CLI/SDK install commands (Giga, Height).

```css
.install-block {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 24px;
    background: var(--surface-1);    /* code block background — system */
    border-radius: 8px;             /* feature card radius — system */
    max-width: 540px;               /* subtitle measure — system section 7 */
    margin: 0 auto;
}

.install-command {
    font-family: var(--font-mono);
    font-size: 14px;                 /* button/nav scale — system */
    font-weight: 400;
    color: var(--text);
}

.install-command .prompt {
    color: var(--text);
    opacity: 0.4;                    /* de-emphasized prompt symbol */
}

.copy-button {
    background: none;
    border: none;
    padding: 4px;
    color: var(--text);
    opacity: 0.4;                    /* auxiliary tier — system */
    cursor: pointer;
    transition: opacity 0.3s linear;     /* system transition */
    /* Uses a 16px clipboard SVG icon */
}
.copy-button:hover { opacity: 1; }
```

Copy button JavaScript:

```javascript
document.querySelectorAll('.copy-button').forEach(btn => {
    btn.addEventListener('click', () => {
        const command = btn.closest('.install-block').querySelector('.install-command').textContent.replace('$ ', '');
        navigator.clipboard.writeText(command);
        btn.textContent = 'Copied';
        setTimeout(() => { btn.textContent = 'Copy'; }, 2000);
    });
});
```

---

## Compatibility Note Pattern

Appears below the primary CTA in auto-detect layouts. Evidence: Linear ("Compatible with Apple Silicon and Intel"), Craft ("Optimized for Apple Silicon"), Tailscale ("Requires macOS Big Sur 11.0 or later").

```css
.compatibility-note {
    font-family: var(--font-mono);
    font-size: 12px;                 /* label scale — system */
    font-weight: 400;
    letter-spacing: 0.72px;          /* label tracking — system */
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                    /* auxiliary tier — system */
    margin-top: 16px;
}
```

---

## "View All Platforms" Link Pattern

Used with auto-detect CTA to provide access to manual platform selection. Evidence: Windsurf ("Not using macOS? View all download options"), SpaceXAI ("More downloads").

```css
.all-platforms-link {
    font-family: var(--font-display);
    font-size: 14px;                 /* button/nav scale — system */
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    text-decoration: none;
    transition: opacity 0.3s linear;     /* system transition */
    margin-top: 24px;
    display: inline-block;
}
.all-platforms-link:hover { opacity: 1; }
```

---

## System Requirements Display

Majority of products (16/21) show no system requirements. When displayed, they appear inline below the CTA or per-card.

```css
.system-req {
    font-family: var(--font-mono);
    font-size: 12px;                 /* label scale — system */
    font-weight: 400;
    color: var(--text);
    opacity: 0.4;                    /* auxiliary tier — system */
    margin-top: 8px;
}
```

---

## Total Page Length by Archetype

| Archetype | Section count | Relative length |
|-----------|--------------|-----------------|
| A. Platform Selector | 3-5 | Shortest (often single viewport) |
| B. Multi-Product | 4-6 | Medium |
| C. Developer Distribution | 3-5 | Short to medium (version archive can extend) |

### Narrow Screen Behavior

All sections stack naturally in a single column. No section reordering is needed on narrow screens. Platform card grids collapse to 2 columns. Platform rows remain full-width. Install command blocks remain full-width with horizontal scrolling if needed.
