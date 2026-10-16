# About Page Hero Patterns

> Source: 11 hero observations across well-known brands (Airtable, Dropbox, PayPal, ElevenLabs, Windsurf, Kajabi, Quicken, GitBook, Headspace, Savor) + 1 studio. All tokens validated against `shared/visual-style.md`.

---

## How the About Hero Differs from the Landing Hero

| Dimension | Landing Hero | About Hero |
|-----------|-------------|------------|
| Purpose | Convert: explain product + push to CTA | Declare: state who the company is and what it believes |
| CTA button | Required (primary + optional secondary) | Almost never (1/11 exception: Kajabi) |
| Product visual | Product screenshot is the centerpiece | No product visual — text IS the content |
| Content | Headline + subtitle + CTA + product screenshot | Heading + 1-2 sentence mission statement |
| Height | Tall (128px top + screenshot + spacing) | Shorter (text block only, no visual element below) |
| Label above heading | Rare | Optional (4/11: "ABOUT US", "ABOUT", "VISION", "OUR MISSION") |

**Key insight**: The About hero is a **statement section**, not a conversion funnel. The mission statement replaces both the product tagline and the product screenshot as the hero's primary content.

---

## Heading Copy Patterns

### Pattern 1: Mission / Belief Statement (5/11 — most common)

**When to use**: Archetype A (Company Story) and C (Mission-Driven). The company has a clear belief or mission worth leading with.

**Examples** (from observations):
- Dropbox: "Our mission is to design a more enlightened way of working"
- PayPal: "We believe every person has the right to participate fully in the global economy."
- Windsurf: "Our Mission" (heading) + 3 paragraphs of mission text

**Implementation**: Use `font-size` at section heading scale (not hero heading scale) when the statement is a full sentence. Full-sentence headings at hero scale (80px) become unwieldy.

```css
.about-hero-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading scale — full sentences need this */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}
```

**When to use hero heading scale instead**: When the heading is 2-4 words ("About us", "Who we are") rather than a full sentence.

### Pattern 2: "About [Company]" (3/11)

**When to use**: Archetype A when the company name is well-known. Simple and direct.

**Examples**: Airtable ("About us"), Headspace ("About Headspace"), Quicken ("About Us")

**Implementation**: Short headings can use hero heading scale.

```css
.about-hero-heading-short {
    font-family: var(--font-display);
    font-size: clamp(48px, 7vw, 80px);   /* hero heading scale — works for 2-4 word headings */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.05;
    color: var(--text);
}
```

### Pattern 3: "Who We Are" (2/11)

**When to use**: Archetype B (Team-First). Frames the page as a team introduction.

**Examples**: ElevenLabs ("WHO WE ARE"), Savor ("Who we are")

**Implementation**: Same as Pattern 2 (short heading, hero scale). Do NOT use all-caps unless the product's brand tone is assertive/technical.

---

## Label Above Heading

**Frequency**: 4/11 have a label, 7/11 do not.

**When to include**: When the About page needs a clear section identifier — especially if the hero heading is a full sentence (Pattern 1) and could be confused with a general statement.

**When to omit**: When the heading is self-explanatory ("About us", "Who we are") or when the heading IS the label.

**Common label text**: "ABOUT" / "ABOUT US" / "OUR STORY" / "OUR MISSION" / "VISION"

```css
.about-hero-label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 24px;              /* label to heading gap */
}
```

---

## Layout

### Recommended Default: Centered Text-Only

**When to use**: Default for all archetypes in this design system. Safest layout when no photo is available (which is the expected case, since the system rejects stock photos and illustrations).

**Evidence**: 2/11 hero observations are centered text-only (Windsurf, ElevenLabs). Although 7/11 use two-column layouts, most of those place a photo in the second column — which our system does not generate. Centered text-only avoids the empty-right-column problem.

```css
.about-hero {
    padding-top: 128px;               /* hero top whitespace — from spacing system */
    padding-bottom: 180px;            /* section rhythm */
    text-align: center;
}

.about-hero .container {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.about-hero-heading {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);   /* section heading for full sentences */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    max-width: 720px;                 /* prevent overly long heading lines */
    margin: 0 auto;
}

.about-hero-body {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    max-width: 540px;                 /* subtitle max-width from grid system */
    margin: 24px auto 0;             /* heading to subheading gap */
}
```

**Narrow screen (< 768px)**:
```css
@media (max-width: 767px) {
    .about-hero {
        padding-top: 80px;            /* 128px → 80px */
        padding-bottom: 96px;         /* 180px → 96px */
    }
    .about-hero .container {
        padding: 0 20px;              /* 32px → 20px */
    }
}
```

### Alternative: Full-Width Short Heading

**When to use**: When the heading is 2-4 words ("About us", "Who we are") and the page wants a bold typographic opening. Best for Archetype B (Team-First) where the team grid immediately follows.

```css
.about-hero-heading-short {
    font-family: var(--font-display);
    font-size: clamp(48px, 7vw, 80px);   /* hero heading scale */
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.05;
    color: var(--text);
    text-align: center;
}
```

---

## What the About Hero Does NOT Include

- **No CTA button**: 10/11 heroes have no button. The About hero is a statement, not a conversion point. Exception: Kajabi includes "See Open Positions" — this is a careers CTA, still not product conversion
- **No product screenshot**: Product visuals belong on the Landing page. About hero content is the company's identity, not its interface
- **No illustration or brand mascot**: Headspace uses a brand mascot — this violates the system's "Content as decoration" principle. No illustrations
- **No video embed**: No hero observations include embedded video
- **No background photo**: Dropbox uses a photo background (1/11), but photo backgrounds are outside the system's achromatic principles. Use `var(--bg)` only
