# Section Composition Rules — Contact Page

> Source: Mobbin research synthesis from 53 section-level observations across ~30 independent products

---

## 1. Recommended Section Order by Archetype

### A. Simple Contact

```
Navigation
    |
Page Header (title + optional subtitle)
    |
Contact Section (form + contact info, side by side or stacked)
    |
FAQ (optional, 3–4 questions)
    |
Footer
```

### B. Department Routing

```
Navigation
    |
Page Header (title + subtitle)
    |
Department Cards (2–4 card grid)
    |
Contact Info / Offices (optional; multiple office locations or general info)
    |
FAQ (optional)
    |
Footer
```

### C. Sales-Focused

```
Navigation
    |
Form Section (left: title + description + social proof — right: Demo form)
    |
Trust Signals (optional; customer logo wall or testimonial)
    |
FAQ (optional, 3–4 questions)
    |
Footer
```

### D. Support Hub

```
Navigation
    |
Page Header + Search (title + search bar)
    |
Help Categories (topic category card grid)
    |
Contact Fallback ("Still need help?" + contact entry)
    |
FAQ (optional)
    |
Footer
```

---

## 2. Hard Rules Between Sections

These rules must not be violated:

| Rule | Explanation |
|------|-------------|
| **Form or cards must come after Page Header** | Users first understand the page's purpose, then act. The header establishes context at the top |
| **Department Cards and inline Contact Form must not coexist** | Card routing means each department has a separate workflow; having a general form on the same page causes confusion. If a general form is needed, use a Subject dropdown for lightweight routing (Archetype A variant) — not cards |
| **Social Proof must be adjacent to the form** | Sales-Focused (C) trust signals must be in the same visual area as the form (within the left-right split, or immediately below the form), not separated by other sections |
| **Contact Fallback comes after Help Categories** | Support Hub (D) contact entry is a last resort for "couldn't find an answer"; it belongs after self-service content |
| **Nav at the top, Footer at the bottom** | Fixed positions; reuse `shared/navigation.md` and `shared/footer.md` |

---

## 3. Soft Rules Between Sections

Can be adjusted based on content, but follow by default:

| Rule | Explanation | Exception |
|------|-------------|-----------|
| **FAQ comes after form / cards** | FAQ answers questions users have while considering making contact | If FAQ content is "what to know before contacting," it can go before the form |
| **Contact Info in the same section as the form** | Side-by-side presentation reduces page navigation | For multiple office locations, can be a standalone section (Offices part of Archetype B) |
| **Page Header has no CTA button** | The Contact Page itself is the CTA; the header doesn't need a button | When Archetype B's header is immediately followed by Department Cards, the cards themselves are the CTA |
| **No Bottom CTA needed** | Contact pages aren't as long as Landing/Pricing pages; no need to repeat a CTA at the bottom | No exception. The Contact Page's primary action (form/cards) is already in the upper portion |

---

## 4. Spacing Rules

```
Section spacing (vertical space between sections):       180px
Page Header top padding (nav to title):                 80px (Contact Page is more compact than Landing Page — it's a utility page, not a showcase)
Page Header to content section:                         58px (standard title-to-content distance)
Section title to content within a section:              58px
Form field spacing (vertical space between fields):     24px
Form field label to input:                              8px
Two-column field horizontal gap:                        24px
Contact Info item spacing:                              24–32px
Department Cards gap:                                   24px
Footer top padding:                                     128px
```

**Key distinctions**:
- Contact Page is overall shorter than Landing Page and Pricing Page, but section spacing remains 180px — there are fewer sections (2–4 content sections), and spacing maintains the breathing room
- Page Header to content spacing (80px) is more compact than Landing Page Hero to next section (180px), because the Contact Header is shorter and more direct
- Forms are dense interactive areas; internal spacing uses 24px (compact but not cramped), unlike the 180px between sections

---

## 5. Background Color Rules

```
Navigation:           var(--bg)              transparent / white
Page Header:          var(--bg)              consistent with nav
Contact Section:      var(--bg)              main area
  (form container):   var(--bg) or var(--surface-1)   optional surface-1 for card-style container
Department Cards:     var(--bg)              cards themselves use var(--surface-1)
Contact Info:         var(--bg)
Help Categories:      var(--bg)              cards use var(--surface-1)
FAQ:                  var(--bg)
Footer:               var(--bg) or var(--surface-1)
```

**Core principles**:
- Contact Page background is **nearly unified** throughout (var(--bg))
- **At most 1 section** may use var(--surface-1) background — typically the Contact Info standalone section or Offices section
- Department Cards and Help Category Cards use `var(--surface-1)` background, but the section they're in has `var(--bg)` background
- The form container can optionally use `var(--surface-1)` + `border-radius: 16px` for a card-style wrapper (Aave pattern), or be placed directly on `var(--bg)` without a wrapper
- **Do not use colorful backgrounds** for form areas, header areas, or any section

---

## 6. Decision Guide for Adding / Removing Sections

### When to Add

| Section | Condition for adding |
|---------|---------------------|
| Contact Info (side by side) | Have real email / phone / address to display |
| Contact Info (standalone section) | Multiple office locations; too much info to fit side by side |
| Department Cards | 3+ departments with separate contact workflows (not just different recipients) |
| Social Proof (logos / testimonials) | Archetype C only, and there are genuine customer logos or testimonials |
| FAQ | 3+ common contact-related questions ("Response time?" "Business hours?" "Data privacy?") |
| Search | Archetype D only, and there is a searchable help content library |

### When to Remove

| Section | Condition for removing |
|---------|----------------------|
| Contact Info | User hasn't provided any contact details (form only) |
| Department Cards | Fewer than 2 departments, or departments have no workflow differences |
| Social Proof | Not Archetype C, or no real customer data |
| FAQ | Fewer than 3 meaningful questions |
| Search | Not Archetype D, or no help documentation database |

---

## 7. Minimum Page vs. Full Page

### Minimum Viable Contact Page (Archetype A)

```
Navigation -> Page Header -> Contact Form (3 fields) -> Footer
```
Approximately 2 content sections; minimal and efficient. Suited for early-stage products or personal projects.

### Standard Contact Page (Archetype A/B)

```
Navigation -> Page Header -> Contact Section (form + info) -> FAQ (3-4 questions) -> Footer
```
Approximately 3 content sections; covers most needs.

### Full Contact Page (Archetype B + Offices / Archetype C)

```
Navigation -> Page Header -> Department Cards (3-4) -> Office Locations -> FAQ -> Footer
```
Or:
```
Navigation -> Form Section (info + form + social proof) -> Trust Signals -> FAQ -> Footer
```
Approximately 4–5 content sections. **Do not exceed 5** — the Contact Page should quickly guide users to action, not bombard them with information.

---

## 8. Shared Components with Other Pages

The following components reuse existing styles and are not redefined on the Contact Page:

| Component | Source | Notes |
|-----------|--------|-------|
| Navigation | `shared/navigation.md` | Consistent style; active state marks "Contact" |
| Footer | `shared/footer.md` | Fully reused |
| FAQ layout | `pages/landing-page/references/faq.md` | Accordion / two-column layout reused |
| Button styles | `shared/visual-style.md` component Token | `.btn-dark` and `.btn-outline` reused |
| Label styles | `shared/visual-style.md` component Token | `.label` style reused |

---

## 9. Components Unique to the Contact Page

The following components are new to the Contact Page and need specific tokens defined in files like `contact-form.md`:

| Component | Applicable Archetype | Brief description |
|-----------|---------------------|------------------|
| Contact Form | A, B (form routing variant), C | Inputs, textarea, select, submit button |
| Department Cards | B | Routing cards with title + description + CTA |
| Contact Info Block | A, B | Information display block for email / phone / address |
| Search Bar | D | Help center search bar (pill shape) |
| Help Category Cards | D | Help topic category cards |
