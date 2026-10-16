# Anti-Patterns — Downloads Page

> Source: 42 section observations across 21 unique products + lessons from Landing/Pricing/Contact/404/About/Product/Blog/Section Skills practice. Every rule validated against `shared/visual-style.md`.

---

## 1. Visual Errors

### 1.1 Colorful Platform Card Backgrounds

**Problem**: Each platform card has its own colored or gradient background (e.g., dark blue for macOS, teal for Windows, rainbow for iOS, green/yellow for Android).
**Why it's wrong**: `shared/visual-style.md` section 1 explicitly forbids "Different accent colors for individual feature cards" and "Colored circular/square backgrounds behind icons." Per-platform color coding also violates color silence: "chromatic color occupies <10% of visible page area."
**Evidence**: Airtable uses vivid gradient backgrounds per card. This is an outlier — 18/21 products use uniform card styling without per-platform color variation.
**Correct approach**: All platform cards use the same `var(--surface-1)` background. Differentiation comes from the platform icon and label, not background color.

```css
/* Correct */
.platform-card {
    background: var(--surface-1);     /* #F5F5F5 light / #141414 dark */
    border-radius: 8px;              /* feature card — system */
    /* zero shadow */
}

/* Wrong */
.platform-card-macos { background: linear-gradient(135deg, #1a1a3e, #2d2d5e); }
.platform-card-windows { background: linear-gradient(135deg, #0a3d4e, #1a5d6e); }
```

**Checklist item**: Do all platform cards share the same background color?

---

### 1.2 Platform Icons with Colored Backgrounds

**Problem**: Platform icons are placed on colored circles or squares (e.g., Windows icon on a blue circle, Apple icon on a gray circle).
**Why it's wrong**: `shared/visual-style.md` section 1 accent allowed-use list is exhaustive. "Icon backgrounds, badge fills" are explicitly marked with a red cross. Platform icons should be rendered directly without decorative containers.
**Evidence**: OpenPhone uses subtle bordered cards (correct pattern); Airtable uses large centered colored icons (anti-pattern).
**Correct approach**: Platform icons rendered at `color: var(--text); opacity: 0.5` directly on the card surface. No background shape behind the icon.

**Checklist item**: Do any platform icons sit on colored backgrounds? If yes, remove the backgrounds.

---

### 1.3 Illustrations Instead of Product Visuals

**Problem**: Downloads page uses decorative illustrations (workspace scenes, device mockups with illustrations, abstract graphics) instead of product screenshots or app icons.
**Why it's wrong**: Design Philosophy item 4 — "Content as decoration — Product screenshots/output serve as hero visuals and brand texture; reject illustrations, abstract gradients, stock photos." Evidence: Notion uses a line illustration (decorative workspace scene), Discord uses colorful device mockup illustrations. These are brand-specific investments that agents cannot reproduce.
**Correct approach**: Use the product's app icon (Linear, Shade, Cursor — 3/21) or a product screenshot (Clay, Spline, 1Password — 3/21). If neither is available, use no visual at all (OpenAI, SpaceXAI, Windsurf, Giga, Height — 5/21 use no visual and still work).

**Checklist item**: Is the hero visual a product screenshot, app icon, or absent? No illustrations.

---

### 1.4 Box-Shadows on Platform Cards

**Problem**: Platform cards use `box-shadow` for depth or hover effects.
**Why it's wrong**: `shared/visual-style.md` section 5: "Zero shadows. No element on the entire site uses box-shadow." Hierarchy is established through background color steps.
**Evidence**: ClickUp uses subtle card shadows. This violates the system's shadow-free principle.
**Correct approach**: Cards use `background: var(--surface-1)` with no shadow. For hover, use `transform: translateY(-4px)` + `border-color: var(--text)` transition (card hover from system section 6).

```css
/* Correct */
.platform-card {
    background: var(--surface-1);
    border: 1px solid transparent;
    transition: transform 0.2s ease-in-out, border-color 0.3s linear;  /* system */
}
.platform-card:hover {
    transform: translateY(-4px);     /* card hover lift — system section 6 */
    border-color: var(--surface-2);
}
```

**Checklist item**: Does any card element use box-shadow? If yes, remove it.

---

### 1.5 Different Accent Colors per Platform

**Problem**: Each platform's download button uses a different accent color (blue for macOS, green for Android, orange for Windows).
**Why it's wrong**: The system uses a single accent color. `shared/visual-style.md` section 1: "Different accent colors for individual feature cards" is in the forbidden list. All buttons use `var(--accent)` / `var(--accent-text)`.
**Evidence**: 20/21 products use a uniform button color. Hermes Agent (brutalist style) is the sole exception.
**Correct approach**: All download buttons use `.btn-dark` with `var(--accent)`. Differentiation is through the label text and platform icon, not button color.

**Checklist item**: Do all download buttons use the same accent color?

---

### 1.6 Dropdown Menus for Architecture Selection

**Problem**: Architecture variants (Apple Silicon / Intel / x64 / ARM64) are hidden inside a dropdown menu on the download button.
**Why it's wrong**: Dropdowns add a click to the download flow. Architecture choice is a critical decision that should be visible. Evidence: Discord uses a dropdown chevron on the download button — but Notion, Cursor, TIDAL, and Windsurf all show architecture options as visible, separate buttons. Visible buttons reduce decision cost.
**Correct approach**: Show architecture variants as separate buttons or button-like rows. Each variant is a distinct, visible click target.

```
/* Correct — visible separate buttons */
[Download for macOS (Apple Silicon)]
[Download for macOS (Intel)]

/* Wrong — hidden in dropdown */
[Download for macOS v]
  > Apple Silicon
  > Intel
```

**Checklist item**: Are architecture options visible without opening a dropdown?

---

## 2. Content Errors

### 2.1 Fabricated Version Numbers or File Sizes

**Problem**: The Downloads page displays invented version numbers ("v4.2.1"), build numbers, or file sizes ("128 MB").
**Why it's wrong**: `shared/quality-checklist.md` prohibits fabricated metrics. Version and file size data must come from user input. Evidence: 19/21 products show no version number; 21/21 show no file size. These are metadata that change with every release and must be real.
**Correct approach**: Omit version numbers and file sizes unless the user explicitly provides them. If the user provides a version, display it. Never invent one.

**Checklist item**: Are all version numbers and file sizes user-provided or omitted?

---

### 2.2 "Get Started" or "Try Free" Instead of "Download"

**Problem**: The download button says "Get Started", "Try Free", "Start Now" instead of "Download" or "Install".
**Why it's wrong**: Downloads pages serve users who have already decided to get the product. The CTA should be direct and functional: "Download for macOS", not "Get Started." Evidence: 15/21 products use "Download" in the CTA. "Get Started" belongs on the Landing page, not the Downloads page.
**Correct approach**: Button text follows the pattern: "Download for [Platform]" or "Download [Product Name]" or simply "Download". For CLI tools: "Install" or the install command itself.

**Checklist item**: Does the primary CTA use "Download" or "Install" language?

---

### 2.3 Marketing Content on a Downloads Page

**Problem**: The Downloads page includes testimonials, feature tours, pricing comparisons, or conversion-oriented content below the download options.
**Why it's wrong**: Users on the Downloads page have already decided to download. Adding marketing content wastes their time and buries the download link. Evidence: 0/21 products include testimonials on the Downloads page. Only Craft and ClickUp include any feature content, and both are hybrid landing/download pages.
**Correct approach**: Downloads page content is strictly functional: heading, platform selection, download buttons, optional system requirements, optional version info. No testimonials, no pricing, no feature grids, no social proof.

**Checklist item**: Is the page free of testimonials, pricing, feature tours, and conversion CTAs?

---

### 2.4 Fabricated System Requirements

**Problem**: System requirements are invented ("Requires macOS 12.0 or later", "Windows 10 64-bit required") without user input.
**Why it's wrong**: System requirements are technical specifications that must be accurate. Incorrect requirements can prevent users from downloading (false restriction) or cause failed installs (false compatibility). Evidence: 16/21 products show no system requirements at all.
**Correct approach**: Show system requirements only when the user provides them. If not provided, omit entirely.

**Checklist item**: Are system requirements user-provided or omitted?

---

## 3. Structural Errors

### 3.1 Showing ALL Architectures Equally When Auto-Detect Is Available

**Problem**: All architecture variants (Apple Silicon, Intel, x64, ARM64, Universal) are displayed as equal-weight options without auto-detection, creating a wall of buttons.
**Why it's wrong**: Most users do not know their CPU architecture. Auto-detection removes the decision burden. Evidence: 11/21 products auto-detect the OS; Windsurf goes one level deeper and auto-detects OS + offers architecture choice immediately. Showing 6+ equal buttons (Notion: 5 buttons) creates decision paralysis for non-technical users.
**Correct approach**: Auto-detect the OS and present the primary CTA. Offer architecture choice as a secondary step (separate buttons below, or a "View all download options" link).

**Checklist item**: Is the primary CTA auto-detected with manual options as secondary?

---

### 3.2 Over-Engineering a Simple Downloads Page

**Problem**: Adding complex card grids, tab bars, version matrices, and architecture tables when the product only has 2-3 platforms.
**Why it's wrong**: A full version matrix (Cursor pattern) is appropriate for developer tools with 10+ build variants. For a product with macOS + Windows + Linux, it is unnecessary complexity. Evidence: OpenAI achieves the download with a single button; SpaceXAI uses 2 rows. Match complexity to platform count.
**Correct approach**: For 1-2 platforms: single CTA + compatibility note (Linear pattern). For 3-5 platforms: card grid or button stack (OpenPhone, Shade pattern). For 6+ platforms with architecture variants: tab bar (1Password) or version matrix (Cursor).

```
1-2 platforms:   Auto-detect CTA + text link for alternative
3-5 platforms:   Card grid or stacked buttons
6+ platforms:    Tab bar or grouped sections (Desktop / Mobile)
```

**Checklist item**: Does the page complexity match the number of platforms?

---

### 3.3 App Store/Google Play Badges as Primary Desktop CTAs

**Problem**: Using App Store or Google Play badge images as the primary download mechanism for desktop apps, or using badges for all platforms uniformly.
**Why it's wrong**: Store badges are appropriate for mobile apps (iOS, Android) but not for desktop direct downloads. Mixing badge styles (a rectangular store badge next to a standard `.btn-dark`) creates visual inconsistency. Evidence: 4/21 products use store badges — all exclusively for mobile platforms (ClickUp, Tailscale, Airtable, Craft). 0/21 use store badges for desktop.
**Correct approach**: Desktop platforms use `.btn-dark` or `.btn-outline` buttons with "Download for [Platform]" text. Mobile platforms may use store badges OR text buttons — but not both on the same card. Be consistent within the Desktop section and within the Mobile section.

**Checklist item**: Are store badges used only for mobile platforms?

---

### 3.4 Missing "Not Using [OS]?" Escape Hatch

**Problem**: Auto-detect CTA is shown, but no link or option exists for users on a different platform than what was detected.
**Why it's wrong**: Auto-detection is not infallible (VPNs, user-agent spoofing, browsing on a different device than download target). Users must always be able to reach the full platform list. Evidence: Windsurf ("Not using macOS? View all download options"), SpaceXAI ("More downloads"), Cursor ("View all download options") all provide escape hatches.
**Correct approach**: Below the auto-detect CTA, include a text link: "Not using [detected OS]? View all download options" or "Other platforms" styled as `.text-link` with `opacity: 0.5`.

**Checklist item**: Does the auto-detect CTA have a "view all platforms" escape hatch?

---

### 3.5 Alternating Section Background Colors

**Problem**: Hero uses white, platform list uses gray, mobile section uses white, creating a zebra stripe effect.
**Why it's wrong**: `shared/visual-style.md` section 8: "Not allowed: different background colors for different sections." At most 1-2 sections use `var(--surface-1)`. Downloads pages are typically so short (3-5 sections) that even 1 background switch is often unnecessary.
**Correct approach**: Default all sections to `var(--bg)`. Cards within sections use `var(--surface-1)`. The page background stays uniform.

**Checklist item**: Is the page background `var(--bg)` with at most 1 `var(--surface-1)` section?

---

## 4. When the User Provides a Brand Color

Adjustments when `--accent` is overridden with a brand color:

- **Download buttons** change from default (black/white) to the brand color via `var(--accent)` / `var(--accent-text)`. Standard `.btn-dark` behavior
- **1.1 does not relax**: No colored card backgrounds, even in the brand color
- **1.2 does not relax**: No colored icon backgrounds, even in the brand color. The accent allowed-use list is exhaustive
- **1.5 does not relax**: All download buttons use the same `var(--accent)`, not per-platform colors
- **1.4 does not relax**: Zero box-shadow, even for branded hover states. Use `transform: translateY(-1px)` + `filter: brightness()` per `shared/visual-style.md` section 10.1
- **Platform card backgrounds stay `var(--surface-1)`**: Do not tint cards with the brand color
- **Chromatic area < 10%** does not relax. On a Downloads page with 3-5 download buttons, the total accent area is already meaningful — do not add accent color to secondary elements
- **Compatibility notes and system requirements stay `opacity: 0.4`**: Do not color metadata text

---

## 5. Verification Checklist

After generating the Downloads page, verify the following:

1. **Do all platform cards share the same background color?** No per-platform gradients or colors
2. **Do any platform icons sit on colored backgrounds?** If yes, remove them
3. **Is the hero visual a product screenshot, app icon, or absent?** No illustrations
4. **Does any element use box-shadow?** If yes, remove it
5. **Do all download buttons use the same accent color?** No per-platform button colors
6. **Are architecture options visible?** Not hidden in dropdowns
7. **Are all version numbers and file sizes user-provided or omitted?** No fabricated metadata
8. **Does the primary CTA use "Download" or "Install" language?** Not "Get Started" or "Try Free"
9. **Is the page free of marketing content?** No testimonials, pricing, or feature tours
10. **Are system requirements user-provided or omitted?** No fabricated requirements
11. **Does the auto-detect CTA have an escape hatch?** "View all platforms" link present
12. **Does page complexity match platform count?** No over-engineering simple pages
13. **Are store badges used only for mobile platforms?** Not for desktop direct downloads
14. **Is the page background `var(--bg)` with at most 1 `var(--surface-1)` section?** No zebra striping
15. **Is the button border-radius 2px?** No pills (999px), no rounded buttons
