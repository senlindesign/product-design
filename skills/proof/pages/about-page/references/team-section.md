# Team Section — Grid Layout and Person Cards

> Source: Mobbin research synthesis from 12 team section observations across Airtable, Miro, Webflow, Handshake, Passionfroot, Sprout Social, 1Password, Intercom, Resend, Studio Freight, Slash, Aurora.

---

## Default Pattern: 3-Column Grid with Circle Photos

Grid layout dominates (7/12 samples). Circle photos are the most system-aligned shape (4/12 samples; square also common at 5/12 but circles are cleaner in a minimal grid). Leadership-only scope is standard (8/12 samples).

### Section Heading

```css
.team-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading — type scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    margin-bottom: 58px;                  /* heading-to-content — spacing system */
}
```

Common heading text: "Leadership" (most common), "Our Team", "Meet the team".

### Grid Layout

```css
.team-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 32px 24px;                       /* 32px vertical (card padding), 24px horizontal (grid gutter) */
    max-width: 1080px;                    /* system grid max-width */
    margin: 0 auto;
    padding: 0 32px;                      /* system side padding */
}
```

### Person Card

```css
.person-card {
    text-align: center;
}

.person-photo {
    width: 96px;                          /* page-specific: mid-range of observed 48-160px */
    height: 96px;
    border-radius: 50%;                   /* circle — default */
    object-fit: cover;
    margin: 0 auto 16px;                  /* 16px photo-to-name gap (spacing scale) */
    background: var(--surface-1);         /* placeholder when no photo loaded */
}

.person-name {
    font-family: var(--font-display);
    font-size: 16px;                      /* body secondary — type scale */
    font-weight: 500;
    color: var(--text);
    line-height: 1.6;
    margin-bottom: 6px;                   /* tight coupling to title (spacing scale minimum) */
}

.person-title {
    font-family: var(--font-display);
    font-size: 14px;                      /* button/nav size — type scale */
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;                         /* subtitle hierarchy */
    line-height: 1.6;
}
```

---

## Grid Column Variants

### When team size is 6-12 (leadership only) -> 3-column grid (default)

- The standard display for leadership teams (8/12 samples show leadership-only)
- 3 columns is the most common count (3/7 grid samples)
- Provides comfortable space for photo + name + title

### When team size is 15+ (full team, 3/12 samples) -> 4-column grid

- Reduces vertical scroll for large rosters
- Works best with name+title only (no bios)

```css
.team-grid--dense {
    grid-template-columns: repeat(4, 1fr);
}

.team-grid--dense .person-photo {
    width: 72px;                          /* smaller to fit narrower columns */
    height: 72px;
}
```

### When each person has a paragraph bio (2/12: Airtable, Intercom) -> 2-column grid

- Extra column width accommodates 3-5 sentence bios
- Each person card becomes a content block, not just a label

```css
.team-grid--detailed {
    grid-template-columns: repeat(2, 1fr);
    gap: 58px 24px;                       /* 58px vertical gap for larger content blocks */
}

.team-grid--detailed .person-card {
    text-align: left;                     /* left-align when bios are present */
}

.team-grid--detailed .person-photo {
    margin: 0 0 16px;                     /* left-align photo too */
}
```

---

## Content Depth Variants

### Variant A: Name + Title Only (4/12 samples)

Best for large teams or when titles speak for themselves. Uses only `.person-name` + `.person-title` elements.

### Variant B: Name + Title + Link (3/12 samples: Slash, Webflow, Passionfroot)

Adds a link to individual bio page, LinkedIn, or profile.

```css
.person-link {
    display: inline-block;
    font-family: var(--font-display);
    font-size: 14px;                      /* button/nav — type scale */
    font-weight: 500;
    color: var(--text);
    opacity: 0.4;                         /* auxiliary level */
    text-decoration: none;
    margin-top: 8px;                      /* spacing scale */
    transition: opacity 0.3s linear;      /* system transition */
}
.person-link:hover {
    opacity: 1;
}
```

Link text: "Read bio" or an arrow character. Do not use colored link text — use opacity transition instead.

### Variant C: Name + Title + Bio (3/12 samples: Airtable, Intercom, Resend)

Adds a paragraph description. Use with the 2-column grid variant.

```css
.person-bio {
    font-family: var(--font-body);
    font-size: 16px;                      /* body secondary size */
    font-weight: 400;                     /* body paragraph weight */
    color: var(--text);
    opacity: 0.5;                         /* subtitle hierarchy */
    line-height: 1.6;
    margin-top: 12px;                     /* spacing scale */
}
```

Bio length: 2-4 sentences. Do not fabricate biographical details — use placeholder text like "Bio will be provided by the team" if real content is unavailable.

---

## Photo Shape Variants

### Circle Headshots (default)

Most aligned with the minimal system. Clean, consistent appearance across varied photo styles.

```css
.person-photo { border-radius: 50%; }
```

### Square Headshots (5/12 samples)

Slightly more editorial. Use when the brand aesthetic is more structured.

```css
.person-photo--square {
    border-radius: 8px;                   /* feature card radius — radius system */
}
```

### No Photo — Text Only (1/12: Studio Freight)

Genuinely rare counterexample (1/12). Only for deliberately minimal/brutalist aesthetic. Remove `.person-photo` entirely; increase name size to compensate for absent visual anchor.

```css
.person-card--text-only .person-name {
    font-size: 20px;                      /* card heading — type scale */
    letter-spacing: -0.4px;
}
```

---

## Multi-Tier Structure

**When displaying Founders + Executive Team separately (1/12: 1Password) -> stacked sub-sections**

Each tier gets its own label and grid. Founders appear first with fewer people, followed by the larger executive team.

```css
.team-tier-label {
    font-family: var(--font-mono);
    font-size: 12px;                      /* label — type scale */
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;                         /* label opacity */
    margin-bottom: 32px;                  /* card padding spacing */
}

.team-tier + .team-tier {
    margin-top: 128px;                    /* large breathing space between tiers */
}
```

Tier structure: "FOUNDERS" (3-4 people, 3-column grid) followed by "EXECUTIVE TEAM" (6-8 people, same or 4-column grid).

---

## Narrow Screen (< 768px)

```css
@media (max-width: 767px) {
    .team-heading {
        margin-bottom: 40px;             /* heading-to-content narrow */
    }

    .team-grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 32px 24px;
        padding: 0 20px;                 /* narrow side padding */
    }

    .team-grid--dense {
        grid-template-columns: repeat(2, 1fr);
    }

    .team-grid--detailed {
        grid-template-columns: 1fr;
    }

    .team-tier + .team-tier {
        margin-top: 80px;                /* large breathing narrow */
    }
}

@media (max-width: 480px) {
    .team-grid {
        grid-template-columns: 1fr;
    }
}
```

---

## Scope Decision Guide

| Signal | Recommendation |
|--------|----------------|
| Startup / small company (< 20 people) | Show full team, 3-column grid, name+title |
| Mid-size company (20-100 people) | Leadership only (6-12 people), 3-column grid |
| Large company (100+ people) | Leadership only, 4-column dense grid, consider multi-tier |
| Agency / studio | Full team, 3 or 4 columns, name+title only |
| Each leader has a unique story to tell | 2-column detailed grid with bios |

---

## When NOT to Use

- Do not use colored backgrounds behind photos (Miro, 1Password pattern) — violates the prohibition on "colored circular/square backgrounds behind icons" in visual-style.md
- Do not use per-person accent colors or role-colored badges (Passionfroot pattern) — violates accent color rules
- Do not display fabricated team members — use placeholder cards with `var(--surface-1)` background if real content is unavailable
- Do not add box-shadow to person cards — zero shadows (design system rule)
- Photos are nearly universal (11/12 samples) — omitting photos should be a deliberate choice, not a default
