# Footer Section — Design Knowledge

> Source: 28 SaaS product Landing Page Footer studies via Mobbin (2026-09-28)

---

## Pattern 1: Multi-Column Links + Newsletter

**When to use**:
- Product has multiple feature areas or pages that need to be exposed
- Want to collect user emails (newsletter / product updates)
- 15-30 total links

**Implementation guidance**:
- 3-5 link columns, 4-8 items per column
- Column titles bolded or uppercase, visually distinct from link text
- Newsletter area placed on the right or at the bottom: email input + submit button
- Newsletter typically needs only 1 field (Email); B2B may add name/company fields
- Bottom row: copyright + legal links (Terms, Privacy) + social icons

**Column naming suggestions**:
| Column name | Suitable content |
|------------|-----------------|
| Product / Platform | Core feature pages |
| Solutions / Use Cases | Organized by scenario or industry |
| Resources | Blog, Docs, Help Center, Changelog |
| Company | About, Careers, Contact, Press |
| Legal | Terms, Privacy, Security |

**Variants**:
- **Developer products**: add Docs, API Reference, Status links; may omit Newsletter
- **Multi-product lines**: columns organized by product line instead of function (Bird: Reach / Grow / Manage / Automate)
- **Organized by user role**: columns organized by target user (Kit: Artists / Authors / Bloggers / Podcasters)

**Evidence**: Zendesk, Bird, Dovetail, Maze, Ditto, Spade, Employment Hero, Patch
**Evidence status**: Cross-sample inference

---

## Pattern 2: Pre-footer CTA + Minimal Links Area

**When to use**:
- Page bottom needs a strong conversion close
- Already has a separate Bottom CTA section, or wants to merge CTA with Footer
- Brand tone allows bold visual expression

**Implementation guidance**:
- Divided into two visual zones:
  1. **CTA zone**: large heading + CTA button, high visual weight (dark or brand-colored background)
  2. **Footer zone**: minimal link columns + copyright info
- CTA zone heading can be a brand statement or call to action
- CTA button echoes the Hero CTA but copy can be more direct
- Footer zone maintains practical navigation function, no need to repeat the CTA

**Variants**:
- **Giant text CTA**: CTA heading uses oversized font dominating the viewport (Current: "Start for free" in yellow-green)
- **Brand-colored CTA band**: vivid brand color strip separating content area from Footer (Pinterest: yellow "Ready to build?")
- **Dual-path CTA**: simultaneously offers two conversion paths (FLORA: "Book a call" + "Sign up for free")

**When not to use**:
- Page already has a separate Bottom CTA section — would cause duplication
- Page is short (4-5 sections) and CTA is already adequately covered in the Hero

**Evidence**: Current, Pinterest Dev, OpenTable, The Leap, Podia, Notion, Luma, FLORA
**Evidence status**: Cross-sample inference

---

## Pattern 3: Giant Brand Wordmark

**When to use**:
- Strong brand visual identity, want to close the page with the brand
- Design-driven product
- Can be combined with Pattern 1 or 2

**Implementation guidance**:
- Place an oversized brand name wordmark at the bottom of the Footer
- Wordmark can be high contrast (white text on black background) or low-contrast semi-transparent
- Wordmark can be fully visible or partially cropped (only the top half showing)
- Link area stays above the wordmark

**Evidence**: Maze, Ditto, Popcorn, Cosmos, Melius, CTRL
**Evidence status**: Cross-sample inference

---

## Pattern 4: Minimal Single Row

**When to use**:
- Small number of links (< 12)
- Simple product line
- Overall minimalist page design

**Implementation guidance**:
- All links arranged horizontally in 1-2 rows
- No column structure; separated by spacing or dividers
- Logo can be on the left or omitted
- Social links use text rather than icons

**Evidence**: Chronicle, Metalab, Luma
**Evidence status**: Observed

---

## Key Design Decisions

### Background Color Choice
| Background | Observed proportion | Guidance |
|-----------|---------------------|----------|
| Dark/black (`var(--text)` band) | ~45% | High contrast, signals end of page. When used, wrap in `class="section-dark"` so text and buttons invert correctly |
| White/light (`var(--bg)`) | ~40% | Consistent with a light page. Add a `border-top: 1px solid var(--surface-2)` to visually separate from body |
| Brand color | ~15% observed | **Not recommended in this design system** — `visual-style.md` §1 restricts `--accent` to CTA buttons and 1-2 secondary uses. A brand-colored footer background would exceed the <10% chromatic area limit |

**Default recommendation**: light theme → `var(--bg)` with `border-top: 1px solid var(--surface-2)`; dark theme → `var(--surface-1)`, a one-step lift that signals the page has ended. A dark band (`var(--text)` via `.section-dark`) is an option on **light** pages only — on a dark page `var(--text)` is the light text color, so the band would turn into a light footer. `.section-dark` is a Minimal technique; in other styles, use the active style file's own section-background rules. Never use brand color as a full footer background.

### Link Count
- **< 10**: Minimal Footer (Chronicle, Luma) — simple or early-stage product
- **15-25**: Standard Footer (most SaaS) — 3-4 columns
- **30+**: Large enterprise Footer (Zendesk, Rox, Kit) — 5+ columns, suited for multi-product lines

### Social Icons
- Common platforms: Twitter/X, LinkedIn, Instagram, YouTube (4 most common)
- Developer products add: Discord, GitHub
- Young/creator products add: TikTok
- Icons vs. text links: icons more common (~70%), text links more minimalist
- Icon source: Simple Icons in one color (`https://cdn.simpleicons.org/<slug>/<hex>`, e.g. `x`, `linkedin`, `github`, `discord`, `youtube`, `instagram`) or an icon MCP — never drawn. See *Real logos only* in the master SKILL.md

### Legal/Compliance Elements
- Must include: copyright notice, Terms of Service, Privacy Policy
- Optional: Cookie settings (GDPR compliance), Accessibility, SOC-2 certification
- International products: language selector
- Region-specific: Indigenous acknowledgment statement (Australia), full address (B2B trust)

### Newsletter Form Complexity
- **1 field** (Email only): most SaaS. Minimizes signup friction
- **2 fields** (Name + Email): Patch style. Slightly more personalization
- **4 fields** (Name + Company + Email + other): Bird style. B2B sales-oriented, high friction but high-quality leads
- If the page already has a Bottom CTA section with a signup form, Footer does not need to repeat it

### Relationship with CTA Section
- If the page has a separate Bottom CTA section (see [[cta]]), Footer maintains pure navigation function
- If there is no separate CTA section, Footer can take on the conversion function (Pattern 2)
- Avoid CTA section + Pre-footer CTA appearing simultaneously — information duplication

---

## CSS Tokens (required — quote these verbatim, do not author independently)

These values are the source of truth for all Page Skills and Section Skills that render a footer.

```css
/* Footer spacing */
footer {
    padding-top: 128px;             /* distance from the last section to footer content */
    padding-bottom: 48px;           /* below the copyright bar — visual-style.md §3 */
}

/* Inner container — aligns with section content edges */
footer > .container {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

/* Link columns */
.footer-columns {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    gap: 24px;                      /* between columns */
    margin-bottom: 58px;            /* columns → bottom bar */
}

.footer-col-title {
    font-family: var(--font-mono);  /* same label treatment as the rest of the system */
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 16px;            /* column title → first link */
}

.footer-col-links {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: column;
    gap: 12px;                      /* between stacked links in a column */
}

.footer-col-links a {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 400;               /* body weight for footer links */
    color: var(--text);
    opacity: 0.5;
    text-decoration: none;
    transition: opacity 0.3s linear;
}
.footer-col-links a:hover { opacity: 1; }

/* Bottom bar (copyright + legal + social) */
.footer-bottom {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-top: 32px;
    border-top: 1px solid var(--surface-2);
}

.footer-copyright {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.2;                   /* copyright = weakest tier */
}

.footer-social {
    display: flex;
    align-items: center;
    gap: 16px;                      /* between social icons */
}

.footer-social a {
    color: var(--text);
    opacity: 0.4;
    transition: opacity 0.3s linear;
}
.footer-social a:hover { opacity: 1; }

/* Dark footer variant — wrap the entire <footer> in class="section-dark" */
/* .section-dark is defined in visual-style.md §8 — it sets bg + text-inverse */

/* Narrow screen */
@media (max-width: 767px) {
    footer { padding-top: 80px; }   /* 128px → 80px per narrow-screen table */
    footer > .container { padding: 0 20px; }
    .footer-columns { grid-template-columns: 1fr 1fr; gap: 32px; margin-bottom: 40px; }
    .footer-bottom { flex-direction: column; gap: 16px; text-align: center; }
}
```
