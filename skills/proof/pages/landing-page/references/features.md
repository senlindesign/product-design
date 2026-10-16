# Features Section — Design Knowledge

> Source: Mobbin research across 26 SaaS product Landing Page Features sections (2026-09-28)

---

## Pattern 1: Equal-Width Grid (Most Common)

**When to use**:
- 3–6 features of equal importance
- Each feature can be explained in 1–2 sentences
- Users need to quickly scan the full feature set

**Execution**:
- 3 columns × 2 rows (6 features) is the most common "sweet spot"
- Each cell: icon + title + description (1–2 sentences)
- Icons share a unified style and size; use brand color
- Cards are optional: bordered cards vs. borderless with spacing only. ⚠️ Shadowed cards are prohibited in this design system — use `border: 1px solid var(--surface-2)` or no border, never box-shadow
- On narrow screens, 3 columns collapse to 2 columns or single-column stacking

**Variants**:
- **Numbered grid**: replace icons with numbers (E/1, E/2...) (Lemon Squeezy) — conveys systematization and completeness
- **No-description grid**: icon + name, no description (Fibery with 16 features, Teak with 7) — suited for many features that are each self-explanatory
- **Dark competitor comparison**: dark background + quantified headlines (Railway: "40% cheaper", "50% faster") — directly benchmarks against competitors

**When not to use**:
- Features require a product screenshot to be understood → use image-text split
- More than 8 features → consider tab switching or a long list
- One core feature is far more important than the others → use Bento grid to highlight the primary feature

**Evidence**: Aboard, Jitter, Lemon Squeezy, Fibery, Railway, Loom, Cohere, PayPal
**Evidence status**: Cross-sample inference

---

## Pattern 2: Image-Text Split (Alternating Left-Right)

**When to use**:
- Features need product screenshots or illustrations to explain them
- 3–4 features, each requiring a deeper description
- Need to show real product UI

**Execution**:
- Each feature occupies one row: text (~40%) + screenshot / image (~60%)
- Alternate sides: first row text left, image right; second row image left, text right (creates visual rhythm)
- Text area contains: headline + description paragraph + optional "Learn more" link
- Screenshot uses real product UI, placed in a light container or window frame with `var(--surface-1)` background. No box-shadow — hierarchy via background color step

**Variants**:
- **No alternating**: all text left, image right (Square) — consistent but potentially monotonous
- **Embedded testimonial**: customer quote embedded at the bottom of the text area (Intercom) — provides social proof alongside the feature description
- **Tag list**: replace paragraph description with capsule tags (Ease) — more modern; suited for bullet-point-style explanations

**When not to use**:
- Features don't require visual aid
- Page is already very long (each row adds considerable height)

**Evidence**: Cycle, incident.io, Ease, Intercom, 1Password, Square
**Evidence status**: Cross-sample inference

---

## Pattern 3: Full-Width Product Screenshot

**When to use**:
- The product UI is itself the best feature explanation
- Users need to see the real interface density and data display
- Features are centered on one core interface

**Execution**:
- Above: headline + description + CTA button (centered)
- Below: full-width product screenshot with window-frame effect or light container
- Screenshot shows real data (not empty state), including a complete view with multiple panels / windows
- Optional: floating cards, multi-device side-by-side to add depth

**Variants**:
- **Tab switching**: a horizontal tab bar switches between screenshots of different features (ClickUp) — suited for platforms with many features
- **Multi-device**: desktop + mobile screenshots side by side (incident.io) — showcases cross-platform capability
- **Bento mix**: one large screenshot + multiple smaller cards (FLORA) — highlights the core feature, with secondary features alongside

**When not to use**:
- Product UI isn't visually polished, or data is sensitive
- Product is an API / back-end tool with no displayable UI

**Evidence**: Craft, ClickUp, Amplemarket, mymind, FLORA
**Evidence status**: Cross-sample inference

---

## Key Design Decisions

### Feature Count vs. Layout Choice
| Count | Recommended layout | Reason |
|-------|--------------------|--------|
| 3 | Three-column horizontal or image-text split | Each feature can go deep |
| 4 | 2×2 grid or image-text split | Balance depth and breadth |
| 6 | 3×2 grid | Most common sweet spot |
| 8+ | Tab switching or grouped list | Avoids excessive page length |
| 12+ | No-description list or categorized tabs | Only for feature-dense platforms |

### Visual Element Choice
| Element | When to use | When not to use |
|---------|-------------|-----------------|
| Brand-color icons | Feature concept is clear; no screenshot needed | Feature requires visual proof |
| Product screenshots | Product UI is attractive; feature needs to be "seen" | Early product; UI unstable |
| Real photos | Product has physical touchpoints (POS, hardware) | Pure software products |
| Abstract geometric icons | Enterprise / AI product; conveys technical feel | Consumer-facing lightweight tools |
| No visual element | Headlines are already self-sufficient (numbers as substitute) | Feature concept is not intuitive |

### Copywriting Frameworks
| Framework | Description | When to use | Example |
|-----------|-------------|-------------|---------|
| **Feature-oriented** | "What we have" | Default choice | "Account management", "AI documentation" |
| **User-oriented** | "What you can do" | User as subject | "Accept online payments", "Generate strong passwords" |
| **Competitor comparison** | "Better than X in what way" | There is a clear competitor to displace | "40% cheaper [than Heroku]" |
| **Value proposition** | "No limits / everything ready" | Emphasize frictionlessness | "No limits on seats", "Just enough to get things done" |

### Icons vs. No Icons
- **Use icons** (~70%): improves scannability and provides visual anchor. Icons must share a unified style
- **No icons** (~30%): when headlines are already clear, numbers or whitespace replace them. Cleaner but less scannable
- Never use generic / vague icons (gears, lightbulbs) — if you can't find a meaningful icon, it's better to use none

### Number of Features Sections
A page can have multiple Features sections:
- **Primary Features**: 3–6 core features, shown in detail
- **Supplementary Features**: 8–16 secondary features, list-style display (Fibery "Some more of our features")
- **Enterprise Trust Features**: 3 high-level concepts (Security / Scalable / Customizable), aimed at decision-makers

Different-tier Features sections use different layouts to avoid visual repetition.
