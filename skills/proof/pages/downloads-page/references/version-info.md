# Version Info — Design Knowledge

> Source: Mobbin research synthesis across 21 products' Downloads page version, requirements, and supplementary information sections

---

## Version Display

**When to show**:
- Developer tools where users pin to specific versions (Cursor)
- Products where version number is part of the brand identity (1Password 8)
- ~10% of observed products show version info (2/21); the majority do not

**When to skip**:
- Consumer apps (TIDAL, Notion, Discord) — users do not care about version numbers
- Products with auto-update — the version is always "latest"

**Execution**:

**Inline Version Badge** (next to heading or CTA — most common when present):
```css
.version-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;                             /* spacing scale */
}

.version-number {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    color: var(--text);
}

.version-latest {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    background: var(--surface-1);         /* #F5F5F5 (Light) / #141414 (Dark) */
    padding: 4px 8px;
    border-radius: 8px;                   /* feature card radius for small badges */
    /* Content: "LATEST" */
}
```

**Version in CTA text** (1Password pattern):
- CTA reads "Download [Product] [Version] for [Platform]" — e.g., "Download 1Password 8 for Mac"
- No separate badge needed; version is embedded in the button text

**Evidence**: Cursor (version badge + accordion), 1Password (version in CTA text)
**Evidence status**: Observed fact (2/21 products)

---

## System Requirements

**When to show**:
- Minimum OS version matters and could cause failed installs (Tailscale, Airtable, TIDAL, 1Password)
- Product has genuinely restrictive requirements (e.g., macOS Catalina 10.15+, not just "modern browsers")

**When to skip**:
- Product runs on all modern OS versions — ~76% (16/21) of observed products show no system requirements
- Web-only products — no system requirements apply

**Execution**:

**Inline below CTA** (most common placement):
```css
.sys-req {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-top: 12px;
    /* e.g., "REQUIRES MACOS CATALINA 10.15 OR LATER" */
    /* e.g., "REQUIRES WINDOWS 10+ (64-BIT)" */
}
```

**Per-Card Placement** (Airtable, Hermes, TIDAL pattern):
- System requirement appears inside each platform card, below the platform name or download button
- Uses the same `.platform-card-req` tokens defined in `platform-cards.md` Pattern 2

**Rules**:
- System requirements use mono label style (consistent with compatibility notes and architecture labels)
- Do not use a separate "System Requirements" section heading unless there are 5+ requirements (rare)
- Place inline with the relevant download action — users should see requirements before clicking

**Evidence**: Tailscale, Airtable, TIDAL, 1Password, Hermes (5/21 products show requirements)
**Evidence status**: Cross-sample inference

---

## Previous Versions / Archive

**When to show**:
- Developer tools with version-pinning needs (Cursor is the only observed example with a full archive)
- Products with beta/stable release channels

**When to skip**:
- Consumer apps — always download the latest version
- Products with auto-update and no rollback need (~90% of observed products)

**Execution**:

**Accordion Pattern** (Cursor pattern — most comprehensive observed):
```css
.version-archive {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.version-section {
    border-bottom: 1px solid var(--surface-2);  /* #E9E9E9 (Light) / #1F1F1F (Dark) */
}

.version-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 16px 0;                      /* spacing scale */
    cursor: pointer;
}

.version-header-title {
    display: flex;
    align-items: center;
    gap: 12px;
}

.version-header-name {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading */
    font-weight: 500;
    letter-spacing: -0.4px;
    color: var(--text);
    /* e.g., "Version 1.6" */
}

/* "Latest" badge reuses .version-latest from above */

.version-header-toggle {
    color: var(--text);
    opacity: 0.4;
    transition: transform 0.2s ease-in-out;
    /* Chevron icon, 16px. Rotates 180deg when expanded */
}
.version-header-toggle.expanded {
    transform: rotate(180deg);
}

.version-body {
    padding: 0 0 24px;
    /* Contains .platform-table or .platform-row items from platform-cards.md Pattern 3 */
    /* Latest version expanded by default; previous versions collapsed */
}
```

**Collapsed State**:
- Previous versions show only the version header row (version number + date)
- Clicking expands to reveal the full platform/architecture download grid
- Latest version is expanded by default; all others collapsed

**Expand/Collapse JS**:
```javascript
document.querySelectorAll('.version-header').forEach((header, index) => {
    const body   = header.nextElementSibling;
    const toggle = header.querySelector('.version-header-toggle');

    // Initial state: first (latest) version expanded; rest collapsed
    if (index === 0) {
        body.style.display = 'block';
        toggle.classList.add('expanded');
    } else {
        body.style.display = 'none';
    }

    // Make focusable for keyboard users
    header.setAttribute('tabindex', '0');
    header.setAttribute('role', 'button');
    header.setAttribute('aria-expanded', index === 0 ? 'true' : 'false');

    function toggle_() {
        const isExpanded = body.style.display !== 'none';
        body.style.display = isExpanded ? 'none' : 'block';
        toggle.classList.toggle('expanded', !isExpanded);
        header.setAttribute('aria-expanded', isExpanded ? 'false' : 'true');
    }

    header.addEventListener('click', toggle_);
    header.addEventListener('keydown', e => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); toggle_(); }
    });
});
```

**Evidence**: Cursor (versions 1.6, 1.5, 1.4, 1.3, 1.2 as collapsible sections)
**Evidence status**: Observed fact (1/21 products)

---

## Changelog Link / Cards

**When to show**:
- Product publishes regular release notes (developer tools, design tools)
- Changelog is a selling point (demonstrates active development)

**When to skip**:
- No public changelog exists
- Consumer apps where version changes are invisible to users

**Execution**:

**Simple Text Link** (most common):
```css
.changelog-link {
    /* Inherits .text-link */
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    transition: opacity 0.3s linear;
    margin-top: 16px;
    display: inline-block;
    /* e.g., "View release notes" or "See what's new in [Product]" */
}
.changelog-link::after { content: ' \2192'; }
.changelog-link:hover { opacity: 0.7; }
```

**Horizontal Changelog Cards** (Cursor pattern — more visual):
```css
.changelog-cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 24px;                            /* grid gutter */
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.changelog-card {
    padding: 24px;                        /* reduced from 32px — compact 4-column grid
                                             where standard padding would dominate card content */
    background: var(--surface-1);         /* #F5F5F5 (Light) / #141414 (Dark) */
    border-radius: 8px;                   /* feature card radius */
    /* zero shadow */
}

.changelog-card-version {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading */
    font-weight: 500;
    letter-spacing: -0.4px;
    color: var(--text);
}

.changelog-card-date {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-top: 6px;
    /* e.g., "JUNE 15, 2026" */
}

.changelog-card-summary {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    line-height: 1.6;
    margin-top: 12px;
    /* 1-2 sentence summary */
}
```

**Narrow screen**: `grid-template-columns: 1fr 1fr` at 767px, `1fr` at 480px.

**Evidence**: Cursor (4 changelog cards), 1Password ("See what's new" link)
**Evidence status**: Observed fact (2/21 products)

---

## Install Commands (Archetype C: Developer Distribution)

**When to show**:
- SDK, CLI tool, or library distributed via package manager (npm, pip, brew, apt)
- The install command IS the download action — no file download needed
- Developer audience that expects terminal-based installation

**When to skip**:
- GUI application with a standard installer (.dmg, .exe, .msi)
- Non-technical audience

**Execution**:

```css
.install-command {
    background: var(--surface-1);         /* #F5F5F5 (Light) / #141414 (Dark) */
    padding: 16px 24px;
    border-radius: 8px;                   /* feature card radius */
    display: flex;
    align-items: center;
    justify-content: space-between;
    max-width: 540px;                     /* subtitle measure — keeps command readable */
    margin: 0 auto;
}

.install-command code {
    font-family: var(--font-mono);
    font-size: 14px;                      /* button/nav scale */
    font-weight: 400;
    color: var(--text);
    line-height: 1.5;
    /* e.g., "$ npm install -g @heightapp/cli" */
    /* e.g., "$ pip install giga-sdk" */
    /* e.g., "$ brew install tailscale" */
}

.install-command .copy-btn {
    background: none;
    border: none;
    color: var(--text);
    opacity: 0.4;
    cursor: pointer;
    padding: 4px;
    transition: opacity 0.3s linear;
    /* Copy icon: clipboard SVG, 16px */
}
.install-command .copy-btn:hover {
    opacity: 1;
}
```

**Copy Button JS**:
```javascript
document.querySelectorAll('.copy-btn').forEach(btn => {
    const originalHTML = btn.innerHTML;         // save SVG before overwriting
    btn.addEventListener('click', () => {
        const code = btn.closest('.install-command').querySelector('code');
        const text = code.textContent.replace(/^\$\s*/, ''); // strip leading "$ "
        navigator.clipboard.writeText(text);
        btn.innerHTML = 'Copied';               // textContent = 'Copied' would also work here
        btn.style.opacity = '1';
        setTimeout(() => {
            btn.innerHTML = originalHTML;       // restore SVG icon (not textContent = '')
            btn.style.opacity = '';
        }, 2000);
    });
});
```

⚠️ Bug to avoid: `btn.textContent = 'Copied'` then `btn.textContent = ''` destroys the SVG permanently — `textContent` strips all child elements. Use `btn.innerHTML = originalHTML` to restore.

**Command format rules**:
- Always show `$` prompt prefix (non-selectable, opacity 0.4 via a `::before` pseudo-element or a separate `<span>`)
- One command per block — if multiple steps are needed, use multiple blocks or newlines
- Do not include `sudo` unless absolutely required
- Show the most common package manager first; offer alternatives as text below (e.g., "Or install via Homebrew: `brew install ...`")

**Inline Install Pill** (Giga pattern — command as a compact CTA):
```css
.install-pill {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--surface-1);
    padding: 8px 16px;                    /* button padding */
    border-radius: 2px;                   /* button radius */
    font-family: var(--font-mono);
    font-size: 14px;
    font-weight: 400;
    color: var(--text);
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
}
.install-pill:hover {
    transform: translateY(-1px);          /* button micro-lift */
}
```
The pill variant is used when the install command replaces the primary CTA button entirely — the command itself is the call to action. Clicking copies to clipboard.

**Evidence**: Height (code block + copy button), Giga (install pill as CTA)
**Evidence status**: Observed fact (2/21 products)

---

## Post-Download Content

These optional sections appear below the primary download area.

### Feature Highlights

**When to show**: When the Downloads page doubles as a product marketing page (Craft, Spline, Clay).

A brief 3-4 feature grid below the download section. Uses the same feature card tokens from the shared design system:
```css
.feature-card {
    padding: 32px;                        /* card internal padding */
    background: var(--surface-1);
    border-radius: 8px;                   /* feature card radius */
}
```
See `pages/landing-page/references/features.md` for full feature section knowledge.

### Alternative Download Methods

**When to show**: When both direct download and app store are available for the same platform (Craft, 1Password, Tailscale).

Display as secondary links below the primary CTA, not as competing CTAs:
```css
.alt-download {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    opacity: 0.5;
    transition: opacity 0.3s linear;
    margin-top: 12px;
    display: inline-block;
    /* e.g., "Also available on the Mac App Store" */
}
.alt-download:hover { opacity: 0.7; }
```

### Help Link

**When to show**: When architecture choice might confuse users (TIDAL: "Not sure? Find your chip.").

```css
.help-link {
    /* Same as .text-link */
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    text-decoration: none;
    transition: opacity 0.3s linear;
    /* e.g., "Not sure which version? Check your system" */
}
.help-link::after { content: ' \2192'; }
.help-link:hover { opacity: 0.7; }
```

**Evidence**: TIDAL ("Not sure? Find your chip."), Tailscale ("also on the Mac App Store")
**Evidence status**: Observed fact
