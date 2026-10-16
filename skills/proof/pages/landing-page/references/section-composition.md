# Section Composition Rules

> Source: Section arrangement patterns observed in Mobbin research across 30+ SaaS Landing Pages (2026-09-28)

---

## 1. Recommended Section Order

Basic order (top to bottom):

```
Navigation (fixed)
    ↓
Hero (fixed)
    ↓
[Logo wall / trust signal] (optional — place immediately after Hero if present)
    ↓
Features / core value display (nearly required)
    ↓
[How It Works] (optional)
    ↓
[Social Proof / customer testimonials] (optional)
    ↓
[Pricing preview] (optional)
    ↓
[FAQ] (optional)
    ↓
Bottom CTA (recommended)
    ↓
Footer (fixed)
```

**Fixed-position sections**: Navigation at the very top, Hero immediately after, Footer at the very bottom. These three should not be moved.

**Highly flexible sections**: The order of Features, How It Works, and Social Proof can be adjusted based on content.

---

## 2. Dependencies Between Sections

| Section A | Depends on Section B | Reason |
|-----------|---------------------|--------|
| FAQ | No strong dependency | But if there's a Pricing preview, FAQ typically comes after Pricing (addresses pricing questions) |
| How It Works | Features (recommended before) | Features first explains what the product can do; How It Works explains how to do it |
| Bottom CTA | Hero CTA (recommended to match) | First and last CTA echo each other, but copy can differ (bottom is more direct) |
| Social Proof | Features (recommended after) | Show functional claims first, then support them with evidence |

---

## 3. Conflict Detection Between Sections

### Information Repetition
| Conflict | Description | Solution |
|----------|-------------|---------|
| Hero vs. Features | Hero headline already lists feature points; Features repeats them | Hero focuses on a single value proposition; Features expands on specific functionality |
| Social Proof vs. Hero | Hero already has a logo wall; a separate Social Proof section also exists below | When logo wall is in the Hero bottom, Social Proof section uses a different form (e.g., customer quotes rather than logos) |
| How It Works vs. Features | Both talk about "what the product does" | How It Works focuses on process / steps; Features focuses on capabilities / value |
| CTA repetition | CTA buttons after every section | Limit standalone CTAs to 2–3 places: Hero + [optional middle] + Bottom CTA |

### Visual Conflict
| Conflict | Description | Solution |
|----------|-------------|---------|
| Multiple full-width dark sections | Consecutive dark backgrounds make the page heavy | Insert a light section between dark sections |
| Multiple grid / card sections | Features use cards, Social Proof uses cards, Pricing also uses cards | At least one section uses a different layout (alternating image-text, list, large image + text) |
| Equal visual weight everywhere | Every section has the same size headline and same spacing | Establish hierarchy: core sections get larger headlines and more spacing |

---

## 4. Visual Rhythm Rules

### Background Color Alternation
Recommended background color rhythm pattern:

```
Navigation: white / transparent
Hero: white or dark (depends on archetype)
Logo wall: white (same as Hero or light transition)
Features: light gray or white
How It Works: white (if Features is light gray)
Social Proof: var(--surface-1) or var(--bg)
Bottom CTA: .section-dark (var(--text) background — no brand color as section fill)
FAQ: white
Footer: dark or dark gray
```

**Core principle**: never have 3 or more consecutive sections with the same background color.

### Spacing Rhythm
- **Hero to first section**: larger spacing (Hero is its own visual focal point)
- **Consecutive Features sections**: medium spacing
- **CTA section**: top and bottom spacing can be larger than typical sections (creates a "pause")
- **Before Footer**: clear separation (background color change or dividing line)

---

## 5. Minimum Viable Page vs. Full Page

### Minimum Viable Page (4–5 sections)
Suitable for: limited content, quick prototype, early-stage product

```
Navigation → Hero → Features (3–4) → CTA → Footer
```

### Standard Page (6–8 sections)
Suitable for: has customer data, has pricing, product is mature

```
Navigation → Hero → Logo wall → Features → Social Proof → CTA → FAQ → Footer
```

### Full Page (8–10 sections)
Suitable for: rich content, complex product, high conversion goal

```
Navigation → Hero → Logo wall → Features → How It Works → Social Proof → Pricing → FAQ → CTA → Footer
```

**Do not exceed 10 sections** — an overly long page dilutes the impact of each section.

---

## 6. Decision Guide for Adding / Removing Sections

### When to Add
| Section | Condition for adding |
|---------|---------------------|
| Logo wall | Have 4+ displayable customer / partner logos |
| How It Works | Product has a 3+ step usage flow, or new users wouldn't intuitively know how to start |
| Social Proof | Have genuine customer quotes, ratings, or case stories |
| FAQ | Have 4+ common questions, or pricing / policies need explanation |
| Pricing preview | Have clear pricing plans and page goal includes conversion |

### When to Remove
| Section | Condition for removing |
|---------|----------------------|
| How It Works | Product usage is intuitively obvious (e.g., "sign up in one click and it's ready to use") |
| Social Proof | No genuine customer data. Do not fabricate |
| FAQ | Fewer than 3 questions, or questions can be answered within other sections |
| Pricing | Pricing requires consultation or isn't discussed on this page |
