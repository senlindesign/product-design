# About Page Archetypes & Selection Guide

> Source: Mobbin research synthesis across ~41 unique products, ~53 section observations (2026-10-01)

---

## Archetype Definitions

### A. Company Story (Default)

**Typical products**: Airtable, Intercom, Dropbox, Customer.io, Quicken, Deel, Apollo, Lightdash
**Core characteristic**: Established product with history; the page tells the company's origin, growth, and direction

**When to use**:
- Product has been around long enough to have milestones (2+ years)
- Company has a founding narrative worth telling
- Team is medium-to-large (leadership display, not full roster)
- Standard corporate About page with no strong ideological angle

**Section composition** (6-8 sections):
1. Nav (shared)
2. Hero (mission statement heading, text-only, no CTA button)
3. Story / Origin (2-4 paragraphs of founding narrative, optionally with founder photo)
4. Team (leadership grid, 3-4 columns, 6-12 people)
5. Stats (4-stat horizontal row: team size + year founded + customers + geography)
6. Values (3-5 values, numbered list or definition list)
7. CTA (careers-focused: "Join the team" / "Open positions")
8. Footer (shared)

**Visual tendencies**:
- Light theme dominant (8/11 hero observations are light)
- 6-8 total sections; longest archetype
- Stats section often uses `var(--surface-1)` background as a full-width band
- Timeline optional (include only when the company has 5+ notable milestones)

---

### B. Team-First

**Typical products**: ElevenLabs, Resend, Passionfroot, Studio Freight
**Core characteristic**: Small team where the people ARE the story; team grid dominates the page

**When to use**:
- Small startup or studio (under 20 people)
- Company identity is inseparable from its team members
- Product is early-stage; there is no long founding narrative to tell
- Dev tools, design studios, consulting firms

**Section composition** (4-5 sections):
1. Nav (shared)
2. Hero (brief mission statement or "Who we are", text-only)
3. Team (dominant section: full team grid, 3-4 columns, every member shown)
4. Values (brief, 3-4 values as a simple list or inline text)
5. CTA (careers: "Join us" or contact: "Work with us")
6. Footer (shared)

**Visual tendencies**:
- Light or dark theme (Resend uses dark)
- 4-5 total sections; shortest archetype
- Team section occupies the largest vertical space on the page
- Stats section is uncommon (small teams have fewer impressive numbers)
- No timeline (not enough history)

---

### C. Mission-Driven

**Typical products**: PayPal, Vanta, Webflow, Attio, Windsurf
**Core characteristic**: Strong ideological position; values and principles dominate the narrative

**When to use**:
- Company has a strong "why" (social impact, security, open web, democratization)
- Values/principles are a hiring filter or product differentiator
- The belief statement carries more weight than the product feature list
- Products where trust and mission alignment matter to the audience

**Section composition** (5-7 sections):
1. Nav (shared)
2. Hero (belief/principle statement as hero heading, no CTA button)
3. Values / Principles (dominant section: 4-5 values with descriptions, numbered or definition list)
4. Stats (4-stat row, positioned after values to ground the mission in evidence)
5. Team (secondary: leadership only, 3-column grid)
6. Investor / Partner logos (optional: reuse social-proof logo wall pattern)
7. CTA (careers-focused, framed as mission invitation: "Join us in building...")
8. Footer (shared)

**Visual tendencies**:
- Light or dark theme (Windsurf uses dark navy; Vanta uses dark hero with light body)
- 5-7 total sections
- Hero heading tends to be a belief statement, not a company name or "About us"
- Values section is the most prominent, often with the most vertical space
- Copy is manifesto-style: assertive, first-person plural ("We believe...", "We care about...")

---

## Cross-Archetype Rules

Regardless of archetype:

1. **Hero is text-only**: No product screenshots, no CTA button (1/11 exception), no product visuals. The mission statement IS the content. See `about-hero.md`
2. **CTA defaults to careers**: 5/6 observed CTAs link to careers/hiring. 0/6 link to product signup. About page CTAs are "Join the team", not "Start free trial"
3. **Stats follow a common 4-item pattern**: team size + year founded + customer count + geography. These are the four most-observed categories (each appearing in 2-4 of 5 samples), though no single observation contains all four simultaneously
4. **Nav and Footer are shared**: Same nav and footer as all other page types. Reuse `shared/navigation.md` and `shared/footer.md`
5. **No product screenshots in hero**: About heroes show the company story, not the product UI. Product visuals belong on the Landing page
6. **Values appear in ALL archetypes**: The difference is emphasis (A: mid-page supporting section; B: brief; C: dominant section)
7. **Team photos are nearly universal**: 11/12 team observations include photos. Text-only team display is a niche pattern (1/12, Studio Freight)

---

## Decision Matrix

```
1. Does the company have a strong ideological position or social mission?
   ├─ Yes → C. Mission-Driven
   └─ No
       ├─ Is the team small (< 20 people) and central to the brand identity?
       │   ├─ Yes → B. Team-First
       │   └─ No → A. Company Story (default)
       └─ Uncertain → A. Company Story (default)

2. After choosing an archetype, adjust sections based on available content:
   - Has 5+ milestones?       → Add Timeline section (A and C only)
   - Has investor backing?     → Add Investor logo wall (C and A only)
   - Has office photos?        → Skip — photos are a visual risk in this system
   - Has press coverage?       → Fold into stats or investor section
   - Team > 8 people?         → Show leadership only, not full roster (A and C)
   - Team < 8 people?         → Show everyone (B)
```

---

## Section Presence by Archetype

| Section | A. Company Story | B. Team-First | C. Mission-Driven |
|---------|-----------------|---------------|-------------------|
| Hero | Required | Required | Required |
| Story / Origin | Required | Optional (brief) | Optional |
| Team | Required (leadership) | Required (full team, dominant) | Required (leadership, secondary) |
| Stats | Required | Optional | Required |
| Values | Required | Optional (brief) | Required (dominant) |
| Timeline | Optional | Skip | Optional |
| Investor logos | Optional | Skip | Optional |
| CTA | Required (careers) | Required (careers/contact) | Required (careers/mission) |
