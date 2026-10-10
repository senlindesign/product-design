# Anti-Patterns & AI Convergence Traps

> Source: Competitive Skill research (Anthropic, bear2u, 2389 Research, Impeccable) + Mobbin research observations (2026-09-28)

---

## 1. Five Visual Convergence Traits of AI-Generated Pages

Source: Convergence patterns explicitly named in Anthropic's frontend-design Skill.

| Convergence trait | Description | Alternative direction |
|-------------------|-------------|----------------------|
| **Cream + Terracotta** | Beige background + terracotta / warm brown tones. AI's default "warm professional" palette | Derive color from the product's actual industry / material / vocabulary. Tool-type products don't need "warmth" |
| **Dark + Neon** | Dark background + neon accent color. AI's default "tech feel" palette | Not all tech products need neon. incident.io uses red-orange, Retool uses white-green — both dark but with brand personality |
| **Broadsheet Layouts** | Newspaper-like multi-column large-headline layouts. AI's default for "designerly" output | Layouts should serve content structure, not decoration. Three columns only when three equally weighted pieces of content exist |
| **SaaS Cards** | A row of rounded cards + icon + title + description. The most common AI feature-display approach | Feature display has many forms: large image + alternating text, bento grid, accordion, left-right split. Choose based on content |
| **Template Chrome** | Generic semi-transparent navigation, generic gradients, stock pattern backgrounds | Every design decision should trace back to a concrete characteristic of the product or brand |

**How to check**: After generating a page, ask "What specific characteristic of this product justified this color / layout / component choice?" If you can't answer, it may be a convergence default.

---

## 2. Common Implementation Errors

Source: bear2u's avoidance list + counter-example comparisons observed in Mobbin research.

### Typography
- **Avoid**: using the same font family throughout with hierarchy created only by weight changes. This is the most common AI typography pattern
- **Alternative**: use font family switching for hierarchy (display sans + mono label + body sans), weight locked to 500. See `visual-style.md` §2
- **Avoid**: all text at the same size or only 2 levels of hierarchy
- **Alternative**: Hero 80px → Section 47px → Feature 27px → Card 20px → Body 18px → Label 12px
- **Avoid**: headline letter-spacing of 0 or a positive value. Professional typographic headlines always use negative tracking (approximately −2% of the font size)

### Color (Chromatic Silence Principle)
- **Avoid**: any chromatic color occupying more than 10% of the page area. Default CTA uses `var(--accent)` (default = black / white)
- **Avoid**: using grays with a hue shift (slate #64748B, zinc #71717A, cool gray). Must use pure achromatic gray + opacity
- **Avoid**: using different background colors for different sections — this is the primary source of template-patchwork feel
- **Avoid**: adding chromatic decoration to icons / cards (colorful circular backgrounds, gradient strips, colored borders)
- **Avoid**: gradient CTA buttons, semi-transparent colorful overlays, glow effects
- **Avoid**: box-shadow. Zero shadow across the entire site; hierarchy built through background-color steps
- **Reference**: strictly follow the color system and shadow system in `shared/visual-style.md`

**When the user provides a brand color**:
- ✅ CTA changes from black / white to brand color (`--accent`) — this is normal behavior and does not violate Chromatic Silence
- ✅ Brand color is a product characteristic; using it passes the "design choice traces to product characteristic" test
- ❌ The <10% area rule is not relaxed
- ❌ Icon colorful backgrounds, section colorful backgrounds, gradients are still prohibited
- ❌ Brand color does not spread to surface / border / text — only used for elements in the `--accent` allowlist

### Layout
- **Avoid**: generic centered three-column cards as the default for every section
- **Alternative**: Bento grid (3 columns + featured spanning 2 columns), alternating image-text rows, step list. Choose based on content
- **Avoid**: inter-section spacing < 180px. AI defaults produce spacing that is too tight
- **Avoid**: stock photos as Hero images. Product screenshots / code / work are the visuals (Content-as-Chrome principle)

### Content
- **Avoid**: fabricating customer quotes or statistics. The brief explicitly requires no fake testimonials or fake metrics
- **Avoid**: "Get Started" as the CTA for every instance. Real products adjust based on context: Hero uses "Start free", Features uses "Learn more", bottom CTA uses "Try [Product] today"
- **Avoid**: describing features with vague adjectives like "Powerful", "Seamless", "Cutting-edge". Use specific feature nouns instead

---

## 3. Structural Anti-Patterns

### Overstacking
- **Problem**: adding every section (Hero + Features + How It Works + Social Proof + Pricing + FAQ + CTA + Footer) regardless of whether the product needs them
- **Check**: does each section have independent informational value? Is the page still complete without it?
- **Principle**: section count should be content-driven, not template-driven

### Repetitive Expression
- **Problem**: Hero, Features, and CTA all repeat the same value proposition
- **Check**: does the same information appear more than 2 times in the page?
- **Allowed**: CTAs may repeat (above fold + bottom), but copy should vary

### Lack of Rhythm
- **Problem**: all sections have identical spacing, identical widths, identical layout patterns — the page looks like an infinitely long list
- **Check**: do more than two consecutive sections use exactly the same layout pattern?
- **Alternative**: build section-feel through spacing variation, layout variation (centered → split → full-width), and font-size hierarchy variation. Background color stays consistent; only subtle grayscale differences are permitted (#FFF → #FAFAFA)
- **Note**: do not use large areas of different colorful backgrounds to distinguish sections — this is the primary source of template-patchwork feel

### Fake Interaction
- **Problem**: buttons, tabs, or filters have visual styling but no interaction behavior
- **V1 handling**: in delivery notes, declare which elements are visual display only and which have actual functionality. Don't let visual cues imply non-existent functionality

---

## 4. Knowledge Usage Anti-Patterns

### Template Application
- **Problem**: treating knowledge entries as a mandatory checklist to follow regardless of the specific needs of the current task
- **Principle**: every knowledge entry has conditions for applicability. When conditions are not met, choose a different pattern rather than force-fitting
- **Check**: when using a pattern, can you explain why it is suited for the current product / content / audience?

### Ignoring Input
- **Problem**: the user provided brand colors, copy, images, etc., but the generated page doesn't reflect them
- **Principle**: user-specified directions take priority over default recommendations in the knowledge base (from Anthropic Skill: "Honor briefs over patterns")

### Over-Engineering
- **Problem**: adding unnecessary complexity to showcase knowledge
- **V1 principle**: use a simple approach when a simple one works. A 3-column feature card layout is easier to implement than a bento grid and is good enough in most cases
