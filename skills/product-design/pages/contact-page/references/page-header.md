# Contact Page Header — Design Knowledge

> Layout, copy, and visual treatment of the Contact Page title area.

---

## Core Difference from Landing Page Hero

The Contact Page Header is **not** a Hero section:
- No value proposition needed — just state the page's purpose
- Title is shorter (2–5 words vs Landing Page's 5–12 words)
- No primary CTA button (the page itself is the action entry)
- Subtitle is **service-oriented** ("We're here to help you") rather than **value-oriented** ("Boost your efficiency")
- Less top whitespace: `80px` (vs Hero's `128px`)

---

## 1. Title Copy Strategy

### Three Patterns

| Pattern | Example | When to use |
|---------|---------|-------------|
| Direct | "Contact Us" / "Contact" | Archetype A/B — clear, unambiguous |
| Question | "How can we help?" | Archetype B/D — implies multiple help paths |
| Invitation | "Get in touch" / "Let's talk" | Archetype A/C — warmer, lower pressure |

**Selection rules**:
- Archetype A (Simple Contact) → Direct or Invitation
- Archetype B (Department Routing) → Question (guides user to choose a department)
- Archetype C (Sales-Focused) → Invitation or action-oriented ("Request a demo" / "Book a demo")
- Archetype D (Support Hub) → Question

### Token

```
Title font-size:     clamp(32px, 4vw, 47px)   /* Section title level, not Hero level */
Title font-weight:   500
Title letter-spacing: -0.02em
Title color:         var(--text); opacity: 1
```

**Exception**: Archetype C's "Request demo" can use Hero-level font-size `clamp(48px, 7vw, 80px)`, because the demo page is an independent entry point.

---

## 2. Label (Optional)

**When to use**: When the title itself doesn't contain the word "Contact" (e.g., question-style "How can we help?"), add a label above the title to make the page identity clear.

```
CONTACT
font-family: var(--font-mono)
font-size: 12px
font-weight: 400
letter-spacing: 0.72px
text-transform: uppercase
color: var(--text)
opacity: 0.4
margin-bottom: 16px
```

**When not to use**: When the title already contains "Contact" (e.g., "Contact Us") — no need for an additional label; it would be redundant.

---

## 3. Subtitle

**7 of 10 samples include a subtitle**. Content patterns:

- **State which teams can be reached**: "Get in touch with our sales and support teams for demos, onboarding support, or product questions."
- **Express a welcoming attitude**: "We love hearing from you. Reach out below and let us know how we can help."
- **State response commitment**: "Fill out the form and our team will get back to you shortly."

```
Subtitle font-size:   18px
Subtitle font-weight: 500 (Display) or 400 (Body)
Subtitle color:       var(--text); opacity: 0.5
max-width:            540px   /* controls line width; avoids overly wide text when centered */
margin-top:           24px    /* title to subtitle */
line-height:          1.6
```

**When not to use**: When the title is self-explanatory enough (e.g., "Contact Us" followed immediately by department cards), the subtitle can be omitted.

---

## 4. Layout Patterns

### 4.1 Centered Title (Most Common, 7/10)

```
text-align: center
padding-top: 80px
padding-bottom: 58px   /* to the first content section */
```

Works for Archetype A, B, D. Title + optional label + optional subtitle, arranged vertically centered.

### 4.2 Left-Aligned Title + Right Photo/Illustration (3/10)

```
display: flex
align-items: center
gap: 58px
padding-top: 80px
padding-bottom: 58px
```

Left side: title + subtitle (~55%)
Right side: photo or illustration (~45%)

Works for Archetype B (adds friendliness) or C (team photo adds trust).

**Note**: Photo should be a real office/team photo, not stock photos or AI-generated images (use placeholder in V1 scope).

### 4.3 Sales-Focused Split (Archetype C Only)

Title area and form are combined into a single unit:
```
Left side: title + description + social proof (customer logos / testimonials)
Right side: form
padding-top: 80px
```

In this pattern, there is no standalone "header" — the title and form are in the same section. See the split layout in `contact-form.md`.

---

## 5. Spacing Rules

```
Nav to top of Header:          80px   /* more compact than Landing Page Hero's 128px */
Label to title:                16px
Title to subtitle:             24px
Subtitle to next section:      58px
```

**Why more compact than Hero**: The Contact Page is a utility page (completing an action), not a showcase page (making a first impression). Users come here to do something, not to be impressed.
