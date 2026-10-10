# How It Works Section — Design Knowledge

> Source: Mobbin research across 20 SaaS product Landing Page How It Works sections (2026-09-28)

---

## Pattern 1: Horizontal Three Steps (Most Common)

**When to use**:
- Product usage flow can be summarized in 3 simple steps
- Each step description is short (1–2 sentences)
- Desktop has sufficient width to display them side by side

**Execution**:
- Three equal-width columns; each column: number → step title → description text
- Number style choices: filled circle with number (1, 2, 3) or double-digit number (01, 02, 03)
- Step titles start with a verb ("Choose...", "Set up...", "Start...")
- Optional: each step accompanied by an icon or small screenshot
- On narrow screens, three columns collapse to vertical stacking

**Variants**:
- **With product screenshot**: product UI screenshot below each step (Sequence, Airtasker) — makes the flow concrete instead of abstract
- **With CTA**: CTA button below or alongside the steps (Wise, Apollo) — take action immediately after understanding the flow
- **Minimal text only**: no icons, no illustrations; pure numbers + title + description (Visitors) — suited for developer tools

**When not to use**:
- Step descriptions are long (3+ sentences needed to explain each step) → use vertical list
- Steps have complex branches or conditions → not suited for linear display

**Evidence**: ClassPass, Givingli, Visitors, Mora, Teak, Grammarly and 10 other products (75% use this pattern)
**Evidence status**: Cross-sample inference

---

## Pattern 2: Vertical List

**When to use**:
- Step descriptions are long or there are clear sequential dependencies between steps
- Need to place detailed explanations or screenshots alongside each step
- 3–4 steps

**Execution**:
- Each step occupies one row or block
- Number + title + description arranged vertically
- Steps separated by spacing or dividers
- Can be wrapped in a card container (Railway style)

**Evidence**: Railway, Apollo, Duolingo
**Evidence status**: Observed

---

## Key Design Decisions

### Step Count
- **3 steps**: 75% of samples use this. Suitable for most SaaS products
- **4 steps**: 25% of samples. Suitable for products with a slightly more complex flow
- No 2-step or 5+ step designs observed. If the flow is truly only 2 steps, a How It Works section may not be necessary

### Step Content Types
| Type | Description | When to use | Example |
|------|-------------|-------------|---------|
| **Action type** | What the user needs to do | Self-serve sign-up products | "Sign up", "Paste the script", "Watch visitors" |
| **Value type** | What the product delivers | B2B / service-type products | "Kickoff", "Model", "Strategize" |

### Number Style
Choose a number style that matches the brand tone:
- **Filled circle + number** (1, 2, 3): friendly, clear. Circle uses `var(--surface-1)` background + `var(--text)` number — do NOT use `var(--accent)` as circle fill (prohibited per visual-style.md §1 "icon backgrounds, badge fills")
- **Double-digit number** (01, 02, 03): modern, design-conscious. Suited for design-oriented brands
- **"Step X" text label**: explicit, formal. Suited for educational / process-oriented products
- **Large typographic number**: decorative and expressive. Suited for visually expressive pages

### Headline Choices
| Headline | Tone |
|----------|------|
| "How it works" | Direct and clear (default choice) |
| "How to get started" | More action-oriented |
| "Get started in three easy steps" | Emphasizes simplicity |
| "Wondering how...?" | Empathetic, conversational |

### Whether to Include Product Screenshots
- With screenshots (~45%): makes the flow concrete. Suited when the product UI is attractive and clearly illustrates the step
- Without screenshots (~55%): pure text / icons. Suited when the flow is simple or the product UI isn't a selling point

### Difference from Features
- Features answers "what can the product do" — capability-oriented
- How It Works answers "how do users start / use it" — process-oriented
- When both are needed: Features comes first (builds interest), How It Works comes after (lowers the action threshold)
- If the product features are themselves the process (e.g., sign up in 3 steps and it's ready), choose one or the other
