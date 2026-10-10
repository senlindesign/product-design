# Contact Page Archetypes and Selection Guide

> Source: Mobbin research synthesis from 53 section-level observations across ~30 independent products

---

## Archetype Definitions

### A. Simple Contact

**Typical products**: Early-stage SaaS, open-source tools, personal products, creative studios, small agencies
**Core characteristics**: One form + basic contact information, no department routing, minimal

**Selection conditions**:
- Small team; all inquiries handled through a single entry point
- No need to route by department (or department structure is irrelevant to users)
- Contact page is not a critical node in the conversion funnel
- Product is early-stage or targets individual users

**Typical section composition**:
1. Navigation
2. Page Header (title + optional subtitle)
3. Contact Form (3–5 fields) + Contact Info (side by side or below)
4. FAQ (optional, 3–4 questions)
5. Footer

**Field count**: 3–5. Minimum set = Name + Email + Message. Can add Subject dropdown for simple categorization.

**Visual tendencies**:
- Light theme preferred
- Either layout works: left-right split (left info + right form) or centered single-column
- Generous spacing; whitespace matters more than content density
- No social proof, no qualification filtering
- If Contact Info is present, email is the core (100% required); address and phone are optional

**Observed products**: Framer, Webflow, Aave, Assembly Coffee, Yellowbird, Ragged Edge, Public

---

### B. Department Routing

**Typical products**: Mid-size SaaS (multi-team), B2B platforms, multi-office enterprises
**Core characteristics**: Multiple contact entry points; cards or dropdown guide users to the right department

**Selection conditions**:
- Team has clear division of responsibilities (Sales / Support / Partnerships / Press)
- Different departments need different contact methods or workflows
- Product is mature enough that routing inquiries improves response efficiency
- Users may not know who to contact

**Typical section composition**:
1. Navigation
2. Page Header (title + subtitle explaining what each department can help with)
3. Department Cards (2–4 cards, each with title + description + CTA)
4. Contact Info / Offices (optional; multiple office locations or general contact info)
5. FAQ (optional)
6. Footer

**Routing count**: 2–4 departments. 2 cards (Sales vs Support) is most common (4/10 samples). More than 4 requires reconsidering the information architecture.

**Visual tendencies**:
- Equal-width card grid layout (8/10 samples)
- Each card must have: title + description + CTA
- Differentiated CTA copy (8/10 samples), reflecting different actions rather than a unified "Contact Us"
- Sales card CTA uses primary (filled); Support card can use outline or text link
- Optional icon for visual distinction, but icons have no colored background
- Light or dark theme both viable

**Observed products**: Customer.io, Zendesk, GitBook, Mews, Sprout Social, Workable, Linear, TravelPerk

**Two routing implementations**:
1. **Card routing** (mainstream): Standalone cards; clicking navigates to different pages/forms. Suited for departments with entirely different workflows
2. **Form-internal routing** (lightweight): Single form + Subject/Reason dropdown or radio. Suited for departments where only the recipient differs (NEON uses radio, FARFETCH uses dropdown, Rains uses dropdown)

---

### C. Sales-Focused

**Typical products**: Enterprise SaaS, high-ticket products, B2B tools requiring a demo
**Core characteristics**: Demo booking is the primary goal; form includes qualification fields (company size, role, industry); left side features social proof

**Selection conditions**:
- Product requires a demo or sales conversation to convert
- High per-customer value makes detailed information collection worthwhile
- Has a sales team to handle inbound leads
- Need to qualify users before contact (company size, industry)

**Typical section composition**:
1. Navigation
2. Page Header / Form Section (left: title + description + social proof; right: form) — usually combined into one large section
3. Additional trust signals (optional; customer logo wall or testimonial)
4. FAQ (optional)
5. Footer

**Field count**: 5–9. Core fields = Work Email + Name + Company Name + Company Size (dropdown) + Message/textarea. Common additions: Phone, Industry, Role, "How did you hear about us?"

**Visual tendencies**:
- Left-right split is the only pattern (8/8 Sales form samples use this)
- Left side carries trust signals: customer logos (6/8 samples), quantified data ("24x faster builds"), testimonials, G2 badges
- Form is heavier than Archetype A (more fields + more dropdowns), so two-column layout is common (Name split into First/Last, Email + Phone side by side)
- CTA copy clearly states the action: "Request a demo" / "Book a demo" / "Talk to [ProductName]"
- Privacy/Terms text or checkbox is almost always present

**Observed products**: Vercel, Vanta, Customer.io (demo), Height, Legora, Vizcom, Antimetal, Jasper

---

### D. Support Hub

**Typical products**: Mature SaaS, products with comprehensive help documentation
**Core characteristics**: Self-service first (search, FAQ, help docs); contact form is the last resort

**Selection conditions**:
- Product has a well-developed Help Center / Knowledge Base
- Most user questions can be resolved through documentation
- Reducing support tickets is a business goal
- Users should attempt to search for answers before making contact

**Typical section composition**:
1. Navigation
2. Page Header + Search (title + search bar, guiding users to search first)
3. Help Categories (category cards or link list for common topics)
4. Contact Fallback (contact entry at the bottom, explicitly positioned as "Still need help?")
5. Footer

**Visual tendencies**:
- Search bar is the visual focal point of the page (pill shape, `border-radius: 160px`)
- Help categories use card grid or list
- Contact entry is de-emphasized — not first-screen content; appears after help categories
- Hierarchical card pattern: primary support channel occupies a full row (e.g., Product Support); secondary channels share a row
- May include system status indicator ("All systems operational")

**Observed products**: Framer (Support Hub variant)

**Note**: Direct Support Hub samples are limited (1 sample), but multiple Department Routing samples include Support Hub elements (Mews's Help Center card, Zendesk's "Go to help center" CTA). Implementation primarily follows general Help Center patterns.

---

## Selection Flow

```
1. What is the page's primary goal?
   ├── Collect sales leads / book a demo → C. Sales-Focused
   ├── Guide users to resolve issues themselves → D. Support Hub
   └── Provide contact information
       ├── Need to route by department?
       │   ├── Yes, and departments have different workflows → B. Department Routing (card routing)
       │   ├── Yes, but only the recipient differs → A. Simple Contact + Subject dropdown
       │   └── No → A. Simple Contact
       └── Unsure → A. Simple Contact

2. After selecting an archetype, verify with corrections:
   - Need demo but small team? → A + add Company/Role fields (no need to upgrade to C)
   - B has only 2 departments (Sales + Support)? → 2 cards are enough; don't pad to 4
   - C but product targets individual users? → Downgrade to A; remove company size/industry fields
   - D but no Help Center content? → Downgrade to B or A
```

---

## Cross-Archetype Common Rules

Regardless of which archetype is chosen:

1. **Email is a required field**: 100% of contact forms include an email input. No email field = structural error
2. **CTA copy reflects the specific action**: Don't use "Submit" for all forms. General contact → "Send message"; Demo → "Request a demo"; Sales → "Talk to [ProductName]"
3. **Input fields consistently use full border style**: `border: 1px solid var(--surface-2); border-radius: 4px`. Although underline-only accounts for 26% of observations, our design system explicitly defines input border-radius as 4px, which implies full border
4. **Page header doesn't need a value proposition**: 2–5 words is sufficient ("Contact us" / "Get in touch"); no need to communicate product value like a Landing Page Hero
5. **Don't fabricate contact information**: If the user hasn't provided email/phone/address, use "[email]" / "[phone]" placeholders and note them in the delivery notes
6. **Mobile adaptation**: Left-right split layouts must stack to single-column on narrow screens (form above or below depending on content priority); Department cards stack vertically on narrow screens
