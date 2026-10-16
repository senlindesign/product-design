# Platform Cards — Design Knowledge

> Source: Mobbin research synthesis across 21 products' Downloads page platform selection components

---

## Pattern 1: Stacked Button List

**When to use**:
- 3-6 platform options with simple structure (icon + name + optional architecture)
- Each option leads to a direct download (no additional choices needed)
- Works well inside a split hero (right column) or as a standalone section

**Execution**:

```css
.platform-list {
    display: flex;
    flex-direction: column;
    gap: 12px;                            /* spacing scale */
    max-width: 400px;                     /* prevent stretching in wider containers */
}

.platform-list .btn-dark {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;                             /* spacing scale */
    /* padding, font-size, border-radius from .btn-dark (8px 16px, 14px, 2px) */
    /* or .btn-dark + .btn-lg (12px 24px, 16px) when used as primary hero CTA */
}
```

**Platform icon** (page-specific token):
```css
.platform-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
    /* Platform-standard icons: Apple logo, Windows logo, Linux penguin, etc.
       Rendered as inline SVG or img. Color inherits button text color
       (--accent-text for .btn-dark, --text for .btn-outline) */
}
```

**Button text format**: "[Platform icon] Download for [platform] ([architecture])"
- "Download for macOS (Apple Silicon)"
- "Download for macOS (Intel)"
- "Download for Windows (x64)"
- "Download for Linux (Debian)"

**When not to use**:
- More than 6 options — the vertical list becomes excessively long; use Pattern 2 (card grid) instead
- Platforms need additional metadata (system requirements, file sizes) — use Pattern 2 or 3

**Evidence**: Shade (5 buttons), Notion (5 buttons), Craft (3 buttons)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Platform Card Grid (Recommended for Multi-Platform)

**When to use**:
- 3-5 platforms displayed as equal-weight options
- Each platform needs more than just a name — includes type label, system requirement, or download button within the card
- Product serves desktop + mobile + web equally

**Execution**:

**Container**:
```css
.platform-cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 24px;                            /* grid gutter */
    max-width: 1080px;                    /* main grid */
    margin: 0 auto;
    padding: 0 32px;
}
```

**Single Card**:
```css
.platform-card {
    padding: 32px;                        /* card internal padding */
    background: var(--surface-1);         /* #F5F5F5 (Light) / #141414 (Dark) */
    border-radius: 8px;                   /* feature card radius */
    text-align: center;
    /* zero shadow, zero border — hierarchy from background step */
    transition: transform 0.2s ease-in-out;
}
.platform-card:hover {
    transform: translateY(-4px);          /* card hover lift */
}
```

**Card internal vertical order** (top to bottom):
1. **Platform icon**: 32px (page-specific token, larger than button-inline icon)
2. **Platform name**: card heading scale
3. **Type label** (optional): label style
4. **System requirement** (optional): label style
5. **Download button or store badge**: btn-dark or btn-outline, full-width

```css
.platform-card-icon {
    width: 32px;
    height: 32px;
    margin: 0 auto 16px;
    opacity: 0.5;
    /* Platform-standard icon. Color: var(--text) for SVG icons */
}

.platform-card-name {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
}

.platform-card-type {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-top: 6px;
    /* e.g., "DESKTOP APP", "MOBILE APP", "WEB APP" */
}

.platform-card-req {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-top: 8px;
    /* e.g., "REQUIRES MACOS 10.15+", "REQUIRES WINDOWS 10+" */
}

.platform-card .btn-dark {
    width: 100%;
    margin-top: 24px;
    /* padding, font-size from .btn-dark (8px 16px, 14px) */
}
```

**Active/Selected State** (when cards act as tabs — Tailscale, Spline pattern):
```css
.platform-card.active {
    border: 1px solid var(--text);
    opacity: 1;
}
.platform-card:not(.active) {
    opacity: 0.5;
}
```
When cards act as tabs, clicking a card updates a shared CTA button below the grid (e.g., "Download Tailscale for macOS").

**Variants**:
- **3 cards**: `grid-template-columns: repeat(3, 1fr)` — most balanced layout
- **4 cards**: `repeat(4, 1fr)` — narrower cards, reduce padding to 24px if needed
- **5 cards**: `repeat(5, 1fr)` on desktop, `repeat(2, 1fr)` + orphan on narrow screens

**When not to use**:
- Fewer than 3 platforms — cards look sparse; use Pattern 1 (stacked buttons) or a hero CTA
- Cards need extensive detail (version history, multiple architecture rows) — use Pattern 3

**Evidence**: OpenPhone (5 cards), Tailscale (5 icon cards), Airtable (4 cards), Spline (4 tab-cards), Hermes (3 cards)
**Evidence status**: Cross-sample inference

---

## Pattern 3: Platform Row List

**When to use**:
- Multiple architecture variants per platform (macOS Apple Silicon, macOS Intel, macOS Universal)
- Developer tools where users care about specific package formats (.deb, .rpm, AppImage)
- Version archive pages listing all builds per version

**Execution**:

**Container**:
```css
.platform-rows {
    max-width: 1080px;                    /* main grid */
    margin: 0 auto;
    padding: 0 32px;
}
```

**Single Row**:
```css
.platform-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;                      /* spacing scale */
    border-bottom: 1px solid var(--surface-2);  /* #E9E9E9 (Light) / #1F1F1F (Dark) */
}
.platform-row:last-child {
    border-bottom: none;
}
```

**Row internal horizontal order** (left to right):
1. **Platform icon** (20px) + **Platform name** (body secondary) + **Architecture label** (mono label)
2. **Right side**: download button or download icon link

```css
.platform-row-info {
    display: flex;
    align-items: center;
    gap: 12px;
}

.platform-row-icon {
    width: 20px;
    height: 20px;
    flex-shrink: 0;
    color: var(--text);
    opacity: 0.5;
}

.platform-row-name {
    font-family: var(--font-display);
    font-size: 16px;                      /* body secondary */
    font-weight: 500;
    color: var(--text);
}

.platform-row-arch {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    /* e.g., "APPLE SILICON", "X64", "ARM64" */
}

/* Download icon link (right side) — used when the row itself is the action */
.platform-row-download {
    color: var(--text);
    opacity: 0.5;
    transition: opacity 0.3s linear;
    /* Use a 16px down-arrow icon (SVG or Unicode ↓) */
}
.platform-row-download:hover {
    opacity: 1;
}

/* Or a .btn-dark / .btn-outline button when more emphasis is needed */
```

**Multi-Column Variant** (Cursor pattern — when listing many architectures per platform):
```css
.platform-table {
    display: grid;
    grid-template-columns: repeat(3, 1fr);   /* macOS / Windows / Linux columns */
    gap: 24px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.platform-table-column h3 {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading */
    font-weight: 500;
    letter-spacing: -0.4px;
    color: var(--text);
    margin-bottom: 24px;
}
/* Each column contains .platform-row items stacked vertically */
```

**When not to use**:
- Fewer than 3 platform variants — rows look sparse; use Pattern 1 (buttons)
- Non-technical audience — rows with architecture labels confuse average users; use Pattern 2 (cards)

**Evidence**: Linear (6 rows), Cursor (3-column table), 1Password (tab bar + rows)
**Evidence status**: Cross-sample inference

---

## Pattern 4: Desktop/Mobile Split

**When to use**:
- Product has both desktop and mobile apps
- Desktop and mobile downloads use different methods (direct download vs. app store)
- Desktop has multiple platforms (macOS/Windows/Linux), mobile has 2 (iOS/Android)

**Execution**:

**Container**: Two card-sections stacked vertically, each with its own heading.
```css
.platform-split {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
    display: flex;
    flex-direction: column;
    gap: 32px;                            /* gap between Desktop and Mobile cards */
}
```

**Section Card**:
```css
.platform-split-section {
    padding: 32px;                        /* card internal padding */
    background: var(--surface-1);         /* #F5F5F5 (Light) / #141414 (Dark) */
    border-radius: 8px;                   /* feature card radius */
}

.platform-split-heading {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading */
    font-weight: 500;
    letter-spacing: -0.4px;
    color: var(--text);
    margin-bottom: 8px;
}

.platform-split-desc {
    font-family: var(--font-body);
    font-size: 16px;                      /* body text */
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    line-height: 1.6;
    margin-bottom: 24px;
}
```

Inside each section card, platform rows use the same `.platform-row` tokens from Pattern 3.

**Desktop section content**:
- Heading: "[Product] Desktop" or "Desktop Apps"
- Rows: macOS, Windows, Linux — each with "Download" button or download icon
- Architecture variants as sublabels (Apple Silicon / Intel / x64 / ARM64)

**Mobile section content**:
- Heading: "[Product] Mobile" or "Mobile Apps"
- Rows: iOS, Android — each with App Store / Google Play badge or "Open store" button
- QR code option (Linear pattern): show a QR code icon that opens a code for phone scanning

**When not to use**:
- Desktop only (no mobile app) — skip the Mobile section entirely; use Pattern 1, 2, or 3
- One platform only — a section split is meaningless; use the hero CTA alone

**Evidence**: Linear, Craft, Frontify, ClickUp, Airtable, TIDAL
**Evidence status**: Cross-sample inference

---

## Shared Rules Across All Patterns

### Platform Icon Set

Use platform-standard icons (rendered as monochrome SVGs inheriting `var(--text)` color):
- **macOS/Mac**: Apple logo
- **Windows**: Windows logo (4-pane)
- **Linux**: Tux penguin (or distribution-specific: Ubuntu, Debian, Fedora)
- **iOS**: App Store icon or Apple logo + "iOS" label
- **Android**: Play Store icon or Android robot
- **Web**: Globe icon or browser icon
- **CLI**: Terminal prompt icon (`>_`)

Icon sizes (page-specific tokens):
- Button-inline: 16px (inside CTA buttons)
- Card icon: 32px (at top of platform cards)
- Row icon: 20px (in platform row lists)

### Architecture Labels

Always render in mono label style:
```css
/* Uses .label tokens from visual-style.md */
font-family: var(--font-mono);
font-size: 12px;
font-weight: 400;
letter-spacing: 0.72px;
text-transform: uppercase;
color: var(--text);
opacity: 0.4;
```

Common labels: "APPLE SILICON", "INTEL", "X64", "ARM64", "UNIVERSAL", "DEBIAN", "FEDORA", "APPIMAGE"

### Store Badges (Mobile)

For iOS/Android mobile apps, use official App Store / Google Play badge images rather than custom download buttons. Place them at badge standard height (~40px). Do not recreate badge designs with CSS.

### Narrow Screen Adaptation

```css
@media (max-width: 767px) {
    .platform-cards {
        grid-template-columns: 1fr 1fr;   /* 2 columns on narrow, not 5 */
        gap: 16px;                         /* tighter gap */
    }

    .platform-table {
        grid-template-columns: 1fr;        /* stack columns on narrow */
    }

    .platform-card {
        padding: 24px;                     /* 32px → 24px */
    }
}
```
