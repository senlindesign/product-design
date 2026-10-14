# Anti-Patterns — Contact Page

> Source: 53 section-level observations across ~30 independent products + lessons from Landing Page / Pricing Page Skill practice

---

## 1. Form Errors

### 1.1 Too Many Fields for Simple Contact

**Problem**: Archetype A (Simple Contact) form uses 6+ fields, including qualification-filtering fields like Company Size, Industry, Role.
**Why it's wrong**: Simple Contact users expect to "send a quick message." Too many fields increase friction and reduce completion rate. Qualification-filtering fields belong to Archetype C (Sales-Focused); putting them in a simple contact form implies "you need to be screened before you can contact us." Observation data: Approximately 88% (7/8 pure A samples) of Archetype A forms have 3–5 fields.
**Correct approach**: Archetype A maximum 5 fields. Core set = Name + Email + Message. Can add Subject dropdown and Phone (optional). If Company/Role fields are needed, upgrade to Archetype C.
**Checklist item**: Archetype A field count ≤ 5?

---

### 1.2 Missing Email Field

**Problem**: Contact form has no email input, or email is marked as optional.
**Why it's wrong**: 100% of observed samples include an email field. Email is the only reliable channel for replying to users — phone numbers aren't universal across all regions, and users may be unwilling to provide one.
**Correct approach**: Email is a required field in any contact form, placed after Name. Use `type="email"` to trigger the email keyboard on mobile.
**Checklist item**: Does the form have a required email field?

---

### 1.3 Inconsistent Input Field Styles (Default to Full Border)

**Problem**: Different input field styles are mixed within the same form, or no style was explicitly chosen.
**Why it's wrong**: Our design system defines `input border-radius: 4px`, implying a full border. Full border is the default choice. Although underline-only (26%) and filled-background (22%) also exist in real products (FARFETCH, Oevra, Assembly Coffee), the **entire form must consistently use one style** — no mixing.
**Correct approach**: **Use full border by default** — `border: 1px solid var(--surface-2); border-radius: 4px; background: var(--bg); padding: 8px 16px`. Focus state: `border-color: var(--text)`. If the user explicitly requests a more minimal style, switch the entire form to underline-only or filled-background (see alternative styles in contact-form.md), but do not mix styles.
**Checklist item**: Are all input fields consistently using the same style? Is the default full border + 4px radius?

---

### 1.4 Decorative Border-Top on the Form

**Problem**: Form container has `border-top: 3px solid var(--accent)` or a gradient color strip at the top.
**Why it's wrong**: Based on Landing Page Skill practice (not from this Contact Page observation), decorative border-top is a high-frequency feature of AI-generated interfaces. Real product contact forms don't need a top decorative strip — the form's visual hierarchy is established by its position and heading, not by border-top highlighting.
**Correct approach**: Form container has no decorative border-top. If a visual wrapper is needed, use `background: var(--surface-1); border-radius: 16px; padding: 32px` (card-style container), or place it directly on `var(--bg)` without a container.
**Checklist item**: Does the form have a decorative border-top? If yes, delete it.

---

### 1.5 Mixed Input Field Styles

**Problem**: Different styles are mixed within the same form — text inputs use full border, textarea uses underline-only, select uses filled background.
**Why it's wrong**: Breaks visual consistency and increases cognitive load. Users will wonder whether different styles mean different behaviors.
**Correct approach**: Text inputs, textarea, and select all use the same style — `border: 1px solid var(--surface-2); border-radius: 4px; background: var(--bg); font-family: var(--font-display); font-size: 16px`. Textarea height is fixed or limited to `resize: vertical`. Select adds `appearance: none` to standardize the arrow.
**Checklist item**: Are all form controls (input/textarea/select) using a consistent style?

---

### 1.6 Submit Button Copy Too Generic

**Problem**: All forms use "Submit" as the CTA copy.
**Why it's wrong**: Although "Submit" appears in real products approximately 18% of the time (4/22 samples), more specific copy conveys the action meaning and expected outcome. "Send message" / "Request a demo" has more directional clarity than "Submit." This is a **recommendation**, not a hard prohibition.
**Correct approach**: Choose copy based on Archetype —
- A (Simple Contact) → "Send message" / "Send"
- B (Department Routing) → Differentiated CTA per department ("Contact Sales" / "Get Support")
- C (Sales-Focused) → "Request a demo" / "Book a demo" / "Talk to [ProductName]"
- D (Support Hub) → "Submit a ticket" / "Get help"
**Checklist item**: Is the CTA copy more specific than "Submit"?

---

## 2. Layout Errors

### 2.1 Centered Narrow Form Without Context

**Problem**: A narrow form (max-width 400–500px) sits in the center of the page surrounded by large whitespace, with no contact info, description, or visual support.
**Why it's wrong**: The page looks empty and incomplete. Users lack context — "Who am I sending this to?" "Are there other contact methods?" "Will someone reply?" Observation data: 61% of forms use a left-right split layout with a description, contact info, or social proof on the left.
**Correct approach**: Two options —
1. **Left-right split**: Left side has heading + description + contact info; right side has the form. Form width is approximately 50% of page width.
2. **Centered single-column**: Form max-width 640px, with a Page Header (title + subtitle) above and contact info below.

Not allowed: form occupies the page with no descriptive text context whatsoever.
**Checklist item**: Is there descriptive text or contact info around the form?

---

### 2.2 Department Cards Without CTA Differentiation

**Problem**: All department cards use the same CTA button style and copy ("Contact Us" × 4).
**Why it's wrong**: 80% of observed samples use differentiated CTA copy. Uniform CTA cannot convey different actions for different departments — "Contact Sales" might navigate to a demo booking, while "Contact Support" might navigate to the help center; these are different actions.
**Correct approach**:
- Each card's CTA copy reflects the specific action ("Contact Sales" / "Visit Help Center" / "Email Partnerships")
- Sales / primary department card uses `.btn-dark` (filled); others use `.btn-outline`
- Don't use the same button style for all cards — at minimum differentiate primary from secondary
**Checklist item**: Are department card CTAs differentiated (copy + button style)?

---

### 2.3 Department Cards and General Contact Form Coexisting

**Problem**: The page has both department routing cards (clicking navigates to different departments) and a general contact form.
**Why it's wrong**: Contradictory information architecture — cards tell users "select a department," while the form tells users "write to us directly." Users don't know which to use.
**Correct approach**: Choose one —
- **Card routing**: Department cards are the only contact entry; each card navigates to a standalone form or page
- **Form routing**: A single general form + Subject/Reason dropdown for lightweight routing; no cards

If both must be shown, de-emphasize the general form as an "Other inquiries" entry, placed below the cards, visually positioned as a fallback for "None of the above."
**Checklist item**: Are department cards and an inline contact form coexisting? If so, reconsider the information architecture.

---

### 2.4 Sales-Focused Form Without Social Proof

**Problem**: Archetype C (Sales-Focused) page has only a large form, with no trust signals on the left side or surrounding area.
**Why it's wrong**: A sales form asks users to provide detailed information (company, role, size), which requires trust. 75% of Sales-Focused samples display customer logos, testimonials, or quantified data alongside the form. A demo form without trust signals looks like a blank bureaucratic collection form.
**Correct approach**: Left-right split; the left side includes at least one of the following —
- Customer logo wall (3–6 logos, the style's logo-wall opacity)
- Quantified data ("X users", "Y% improvement")
- 1 testimonial (with name and company)
- G2 / award badges

If there is no real social proof data, use placeholders and note them in the delivery notes.
**Checklist item**: Does the Archetype C form have social proof alongside it?

---

## 3. Visual Errors

### 3.1 Input Fields Have Box-Shadow

**Problem**: Input fields have `box-shadow: 0 1px 3px rgba(0,0,0,0.1)` or a focus-state `box-shadow: 0 0 0 3px rgba(accent, 0.2)`.
**Why it's wrong**: The design system uses zero shadows (`shared/visual-style.md` Section 5). No elements use box-shadow. Hierarchy is established through background color steps and borders. The focus ring uses `border-color: var(--text)` instead of a shadow ring.
**Correct approach**: Input fields have zero shadow. The focus state only changes border-color: `border-color: var(--text)`. For a stronger focus indicator, use `outline: 2px solid var(--text); outline-offset: 2px` (outline is not shadow).
**Checklist item**: Do input fields have any box-shadow? If yes, remove it.

---

### 3.2 Colorful Background on Form Area

**Problem**: The section containing the form uses a colorful background (light blue, light green, light purple), or the form container uses a light variant of the brand color as background.
**Why it's wrong**: Chromatic Silence principle — chromatic area < 10%, and sections are not allowed to use colorful backgrounds (`shared/visual-style.md` Section 8 "absolute prohibitions" list). Form container background can only be `var(--bg)` or `var(--surface-1)`, not a brand color.
**Correct approach**: Form area background = `var(--bg)`. Card-style form container background = `var(--surface-1)`. No colors allowed.
**Checklist item**: Is the form area or container background a pure achromatic color?

---

### 3.3 Large Border-Radius on Input Fields

**Problem**: Input fields use `border-radius: 8px` or larger, inconsistent with button border-radius (2px).
**Why it's wrong**: The design system border-radius scale (`shared/visual-style.md` Section 4) explicitly defines inputs as 4px. Large-radius inputs + small-radius buttons in the same form are visually inconsistent.
**Correct approach**: Input fields `border-radius: 4px`, buttons `border-radius: 2px`. Textarea also 4px. Select also 4px.
**Checklist item**: Is the input field border-radius 4px?

---

### 3.4 Pill-Shaped Submit Button

**Problem**: Submit button uses `border-radius: 999px` (fully rounded).
**Why it's wrong**: System button border-radius is 2px (`shared/visual-style.md` Section 4). Fully rounded buttons are a high-frequency feature of AI-generated pages.
**Correct approach**: `border-radius: 2px` — sharp and authoritative. Button style reuses `.btn-dark` (`padding: 8px 16px; font-size: 14px; font-weight: 500`).
**Checklist item**: Is the button border-radius 2px?

---

### 3.5 Department Cards in Different Colors

**Problem**: Each department card uses a different icon color, border color, or background color (Sales blue, Support green, Press purple).
**Why it's wrong**: Increases cognitive load with no semantic meaning. In real products, card distinction comes from titles and descriptions (content), not colors. Refer to Pricing Page anti-pattern 1.2 — "all tiers share the same color system."
**Correct approach**: All department cards use a uniform style — `background: var(--surface-1); border-radius: 8px; padding: 32px`. Icons uniformly `color: var(--text); opacity: 0.5`; no colors.
**Checklist item**: Are all department cards using a consistent style (background, border, icon color)?

---

### 3.6 Icon with Colored Circular/Square Background

**Problem**: Icons in department cards or contact info are placed inside colored circular or square backgrounds (white phone icon inside a blue circle).
**Why it's wrong**: The `shared/visual-style.md` "absolute prohibitions" list explicitly prohibits "icons inside colored circular/square backgrounds." Icons should be monochrome, with opacity controlling hierarchy.
**Correct approach**: Icons use `color: var(--text); opacity: 0.4–0.5` directly, with no background container. If a visual placeholder is needed, icon size is controlled at 20–24px, aligned with text.
**Checklist item**: Are any icons placed inside a colored background container? If yes, remove the container.

---

### 3.7 Form Labels Using Different Colors or Decorations

**Problem**: Form field labels use brand color, bold weight, or different font sizes as decoration.
**Why it's wrong**: Form labels are functional text, not design elements. Hierarchy is controlled by font-size and opacity, not color.
**Correct approach**: Form label style — `font-family: var(--font-display); font-size: 14px; font-weight: 500; color: var(--text); opacity: 0.5; margin-bottom: 8px` (0.5 is the opacity ladder secondary tier; 0.7 is off-scale). Placeholder style — `color: var(--text); opacity: 0.3`.
**Checklist item**: Do form labels use a consistent style (no color or decoration)?

---

## 4. Content Errors

### 4.1 Fabricated Contact Information

**Problem**: Generate what appears to be real email (hello@company.com), phone numbers (+1 555-0123), or addresses.
**Why it's wrong**: Contact information must come from real data provided by the user. Fabricated contact details, if deployed, have serious consequences — users can't reach the company, or messages get sent to the wrong address.
**Correct approach**: Use placeholders — `[email@company.com]`, `[+1 XXX-XXXX]`, `[Address]`. Note all placeholders in the delivery notes.
**Checklist item**: Does the contact information come from user-provided data?

---

### 4.2 Page Header Uses Value-Oriented Copy

**Problem**: Contact Page title uses Landing Page–style value propositions ("Accelerate your workflow today" / "Transform how you work").
**Why it's wrong**: Contact Page titles are service-oriented, not marketing-oriented. In all observations, 100% of titles are direct ("Contact Us"), question-form ("How can we help?"), or invitation-form ("Get in touch"). Titles average 2–5 words with no product value messaging needed.
**Correct approach**: Choose one of the following —
- Direct: "Contact us" / "Contact"
- Question: "How can we help?"
- Invitation: "Get in touch" / "Let's talk"

Subtitle: 1–2 sentences stating which teams can be contacted or the expected response method.
**Checklist item**: Is the Page Header concise and service-oriented (2–5 words, no value proposition)?

---

## 5. When the User Provides a Brand Color

Adjustments to the rules above:

- Brand color CTA button changes from black/white to the brand color (`var(--accent)`) — normal behavior
- Department cards' primary CTA can use brand color (`.btn-dark` adapts automatically)
- 1.3 does not relax: input fields still use `border: 1px solid var(--surface-2)`, not a brand color border
- 3.1 does not relax: focus ring still uses `border-color: var(--text)`, not brand color `box-shadow: 0 0 0 3px rgba(accent, 0.2)` (this is a shadow; violates the zero-shadow rule)
- 3.2 does not relax: form areas still use `var(--bg)` or `var(--surface-1)` background, not a light variant of brand color
- 3.5 does not relax: department cards still use a uniform style, not different brand color variants per department
- 3.6 does not relax: icons still use `color: var(--text); opacity: 0.4–0.5`, not brand color
- Chromatic area < 10% does not relax

---

## 6. Verification Method

After generating the Contact Page, verify the following 15 items:

1. **Does field count match the Archetype?** A: 3–5 fields, B: 4–6 fields (or no form, use cards), C: 5–9 fields, D: possibly no form
2. **Is there a required email field?** No = error
3. **Are input fields consistently using full border + 4px radius?** Underline / filled / mixed = error
4. **Is there any box-shadow?** Yes = delete
5. **Is the button border-radius 2px?** 999px = error
6. **Does the form have a decorative border-top?** Yes = delete
7. **Are department card styles consistent?** Different colors / backgrounds = error
8. **Are department card CTAs differentiated?** All "Contact Us" = error
9. **Does the Archetype C form have social proof?** No = needs to be added
10. **Is the Page Header concise and service-oriented?** Value-oriented copy = error
11. **Does the contact information come from user data?** Fabricated = replace with placeholders
12. **Is the form area background a pure achromatic color?** Colorful = error
13. **Do icons have colored background containers?** Yes = delete
14. **Do department cards and inline form coexist?** Coexisting = reconsider
15. **After removing all color, is the form still usable?** If it depends on color to distinguish required / optional fields = structural problem
