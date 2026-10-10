# Contact Info — Design Knowledge

> Source: Mobbin research synthesis from 10 product Contact Info sections + contact information embedded in contact-form samples

---

## Information Types and Priority

**Observed occurrence frequency**:
- **Email**: 100% — required; the most fundamental contact method
- **Address**: 80% — companies with physical offices almost always display it
- **Phone**: 60% — more common in B2B products; less common in SaaS tools
- **Social links**: 20% — usually a supplement, not a primary contact method
- **Business hours**: 10% — only in retail/service businesses

**Field priority rules**:
1. Always list email first (the method users are most likely to use)
2. When there is a physical office, listing the address is required
3. Phone is optional — SaaS products omitting phone is normal
4. Social links come last as a supplement, not a primary contact channel
5. A specific contact person's name can increase trust, but is only common in small teams or agencies

---

## Pattern 1: In the Same Section as the Form — Sidebar Information

**When to use**:
- In a split layout, contact info is placed opposite the form (usually left side)
- Limited amount of information (email + address + optional phone)
- Works for Archetype A/B in general

**Execution**:

```css
.contact-details {
    display: flex;
    flex-direction: column;
    gap: 32px;
    margin-top: 48px;                /* spacing from description text */
}

.contact-detail-item {
    /* no border, no background — plain text */
}

.contact-detail-label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 8px;
}

.contact-detail-value {
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 500;
    color: var(--text);
    line-height: 1.5;
}

.contact-detail-value a {
    color: var(--text);
    text-decoration: none;
    transition: opacity 0.3s linear;
}

.contact-detail-value a:hover {
    opacity: 0.5;
}
```

**HTML structure**:
```html
<div class="contact-details">
    <div class="contact-detail-item">
        <div class="contact-detail-label">Email</div>
        <div class="contact-detail-value">
            <a href="mailto:hello@company.com">hello@company.com</a>
        </div>
    </div>
    <div class="contact-detail-item">
        <div class="contact-detail-label">Address</div>
        <div class="contact-detail-value">
            123 Street Name<br>
            City, State 10001
        </div>
    </div>
    <div class="contact-detail-item">
        <div class="contact-detail-label">Phone</div>
        <div class="contact-detail-value">
            <a href="tel:+11234567890">+1 (123) 456-7890</a>
        </div>
    </div>
</div>
```

**Variants**:
- **Table-style layout**: Label and value on the same line; suited for many information types. `display: grid; grid-template-columns: 120px 1fr;`. Reference: Ragged Edge
- **With copy button**: Each row has a "Copy" button on the right to copy the contact method. Reference: Ragged Edge

**When not to use**:
- More than 3 types of contact information — the sidebar can't fit it all; consider a standalone section
- Sales/Demo forms — the left side should have social proof (customer logos / testimonials), not contact info

**Evidence**: Maxima Therapy, Savor, Yellowbird, Ragged Edge
**Evidence status**: Cross-sample inference

---

## Pattern 2: Standalone Contact Info Section

**When to use**:
- Contact information is rich (multiple channels, multiple departments, has an address)
- Needs visual separation from the form
- Usually below the form section

**Execution**:

```css
.contact-info-section {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.contact-info-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}

@media (max-width: 767px) {
    .contact-info-grid {
        grid-template-columns: 1fr;
        gap: 32px;
    }
}
```

**Variants**:
- **3-column channel cards**: Email / Chat / Support each occupies one column. Reference: Homerun
- **Left heading + right content**: Left column holds a "Contact us" heading; middle and right columns hold specific information. Reference: Public

**Evidence**: Homerun, Public, Kinfolk
**Evidence status**: Cross-sample inference

---

## Pattern 3: Multi-Office Display

**When to use**:
- Company has 2–4 office locations
- Need to convey international presence / multi-region coverage

**Execution**:

**2–3 offices — side-by-side display**:
```css
.offices-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 24px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.office-card {
    /* no border, no shadow, no background — plain text group */
}

.office-city {
    font-family: var(--font-display);
    font-size: 20px;
    font-weight: 500;
    color: var(--text);
    letter-spacing: -0.4px;
    margin-bottom: 16px;
}

.office-address {
    font-family: var(--font-body);
    font-size: 16px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    line-height: 1.6;
    margin-bottom: 12px;
}

.office-contact {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
}

.office-contact a {
    color: var(--text);
    text-decoration: none;
    transition: opacity 0.3s linear;
}

.office-contact a:hover {
    opacity: 0.5;
}
```

**Variants**:
- **With timezone display**: City name followed by GMT offset (e.g., "New York (GMT-4)") — suited for international clients. Reference: Mother Design
- **With office photo**: City/building photo above address info for a human touch. Reference: Pentagram, Mother Design, TravelPerk
- **With "Get directions" link**: Text link pointing to Google Maps. Reference: Pentagram, Homerun

**Evidence**: Mother Design, Pentagram, Kinfolk, TravelPerk
**Evidence status**: Cross-sample inference

---

**5+ offices — region-grouped list**:

**When to use**:
- Global enterprise with offices across multiple continents
- High information density; card display is not suitable

**Execution**:
```css
.offices-region {
    margin-bottom: 48px;
}

.offices-region-label {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--surface-2);
    margin-bottom: 24px;
}

.offices-list {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 24px;
}
```

**When not to use**:
- 10+ offices — consider a searchable list or map view (map not implemented in V1)

**Evidence**: SIGMA
**Evidence status**: Single sample; cannot be generalized as a common pattern

---

## Pattern 4: Department Contact List

**When to use**:
- Company handles different types of inquiries by function (General / Sales / Press / Wholesale)
- Common in agencies and media companies
- Mutual alternative with the form's Subject/Reason dropdown routing — either use a dropdown for form-internal routing, or use a department list so users can directly find the right contact

**Execution**:
```css
.departments-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 24px;
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.department-item {
    padding-bottom: 24px;
    border-bottom: 1px solid var(--surface-2);
}

.department-name {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 12px;
}

.department-description {
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 400;
    color: var(--text);
    opacity: 0.5;
    line-height: 1.5;
    margin-bottom: 8px;
}

.department-email {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
}

.department-email a {
    color: var(--text);
    text-decoration: none;
    transition: opacity 0.3s linear;
}

.department-email a:hover {
    opacity: 0.5;
}
```

**Variants**:
- **With specific contact person name**: Each department lists a person in charge (name + title + email + phone). Adds trust and a human touch. Reference: Aino Agency
```css
.department-person {
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 500;
    color: var(--text);
    margin-bottom: 6px;
}

.department-role {
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    text-transform: uppercase;
    letter-spacing: 0.72px;
    color: var(--text);
    opacity: 0.4;
    margin-bottom: 8px;
}
```

- **OFFICES + CONTACT binary**: First list office locations, then list department contact info — two areas distinguished by different section labels. Reference: Kinfolk

**When not to use**:
- More than 6 departments — page becomes too long; consider using tabs or accordion groups
- Already have Subject dropdown in the form for routing — don't provide both a department list and a dropdown; choose one

**Evidence**: Kinfolk, Aino Agency
**Evidence status**: Cross-sample inference. Limited samples (2), but pattern is clear

---

## Social Links Handling

**When to use**:
- Brand is active on multiple social platforms
- As a supplement to contact information, not a replacement

**Execution**:
```css
.social-links {
    display: flex;
    gap: 16px;
    align-items: center;
    margin-top: 24px;
}

.social-links a {
    color: var(--text);
    opacity: 0.3;
    transition: opacity 0.3s linear;
    font-size: 18px;                 /* icon size */
    text-decoration: none;
}

.social-links a:hover {
    opacity: 0.7;
}
```

**Rules**:
- Social icons use text color + low opacity (0.3); hover raises to 0.7
- Don't use each platform's brand color (Twitter blue, Instagram pink, etc.) — maintain monochrome
- Ordering by platform importance: LinkedIn > X/Twitter > Instagram > Facebook > YouTube > GitHub
- For technical products: GitHub > X/Twitter > Discord > LinkedIn
- Display at most 4–6 icons; too many is distracting
- V1 uses Unicode symbols or simple SVG; no icon library

**Evidence**: Public (6 social icons), Pentagram
**Evidence status**: Limited samples (2/10), but pattern is clear

---

## Section Relationships

**Position combinations for Contact Info and Contact Form**:

| Combination | When to use | Notes |
|-------------|-------------|-------|
| Sidebar embed (left side of split) | Archetype A/B, small amount of info | Contact info is to the left of the form, same section |
| Standalone section (below form) | Archetype A/B, large amount of info | Form and contact info each occupy a section, 180px apart |
| Pre-form hint line | Archetype A, has email/FAQ link | A single sentence before the form providing a direct contact method or FAQ link |
| Contact info only (no form) | Archetype B multi-office / multi-department | No form; department email list is the contact method |

**Rules**:
- If the left side of a split layout has social proof (Sales/Demo form), contact info should be placed separately in the Footer or a standalone section
- Don't repeat the same email or address in multiple places on the same page
- FAQ section (if present) usually goes after the contact info or form section

---

## Mobile Adaptation

```css
@media (max-width: 767px) {
    .contact-info-grid,
    .offices-grid,
    .departments-grid,
    .offices-list {
        grid-template-columns: 1fr;
        gap: 32px;
    }

    .social-links {
        justify-content: center;     /* center social icons */
    }
}
```
