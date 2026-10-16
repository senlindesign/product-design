# Downloads Page Archetypes & Selection Guide

> Source: Mobbin research synthesis across 21 unique products, 42 section observations (2026-10-02)

---

## Archetype Definitions

### A. Platform Selector (Default)

**Typical products**: Linear, Shade, Notion, Cursor, Tailscale, 1Password, Spline, Windsurf, TIDAL, OpenPhone, Craft, Clay, Airtable, SpaceXAI/Grok
**Core characteristic**: Single product available on multiple platforms/architectures; the page's job is to match the user to the right build

**When to use**:
- Product is a single application (not a product suite)
- Available on 2+ platforms (macOS, Windows, Linux, iOS, Android, Web)
- User has already decided to download — no persuasion needed
- Desktop app is the primary distribution (not an SDK, CLI tool, or browser extension)

**Section composition** (3-5 sections):
1. Nav (shared, fixed, frosted glass)
2. Hero / Header (product icon or screenshot + heading + auto-detect CTA + compatibility note)
3. Platform List (manual platform selection: buttons, cards, rows, or tabs)
4. [Optional: Mobile section — separated from Desktop when both exist]
5. Footer (shared)

**Key differentiators**:
- Auto-detect OS for primary CTA (11/21 products use auto-detection)
- Secondary platform options below the fold
- Single viewport page — most Archetype A pages fit entirely above the fold or within one scroll
- No marketing content below the download options (user is already committed)

**Visual tendencies**:
- Dark theme slightly more common (11 dark vs 10 light across all observations)
- App icon as hero visual (Linear, Shade, Cursor) or product screenshot (Clay, Spline, 1Password)
- Minimal decoration — 5/21 products use no visual at all (OpenAI, SpaceXAI, Windsurf, Giga, Height)

---

### B. Multi-Product

**Typical products**: ClickUp, 1Password Dev, Frontify
**Core characteristic**: Multiple distinct downloadable apps, tools, or extensions from one company; the page is a product catalog, not a single download funnel

**When to use**:
- Company ships multiple distinct products or tools (mobile app + desktop app + browser extension + CLI)
- Products have different target audiences (end users vs developers)
- Each product has its own download method (direct download vs App Store vs package manager)
- The page heading is "Apps" or "Downloads" (plural), not "Download [Product Name]"

**Section composition** (4-6 sections):
1. Nav (shared, fixed, frosted glass)
2. Header ("APPS" mono label + heading)
3. Featured Products (2-column cards for primary products: Desktop + Mobile)
4. Secondary Products (3-column cards for extensions, integrations, add-ons)
5. [Optional: Developer Tools section — separate card grid for CLI, SDKs, APIs]
6. Footer (shared)

**Key differentiators**:
- Card-per-product layout (not card-per-platform)
- Each card contains its own platform-specific download buttons or store badges
- Product mockup/screenshot within each card
- Mix of download methods: direct download buttons, App Store / Google Play badges, "Install" for extensions

**Visual tendencies**:
- Light theme dominant (2/3 observations are light)
- Product screenshots inside cards (ClickUp desktop card, Frontify mockups)
- Cards may differ in size (ClickUp: Desktop card is larger than Extension cards)

---

### C. Developer Distribution

**Typical products**: Giga, Height, Cursor (version archive section)
**Core characteristic**: CLI tools, SDKs, packages, or developer utilities where the install command IS the download; platform selection is handled by the package manager, not the user

**When to use**:
- Product is primarily a CLI tool, SDK, or library
- Installation method is a terminal command (`pip install`, `npm install`, `brew install`)
- Target audience is developers who are comfortable with terminal
- Version archive or changelog is more important than platform selection

**Section composition** (3-5 sections):
1. Nav (shared, fixed, frosted glass)
2. Hero / Header (heading + install command in code block + copy button)
3. [Optional: IDE Extension — split layout with extension install button]
4. [Optional: Version Archive — version-grouped platform/architecture matrix]
5. [Optional: Feature summary — brief feature grid below install command]
6. Footer (shared)

**Key differentiators**:
- CLI install command as the primary CTA (dark code block with mono font + copy button)
- No platform selection UI — the package manager is cross-platform
- Version numbers, architecture labels, and package format labels are prominent metadata
- Changelog or release notes link is a natural companion

**Visual tendencies**:
- Dark theme preferred (developer tool archetype from `shared/visual-style.md` section 11.C)
- Code block is the visual anchor — `var(--surface-1)` background, mono font
- Minimal or no product visual — the command IS the visual
- License info may appear near the install command (Giga: "MIT license")

---

## Cross-Archetype Rules

Regardless of archetype:

1. **Users have already decided to download.** Do not add marketing content, testimonials, pricing, or feature tours. The Downloads page is a utility page, not a persuasion page. Evidence: 0/21 products include testimonials; only Craft and ClickUp include any feature content below the download area, and both are hybrid pages
2. **Nav and Footer are shared.** Same nav and footer as all other page types. Reuse `shared/navigation.md` and `shared/footer.md`
3. **Heading is direct.** "Download [Product Name]" / "Get [Product Name]" / "Download" — not "Get started" or "Try free". Evidence: 15/21 products use some form of "Download" in the heading or CTA
4. **Auto-detect when possible.** 11/21 products auto-detect the user's OS for the primary CTA. When auto-detection is used, always provide a "View all platforms" or "Not using [OS]?" link for manual selection
5. **Version and file size are usually omitted.** 19/21 products show no version number; 21/21 show no file size. Include version info only for developer tools (Archetype C) or when explicitly provided
6. **System requirements are optional.** 16/21 products show no system requirements. Include only when provided by the user or when specific OS versions matter (e.g., "Requires macOS 12+" for Apple Silicon)

---

## Decision Matrix

```
1. Is the product a CLI tool, SDK, or package installed via terminal?
   +-- Yes --> C. Developer Distribution
   +-- No
       +-- Does the company ship multiple distinct downloadable products?
       |   +-- Yes --> B. Multi-Product
       |   +-- No --> A. Platform Selector (default)
       +-- Uncertain --> A. Platform Selector (default)

2. After choosing an archetype, adjust sections based on available content:
   - Has both desktop and mobile apps?  --> Add separate Mobile section (A only)
   - Has version history to display?    --> Add Version Archive section (C only)
   - Has IDE extension alongside CLI?   --> Add IDE Extension split (C only)
   - Has browser extensions/add-ons?    --> Add Secondary Products grid (B only)
   - Has < 3 platforms?                 --> Simplify to stacked buttons, skip card grid
   - Has > 5 architectures per platform? --> Use version matrix table (Cursor pattern)
```

---

## Section Presence by Archetype

| Section | A. Platform Selector | B. Multi-Product | C. Developer Distribution |
|---------|---------------------|------------------|--------------------------|
| Hero / Header | Required (auto-detect CTA) | Required (catalog heading) | Required (install command) |
| Platform List | Required | Skip (per-product buttons instead) | Optional (version matrix) |
| Product Cards | Skip | Required (card per product) | Skip |
| Mobile Section | Optional (when both desktop + mobile exist) | Handled within cards | Skip |
| Version Archive | Skip | Skip | Optional |
| IDE Extension | Skip | Skip | Optional |
| Feature Summary | Skip | Skip | Optional (brief) |
| CTA section | Skip (the download IS the CTA) | Skip | Skip |

---

## Platform Selection Patterns (from observations)

| Pattern | Observation count | Best for |
|---------|------------------|----------|
| Auto-detect CTA + manual list below | 11 | Archetype A with 3+ platforms |
| Equal-weight cards/buttons | 8 | Archetype A with 2-4 platforms, Archetype B |
| CLI install command | 2 | Archetype C |
| Tab bar switching | 2 (1Password, Spline) | Archetype A with 5+ platforms |
| Text links | 2 (Frontify, Miro) | Archetype B as part of a larger page |

### Auto-Detect CTA Pattern (Recommended Default for Archetype A)

```
[Icon or product visual]
"Download [Product Name]"                        -- heading
"Available for macOS, Windows, and Linux"         -- subtitle, opacity: 0.5
[Download for macOS]                              -- .btn-dark, auto-detected OS
"Compatible with Apple Silicon and Intel"         -- compatibility note, opacity: 0.4
```

Evidence: Linear, Spline, Windsurf, Cursor, Craft, Tailscale, SpaceXAI all use this pattern.

### Architecture Variant Handling

When a platform has multiple architectures (Apple Silicon vs Intel, x64 vs ARM64):

- **Separate buttons** (most common): Notion, Cursor, TIDAL, Windsurf — each architecture gets its own button
- **Compatibility note** (minimal): Linear ("Compatible with Apple Silicon and Intel") — single button, note below
- **Architecture in card label**: Shade, Spline — label within the card identifies the variant

Recommendation: Use separate buttons when > 2 architectures exist. Use a compatibility note when the installer is universal or auto-detecting.
