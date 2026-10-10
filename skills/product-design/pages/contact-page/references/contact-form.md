# Contact Form — Design Knowledge

> Source: Mobbin research synthesis from 22 product Contact/Demo forms (14 general + 8 Sales/Demo)

---

## Pattern 1: Left-Right Split — Left Info + Right Form (Recommended Default)

**When to use**:
- Product needs to show brand information, value propositions, or contact details alongside the form
- Works for Archetype A/B/C; it is the most mainstream Contact form layout
- Left side content can be: heading + description, contact info list, social proof (customer logos / testimonials)

**Execution**:

**Container Token**:
```css
.contact-split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 58px;                       /* standard title-to-content distance */
    max-width: 1080px;               /* consistent with main grid */
    margin: 0 auto;
    padding: 0 32px;
    align-items: start;
}
```

**Left info area**:
```css
.contact-info-side {
    padding-top: 8px;                /* visual alignment with right-side form */
}

.contact-info-side h1 {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
}

.contact-info-side .description {
    font-family: var(--font-body);
    font-size: 18px;
    font-weight: 400;
    line-height: 1.6;
    color: var(--text);
    opacity: 0.5;
    margin-top: 24px;
}
```

**Variants**:
- **Archetype A (Simple Contact)**: Left side has heading + description + direct contact info (email, phone, address). Reference: Webflow, Assembly Coffee
- **Archetype C (Sales/Demo)**: Left side has heading + value proposition list + customer logos / testimonial. Reference: Vercel, Customer.io, Height

**When not to use**:
- Very few form fields (fewer than 3): the split makes the right side feel empty — use centered single-column
- Mobile: must stack to single-column (info above, form below)

**Evidence**: Webflow, Vercel, Vanta, Customer.io, Height, Vizcom, Assembly Coffee, YLLW, Maxima Therapy and others — 14/23 (61%)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Centered Single-Column Form

**When to use**:
- 3–5 form fields; modest content volume
- Page has a large title at the top (e.g., "CONTACT"), and the form is the only interactive area
- First alternative layout for Archetype A (Simple Contact)

**Execution**:

```css
.contact-centered {
    max-width: 560px;                /* maximum form width */
    margin: 0 auto;
    padding: 0 32px;
}

.contact-centered h1 {
    font-family: var(--font-display);
    font-size: clamp(32px, 4vw, 47px);
    font-weight: 500;
    letter-spacing: -0.02em;
    line-height: 1.1;
    color: var(--text);
    text-align: center;
    margin-bottom: 58px;             /* standard title-to-content distance */
}
```

**Variants**:
- **Card container style**: Form wrapped in a surface-1 background card for added visual hierarchy. `background: var(--surface-1); padding: 32px; border-radius: 16px;`. Reference: Aave
- **Plain background style**: Form placed directly on the page background with no additional container. Reference: NEON, MANA

**When not to use**:
- 6+ form fields — vertical scroll becomes too long; consider a split layout
- Needs to show contact info or social proof — not enough space; use split layout

**Evidence**: NEON, Framer, Aave, MANA, Rains, Savor and others — 6/23 (26%)
**Evidence status**: Cross-sample inference

---

## Field Combination Rules

### Archetype A — Simple Contact (3–5 fields)

**When to use**:
- General inquiry form; no qualification filtering needed
- Any product wanting low-friction communication

**Execution**:
- **Minimum set (3 fields)**: Name, Email, Message — Reference: Framer, Webflow
- **Standard set (4–5 fields)**: Name, Email, Phone (optional), Subject/Reason (optional), Message — Reference: Rains, Yellowbird
- **Don't split Name**: Use a single "Name" or "Full Name" field. Split First/Last only for Archetype C or legal/compliance scenarios

**Variants**:
- Add an "I am a..." dropdown for user identity identification (not department routing). Reference: Savor
- When adding a Phone field, mark it as optional to reduce friction

**When not to use**:
- Need to qualify leads — insufficient fields; use Archetype C

---

### Archetype B — Department Routing (4–6 fields)

**When to use**:
- Messages need to reach different departments (General / Support / Sales / Press)
- Product has multiple teams handling different types of inquiries

**Execution**:
- Add a Subject/Reason field on top of Archetype A
- **Dropdown routing** (recommended): `<select>` dropdown with 3–5 options. Reference: FARFETCH, Rains, Maxima Therapy
- **Radio routing**: When options are ≤ 3, radio buttons are more intuitive than a dropdown. Reference: NEON

**Subject/Reason field Token**:
```css
.form-select {
    width: 100%;
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    background: var(--bg);
    border: 1px solid var(--surface-2);
    border-radius: 4px;              /* input border-radius */
    appearance: none;
    cursor: pointer;
}

.form-select:focus {
    outline: none;
    border-color: var(--text);
}
.form-select:focus-visible {
    outline: 2px solid var(--text);
    outline-offset: 2px;
}

/* custom dropdown arrow */
.select-wrapper {
    position: relative;
}
.select-wrapper::after {
    content: '';
    position: absolute;
    right: 16px;
    top: 50%;
    transform: translateY(-50%);
    width: 0;
    height: 0;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 5px solid var(--text);
    opacity: 0.4;
    pointer-events: none;
}
```

**Radio routing Token** (when options ≤ 3):
```css
.form-radio-group {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 24px;
}

.form-radio-group label {
    display: flex;
    align-items: center;
    gap: 8px;
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    cursor: pointer;
}

.form-radio-group input[type="radio"] {
    width: 18px;
    height: 18px;
    accent-color: var(--text);
}
```

**When not to use**:
- More than 5 departments — dropdown list too long; consider paginating or selecting a broad category first

---

### Archetype C — Sales/Demo Form (5–9 fields)

**When to use**:
- Goal is to qualify leads (Company size, Industry, Role)
- Demo booking or Enterprise inquiry
- Form submission followed up by the sales team

**Execution**:
- **Typical field set**: Work Email, First Name + Last Name (two-column), Company Name + Company Size (two-column, dropdown), Phone, Industry/Interest (dropdown), Message (textarea), Privacy checkbox
- Field priority: Work Email > Company Size > Name > Phone > Industry
- **Split Name into First/Last**: Two-column layout saves space and CRM integration requires it
- **Company Size uses dropdown**: Options such as "1-10", "11-50", "51-200", "201-1000", "1000+"
- Left side must have social proof (customer logos or testimonial) to balance the high-friction form on the right

**Variants**:
- **Lightweight demo (5 fields)**: Omit Phone and Industry. Reference: Height, Antimetal
- **Heavy demo (8–9 fields)**: Includes Country, Website, "How did you hear about us?". Reference: Vercel, Customer.io, Legora
- **All-dropdown style**: Use dropdowns for everything except Email to minimize typing. Reference: Vanta

**When not to use**:
- General contact form — too many fields will deter non-sales inquiries

**Evidence**: Vercel, Vanta, Customer.io, Height, Vizcom, Antimetal, Jasper, Legora and others — 8/23
**Evidence status**: Cross-sample inference

---

## Input Field Styles

### Style A: Full Border (Recommended Default)

**When to use**:
- Safest default choice; works for all archetypes
- Naturally consistent with the surface color scale system in visual-style.md

**Execution**:
```css
.form-input,
.form-textarea {
    width: 100%;
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    background: var(--bg);
    border: 1px solid var(--surface-2);  /* #E9E9E9 (Light) / #1F1F1F (Dark) */
    border-radius: 4px;                  /* visual-style.md input border-radius */
    transition: border-color 0.3s linear;
}

.form-input:focus,
.form-textarea:focus {
    outline: none;                       /* suppress default for mouse users */
    border-color: var(--text);           /* border darkens on focus */
}
.form-input:focus-visible,
.form-textarea:focus-visible {
    outline: 2px solid var(--text);      /* visible ring for keyboard users */
    outline-offset: 2px;
}

.form-input::placeholder,
.form-textarea::placeholder {
    color: var(--text);
    opacity: 0.3;
}
```

**Evidence**: 12/23 (52%) use full border
**Evidence status**: Cross-sample inference

---

### Style B: Underline-Only

**When to use**:
- Pursuing minimal visuals; fewer form fields (3–5)
- Paired with all-uppercase mono labels for a more design-forward aesthetic

**Execution**:
```css
.form-input-underline {
    width: 100%;
    padding: 12px 0;
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    background: transparent;
    border: none;
    border-bottom: 1px solid var(--surface-2);
    border-radius: 0;                    /* no border-radius for underline style */
    transition: border-color 0.3s linear;
}

.form-input-underline:focus {
    outline: none;
    border-bottom-color: var(--text);
}
.form-input-underline:focus-visible {
    outline: 2px solid var(--text);
    outline-offset: 2px;
}
```

**When not to use**:
- Many form fields (6+) — many underline inputs create visual chaos with unclear boundaries
- Scenarios requiring clear distinction between input areas and the page background

**Evidence**: Oevra, FARFETCH, YLLW, Rains, Jeton, Savor and others — 6/23 (26%)
**Evidence status**: Cross-sample inference

---

### Style C: Filled Background

**When to use**:
- When the page background is pure white/black, using surface-1 fill on input fields increases differentiation
- Suitable for forms with many fields; filled backgrounds help users locate each field area

**Execution**:
```css
.form-input-filled {
    width: 100%;
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    background: var(--surface-1);        /* #F5F5F5 (Light) / #141414 (Dark) */
    border: 1px solid transparent;       /* reserve space for focus border */
    border-radius: 4px;
    transition: border-color 0.3s linear;
}

.form-input-filled:focus {
    outline: none;
    border-color: var(--text);
}
.form-input-filled:focus-visible {
    outline: 2px solid var(--text);
    outline-offset: 2px;
}
```

**When not to use**:
- The form container itself already has a surface-1 background — inputs merge with the container and become indistinguishable

**Evidence**: Assembly Coffee, Height, Antimetal, Legora and others — 5/23 (22%)
**Evidence status**: Cross-sample inference

---

## Label Placement

### Method 1: Label Above Input (Recommended Default)

**When to use**:
- 4+ form fields; clear identification of each field is needed
- Best accessibility — label is always visible

**Execution**:
```css
.form-label {
    display: block;
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    margin-bottom: 8px;
}
```

**Variants**:
- **Mono all-caps label**: Paired with underline inputs for a more design-forward aesthetic
```css
.form-label-mono {
    display: block;
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 8px;
}
```
Reference: Oevra, Kinfolk, Aino Agency

---

### Method 2: Placeholder-Only (No Separate Label)

**When to use**:
- Minimal form (3 fields); field purpose is self-explanatory (Name, Email, Message)
- Pursuing maximum visual simplicity

**Execution**:
- Placeholder copy clearly describes the field purpose: `"Your name"`, `"Email address"`, `"Your message"`
- Don't use technical jargon like `"Enter email"`

**When not to use**:
- 4+ fields — users can't see the label after filling in the field; easy to get confused
- Complex forms with dropdowns or checkboxes — explicit labels are needed

**Evidence**: Framer, Aave, Webflow and others — approximately 6/23
**Evidence status**: Cross-sample inference

---

## Textarea Handling

**Execution**:
```css
.form-textarea {
    /* inherits base styles from .form-input */
    min-height: 120px;               /* minimum height, 4-5 lines */
    max-height: 240px;               /* prevent unlimited stretching */
    resize: vertical;                /* allow only vertical resizing */
    line-height: 1.6;
}
```

**Textarea Placeholder Copy**:
- General: `"Your message"`, `"How can we help?"`
- Conversational: `"What's up?"` (Webflow)
- Product-specific: `"How would you like to integrate?"` (Aave), `"What would you like to cover?"` (Height)

**Rules**:
- Textarea is always the last text field in the form (before the submit button and privacy checkbox)
- Use the same border/background style as regular inputs — don't give textarea a special border
- Only exception: underline-style inputs paired with full-border textarea (Rains pattern) — not recommended; consistency is better

---

## Submit Button

### Full-Width Solid Button (Recommended Default)

**When to use**:
- Form width ≤ 560px (centered single-column or right side of split)
- Archetype A/B general contact forms

**Execution**:
```css
.form-submit {
    width: 100%;
    padding: 8px 16px;              /* slightly larger than nav CTA to increase click area */
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    background: var(--accent);       /* default = --text */
    color: var(--accent-text);       /* default = --text-inverse */
    border: none;
    border-radius: 2px;              /* button border-radius */
    cursor: pointer;
    transition: transform 0.2s ease-in-out;
    margin-top: 24px;
}

.form-submit:hover {
    transform: translateY(-1px);
}
```

**CTA copy** (by frequency):
1. "Send message" / "Send" — preferred for general contact forms
2. "Submit" — formal / neutral
3. "Request a demo" / "Book a demo" — Archetype C (Sales/Demo)
4. Branded copy (e.g., "Talk to [Brand]") — optional; adds brand feel

**Evidence**: 12/23 use full-width dark solid button
**Evidence status**: Cross-sample inference

---

### Non-Full-Width Button

**When to use**:
- Form is very wide (>600px) or occupies a large portion of space in a split layout
- Design preference for a more restrained CTA presentation

**Execution**:
```css
.form-submit-inline {
    /* same base styles as .form-submit */
    width: auto;
    padding: 12px 32px;             /* increased horizontal padding */
    /* default left-aligned (aligned with labels) */
}
```

**Variants**:
- **Left-aligned** (uncommon): Assembly Coffee — aligned with form content
- **Right-aligned**: FARFETCH — more formal business feel

**Evidence**: Assembly Coffee, FARFETCH and others — 5/23
**Evidence status**: Cross-sample inference

---

### Outline Button

**When to use**:
- Paired with underline input style for an overall lighter feel
- Page visual weight is on the heading or left-side content, not the button

**Execution**:
```css
.form-submit-outline {
    width: 100%;
    padding: 8px 16px;
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    background: transparent;
    color: var(--text);
    border: 1px solid var(--surface-2);
    border-radius: 2px;
    cursor: pointer;
    transition: border-color 0.3s linear;
    margin-top: 24px;
}

.form-submit-outline:hover {
    border-color: var(--text);
}
```

**Evidence**: Oevra, YLLW, Rains and others — 4/23
**Evidence status**: Cross-sample inference

---

## Two-Column Field Pairs

**When to use**:
- 5+ form fields; need to reduce vertical length
- Common in Archetype B/C

**Execution**:
```css
.form-row {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px;                       /* column gap */
}

@media (max-width: 480px) {
    .form-row {
        grid-template-columns: 1fr;  /* stack on narrow screens */
    }
}
```

**Pairable fields** (these combinations only):
- First Name + Last Name — most common pairing
- Email + Phone
- Company Name + Company Size (dropdown)
- Country + City

**Do not pair**:
- Email + Message (textarea is not suited to half-width)
- Any field + Textarea
- Subject dropdown + another dropdown (two dropdowns side by side are hard to distinguish)

**Vertical spacing between fields**:
```css
.form-group {
    margin-bottom: 24px;             /* between field groups */
}
```

**Evidence**: YLLW, FARFETCH, Vercel, Customer.io, Vizcom, Jasper and others — 9/23 use partial two-column
**Evidence status**: Cross-sample inference

---

## Privacy Checkbox and Legal Text

**When to use**:
- European markets or GDPR compliance requirements
- More common in Sales/Demo forms (data collection is more sensitive)

**Execution**:
```css
.form-privacy {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    margin-top: 16px;
}

.form-privacy input[type="checkbox"] {
    width: 18px;
    height: 18px;
    margin-top: 2px;
    accent-color: var(--text);
    flex-shrink: 0;
}

.form-privacy label {
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    line-height: 1.5;
}

.form-privacy a {
    color: var(--text);
    text-decoration: underline;
    opacity: 1;                          /* parent label is already opacity 0.5;
                                           setting opacity 0.5 here compounds to 0.25 */
}
```

**Copy patterns**:
- "I agree to the [Privacy Policy] and [Terms of Service]."
- "By submitting this form, you agree to our [Privacy Policy]."

**Variants**:
- **Text statement only** (no checkbox): Small text below the submit button. Reference: Savor, Vercel
- **Marketing opt-in**: An additional "Send me updates" checkbox (separate from privacy). Reference: Legora

**Evidence**: 8/23 (35%) include a privacy checkbox; Archetype C has a higher proportion
**Evidence status**: Cross-sample inference

---

## Form Width and Positioning Summary

| Layout | Max form width | Positioning | Applicable Archetype |
|--------|---------------|-------------|---------------------|
| Centered single-column | 560px | margin: 0 auto | A |
| Right side of split | 50% of 1080px (≈480px) | grid right column | A/B/C |
| Card container | 560px (including padding) | margin: 0 auto | A |
| Centered wide form | 720px | margin: 0 auto | B (with two-column fields) |

---

## Mobile Adaptation

```css
@media (max-width: 767px) {
    .contact-split {
        grid-template-columns: 1fr;
        gap: 48px;
    }

    .form-row {
        grid-template-columns: 1fr;
    }

    .contact-centered {
        max-width: 100%;
    }

    .form-submit,
    .form-submit-inline {
        width: 100%;                 /* buttons always full-width on mobile */
    }
}
```
