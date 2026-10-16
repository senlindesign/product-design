# Timeline Section — Milestones and Company History

> Source: Mobbin research synthesis from 6 timeline observations across Lightdash, Apollo (2 variants), Going, ClickUp, V7.

---

## Default Pattern: Vertical Alternating Timeline

No single dominant pattern exists for timelines (the most visually varied section type). The vertical alternating timeline (Lightdash pattern) is the recommended default because it works with or without images, scales to any number of milestones, and is fully responsive without JavaScript. Horizontal timelines (3/6 samples) require carousel JS for overflow, which is outside V1 scope for complex variants.

### Section Heading

```css
.timeline-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading — type scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    text-align: center;
    margin-bottom: 58px;                  /* heading-to-content — spacing system */
}
```

Common heading text: "Our Story", "Our Story So Far", "Milestones".

---

## Vertical Alternating Timeline Implementation

### Container and Center Line

```css
.timeline {
    position: relative;
    max-width: 1080px;                    /* system grid max-width */
    margin: 0 auto;
    padding: 0 32px;                      /* system side padding */
}

.timeline::before {
    content: '';
    position: absolute;
    left: 50%;
    top: 0;
    bottom: 0;
    width: 2px;                           /* page-specific: timeline line thickness */
    background: var(--surface-2);         /* divider color from system */
    transform: translateX(-50%);
}
```

### Node Markers

Small circles on the timeline line mark each milestone.

```css
.timeline-node {
    position: absolute;
    left: 50%;
    width: 8px;                           /* page-specific: node size (spacing scale) */
    height: 8px;
    border-radius: 50%;
    border: 2px solid var(--surface-2);   /* matches line color */
    background: var(--bg);                /* page background fills the center */
    transform: translateX(-50%);
    z-index: 1;
}
```

### Milestone Entry — Alternating Layout

Each milestone occupies a full row. Content appears on one side of the center line, alternating per entry. The opposite side can hold an optional image.

```css
.timeline-entry {
    position: relative;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;                            /* grid gutter */
    padding-bottom: 58px;                 /* vertical spacing between milestones — heading-to-content */
}

/* Even entries: content left, image right */
.timeline-entry:nth-child(even) .timeline-content {
    grid-column: 1;
    text-align: right;
    padding-right: 32px;                  /* card padding — clearance from center line */
}
.timeline-entry:nth-child(even) .timeline-image {
    grid-column: 2;
    padding-left: 32px;
}

/* Odd entries: image left, content right */
.timeline-entry:nth-child(odd) .timeline-content {
    grid-column: 2;
    text-align: left;
    padding-left: 32px;
}
.timeline-entry:nth-child(odd) .timeline-image {
    grid-column: 1;
    text-align: right;
    padding-right: 32px;
}
```

### Milestone Content

```css
.timeline-year {
    font-family: var(--font-mono);
    font-size: 12px;                      /* label — type scale */
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                         /* label opacity */
    margin-bottom: 8px;                   /* spacing scale */
}

.timeline-title {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading — type scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    line-height: 1.3;
    color: var(--text);
    margin-bottom: 8px;
}

.timeline-description {
    font-family: var(--font-body);
    font-size: 16px;                      /* body secondary size */
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;                         /* subtitle hierarchy */
    line-height: 1.6;
}
```

### Optional Milestone Image

Images are optional (1/6 samples with photos: Lightdash; 2/6 with illustrations: Apollo, Going). The timeline works well without images — 3/6 samples use text only per milestone.

```css
.timeline-image img {
    max-width: 100%;
    border-radius: 8px;                   /* feature card radius — radius system */
    background: var(--surface-1);         /* placeholder bg */
}
```

---

## Year Grouping Headers

**When milestones span multiple years -> add year headers above groups**

Useful when showing 7+ milestones across several years (Lightdash pattern). The year header interrupts the alternating flow and centers on the timeline line.

```css
.timeline-year-header {
    position: relative;
    text-align: center;
    padding: 16px 0;
    margin-bottom: 32px;
    z-index: 1;
}

.timeline-year-header span {
    font-family: var(--font-display);
    font-size: 20px;                      /* card heading — type scale */
    font-weight: 500;
    letter-spacing: -0.4px;
    color: var(--text);
    background: var(--bg);                /* covers the timeline line behind the text */
    padding: 0 16px;
}
```

---

## Content per Milestone

**When showing year + title only (2/6: Apollo dark, V7) -> minimal entries**
- Omit `.timeline-description` and `.timeline-image`
- Best for long timelines (10+ milestones) where brevity matters

**When showing year + title + description (1/6: ClickUp) -> standard entries**
- Add 1-2 sentence descriptions
- Default recommendation

**When showing year + title + photo (1/6: Lightdash) -> visual entries**
- Product screenshots, team photos, or event photos on the opposite side
- Best when the company has strong visual milestones (launches, events, office openings)

---

## Milestone Count

- **5-7 milestones**: standard range (3/6 samples show 5-6 visible)
- **8+**: works with the vertical layout but requires scrolling — consider year grouping headers
- **Fewer than 4**: timeline feels sparse; consider embedding milestones in another section instead

---

## Narrow Screen (< 768px)

On narrow screens, the alternating layout collapses to a single column with the timeline line on the left edge.

```css
@media (max-width: 767px) {
    .timeline-heading {
        margin-bottom: 40px;              /* heading-to-content narrow */
    }

    .timeline {
        padding: 0 20px;                  /* narrow side padding */
    }

    .timeline::before {
        left: 20px;                       /* line shifts to left edge */
    }

    .timeline-node {
        left: 17px;                       /* 17px + 4px (half of 8px) = 21px center, aligns with line center */
        transform: none;                  /* cancel desktop translateX(-50%) — at left:17px without this
                                             the center would be at 17px - 4px = 13px, off by 8px */
    }

    .timeline-entry {
        grid-template-columns: 1fr;
        padding-left: 40px;              /* clearance from left-side line (20px padding + 20px gap) */
        padding-bottom: 40px;            /* heading-to-content narrow */
    }

    /* Reset alternating alignment — all content flows left-to-right */
    .timeline-entry:nth-child(even) .timeline-content,
    .timeline-entry:nth-child(odd) .timeline-content {
        grid-column: 1;
        text-align: left;
        padding-left: 0;
        padding-right: 0;
    }

    .timeline-entry:nth-child(even) .timeline-image,
    .timeline-entry:nth-child(odd) .timeline-image {
        grid-column: 1;
        text-align: left;
        padding-left: 0;
        padding-right: 0;
        margin-top: 16px;
    }
}
```

---

## Horizontal Timelines — Note

Horizontal timelines appear in 3/6 samples (Apollo cards, ClickUp staggered, V7 minimal). They are space-efficient but require carousel JavaScript for overflow, which adds complexity. For V1, the vertical alternating timeline is the recommended default. A simple horizontal variant (no carousel, all items visible) is acceptable when milestone count is exactly 4-5:

```css
.timeline-horizontal {
    display: flex;
    justify-content: space-between;
    gap: 24px;                            /* grid gutter */
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.timeline-horizontal .timeline-entry {
    flex: 1;
    text-align: center;
}
```

This variant collapses to a vertical stack on narrow screens.

---

## When NOT to Use

- Do not use winding S-curve paths (Going pattern) or staggered above/below layouts (ClickUp pattern) — these require absolute positioning and do not degrade gracefully
- Do not use colored cards or gradient timeline lines — violates the achromatic system
- Do not use 3D or isometric illustrations per milestone — content as decoration principle
- Do not use accent-colored year text — years use the label style (mono, opacity 0.4), not brand color
- Do not fabricate milestones or dates — use placeholder text like "Milestone description" if real content is unavailable
