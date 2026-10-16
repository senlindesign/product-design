# Download Hero — Design Knowledge

> Source: Mobbin research synthesis across 21 products' Downloads page hero/header sections

---

## Pattern 1: Auto-Detect Hero (Recommended Default, ~60% of samples)

**When to use**:
- Product has a native desktop app with a clear primary platform
- The user's OS can be detected via `navigator.platform` / `navigator.userAgent`
- Goal: minimize friction — one click to download

**Execution**:

**Layout**: Centered single column, vertically stacked:
1. [Optional] App icon (centered)
2. Heading
3. Subtitle
4. Primary CTA button (auto-detected OS)
5. [Optional] Compatibility note
6. [Optional] "Not using [OS]?" secondary link

```css
.download-hero {
    text-align: center;
    padding-top: 128px;               /* hero top whitespace — system */
    padding-bottom: 58px;             /* heading-to-content — platform list is part of hero,
                                         not a separate section (see section-composition.md) */
    /* Note: if nav is position: fixed, body has padding-top: var(--nav-h),
       so this 128px measures from below the nav as intended */
}

.download-hero .container {
    max-width: 1080px;                /* main grid */
    margin: 0 auto;
    padding: 0 32px;
}
```

**App Icon** (page-specific token — not in shared system):
```css
.download-hero-icon {
    width: 64px;
    height: 64px;
    margin: 0 auto 32px;             /* 32px gap to heading */
    border-radius: 16px;             /* content-card radius — matches macOS icon shape */
    /* Use the product's actual app icon. If unavailable, use a surface-1
       rounded square with the product's first letter in --font-display */
}
```

**Heading**: Uses section heading scale — Downloads pages are structurally simpler than Landing pages, so hero heading scale (clamp 48-80px) would be disproportionate.
```css
.download-hero h1 {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}
```

**Subtitle**:
```css
.download-hero .subtitle {
    font-family: var(--font-body);
    font-size: 18px;                      /* body text */
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;                     /* subtitle measure cap */
    margin: 24px auto 0;                  /* hero heading to subheading: 24px */
}
```

**Primary CTA**: Auto-detected OS button. Uses `.btn-lg` for visual weight when centered below a large heading.
```css
.download-hero .btn-primary {
    /* Inherits .btn-dark + .btn-lg */
    /* padding: 12px 24px; font-size: 16px; */
    margin-top: 48px;                     /* subheading to CTA: 48px */
}
```
CTA text: "Download for macOS" / "Download for Windows" / "Download for Linux" — auto-detected. Include a platform icon (Apple/Windows/Linux) inline at 16px before the text.

**Compatibility Note** (page-specific token — derived from .label style):
```css
.download-hero .compat-note {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-top: 16px;
    /* e.g., "COMPATIBLE WITH APPLE SILICON AND INTEL" */
    /* e.g., "OPTIMIZED FOR APPLE SILICON" */
}
```

**Secondary Platform Link**: For users on a different OS.
```css
.download-hero .alt-platform {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;                         /* secondary element — subtitle tier */
    text-decoration: none;
    transition: opacity 0.3s linear;
    margin-top: 24px;                     /* spacing scale */
    display: inline-block;
    /* e.g., "Not using macOS? View all download options" */
}
.download-hero .alt-platform:hover { opacity: 1; }
```

**Heading text patterns** (from observations):
- "Download [Product]" — Linear, Shade, TIDAL, Cursor (most common)
- "Get [Product] for [platform]" — Craft
- "Download [Product] for [detected OS]" — Windsurf (OS name in heading)

**Evidence**: Linear, Spline, Windsurf, Cursor, Craft, 1Password, SpaceXAI, OpenAI (11/21 products)
**Evidence status**: Cross-sample inference

---

## Pattern 2: All-Platforms Hero (~25% of samples)

**When to use**:
- Product has 3-5 platforms with roughly equal importance (no dominant platform)
- User should see all options at a glance — no auto-detection needed
- Cross-platform is a selling point (e.g., "works everywhere")

**Execution**:

**Layout**: Centered single column, vertically stacked:
1. Heading
2. Subtitle
3. Platform button row or card row (3-5 items, equally weighted)

```css
.download-hero-all {
    text-align: center;
    padding-top: 128px;
    padding-bottom: 58px;
}
```

Heading and subtitle use the same tokens as Pattern 1.

**Platform Button Row** (when using stacked buttons — Notion pattern):
```css
.platform-buttons {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    margin-top: 48px;                     /* subheading to CTA */
    max-width: 400px;                     /* prevent buttons from stretching to full container */
    margin-left: auto;
    margin-right: auto;
}

.platform-buttons .btn-dark {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    /* padding, font-size, etc. from .btn-dark + .btn-lg */
}
```

**Platform Card Row** (when using cards — OpenPhone, Tailscale pattern):
See `platform-cards.md` Pattern 2 for card grid tokens. The card row is placed inline in the hero with the same `margin-top: 48px` gap.

**Variants**:
- **Button list** (Notion): 5 full-width dark buttons stacked vertically, each with platform icon + "Download for [platform] ([architecture])"
- **Icon cards** (Tailscale): 5 square icon cards in a row, clicking one updates a CTA button below
- **Equal cards** (OpenPhone): 5 cards in a row with icon + platform name + type label

**When not to use**:
- Product has a clear primary platform (use Pattern 1 instead)
- More than 6 platforms — too many equal-weight options causes decision paralysis; group by Desktop/Mobile instead (see Pattern 2 in `platform-cards.md`)

**Evidence**: Notion (5 buttons), OpenPhone (5 cards), Tailscale (5 icon cards), Airtable (4 cards), Spline (4 tab-cards)
**Evidence status**: Cross-sample inference

---

## Pattern 3: Split Hero (~15% of samples)

**When to use**:
- Product wants to provide context/description alongside download options
- CLI/developer tools where install method selection is the primary action (Height: VSCode extension vs. CLI)
- Product screenshot or device mockup is a significant visual element

**Execution**:

**Layout**: Two-column split — left column (heading + subtitle + description) / right column (platform buttons or install command or product visual).

```css
.download-hero-split {
    padding-top: 128px;
    padding-bottom: 58px;
}

.download-hero-split .container {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 58px;                            /* alternating row gap */
    align-items: center;
}
```

Left column uses the same heading and subtitle tokens as Pattern 1, but `text-align: left` instead of `center`.

Right column content varies:
- **Platform button list** (Shade): stacked `.btn-dark` buttons, full width within the right column
- **Install command** (Height): dark code block with copy button — see `version-info.md` Install Commands section
- **Product visual** (Clay, Spline): product screenshot in a `surface-1` rounded frame

**When not to use**:
- 5+ platforms to display — the right column gets too tall; use Pattern 1 or 2 with a platform section below

**Evidence**: Shade, SpaceXAI, Height, Clay
**Evidence status**: Cross-sample inference

---

## Auto-Detection Logic

```javascript
function detectPlatform() {
    const ua = navigator.userAgent;
    const platform = navigator.platform || '';

    // Mobile checks FIRST — Android sets navigator.platform to "Linux",
    // so checking Linux before Android would misidentify Android as Linux desktop
    if (/Android/i.test(ua)) {
        return { os: 'Android', label: 'Get it on Android' };
    }
    if (/iPhone|iPad|iPod/i.test(ua)) {
        return { os: 'iOS', label: 'Download on the App Store' };
    }
    if (/Mac/i.test(platform) || /Mac/i.test(ua)) {
        // Apple Silicon vs Intel: reliable detection requires WebGL renderer check; offer both
        return { os: 'macOS', label: 'Download for macOS' };
    }
    if (/Win/i.test(platform) || /Windows/i.test(ua)) {
        return { os: 'Windows', label: 'Download for Windows' };
    }
    if (/Linux/i.test(platform) || /Linux/i.test(ua)) {
        return { os: 'Linux', label: 'Download for Linux' };
    }
    // Fallback: show all platforms (Pattern 2)
    return { os: 'unknown', label: 'Download' };
}
```

**Rules**:
- Auto-detection updates the CTA button text and download link only
- If detection fails, fall back to a generic "Download" button or show all platforms
- Never hide other platforms entirely — always provide a "View all download options" link
- Architecture detection (Apple Silicon vs. Intel) is unreliable in browsers — show a compatibility note or offer both options instead of guessing

---

## Narrow Screen Adaptation

```css
@media (max-width: 767px) {
    .download-hero {
        padding: 80px 0 40px;             /* 128px → 80px top, 58px → 40px bottom */
    }

    .download-hero .container {
        padding: 0 20px;                  /* 32px → 20px */
    }

    /* Split hero collapses to single column */
    .download-hero-split .container {
        grid-template-columns: 1fr;
        gap: 40px;                        /* 58px → 40px */
    }
}
```
