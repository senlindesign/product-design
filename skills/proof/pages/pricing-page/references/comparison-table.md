# Comparison Table — Design Knowledge

> Source: Mobbin research synthesis across 65+ SaaS product Pricing Page feature comparison tables

---

## When to Include a Comparison Table

| Archetype | Include? | Reason |
|-----------|----------|--------|
| A. Feature-Tiered | **Almost always** | 4+ feature differences across tiers; users need detailed comparison to choose |
| B. Usage-Based | **Usually** | Focuses on usage limits / quotas rather than features, but format is similar |
| C. Simple Binary | **Usually omitted** | Only 2 tiers; feature differences can be written directly in the cards |
| D. Enterprise-First | **Case by case** | Include if there are public tiers; omit if all is "Contact Sales" |

**When not to use**:
- Fewer than 4 feature differences — write them directly in the tier card feature lists
- All tiers have the same features; only usage limits differ — use a limits table instead
- Page overall aims for simplicity (Archetype C)

---

## Pattern 1: Full-Width Comparison Table (Recommended Default)

**When to use**:
- 3–4 tiers to compare
- 10–30 features
- Features need to be displayed in categories

**Execution**:

**Container Token**:
```css
.comparison-table-section {
    max-width: 1080px;
    margin: 0 auto;
    padding: 0 32px;
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    /* table itself has no border */
}
```

**Header Token** (plan name row):
```css
.comparison-table thead th {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    text-align: center;
    padding: 16px 12px;
    border-bottom: 1px solid var(--surface-2);
    position: sticky;
    top: 0;
    background: var(--bg);
    z-index: 10;
}

.comparison-table thead th:first-child {
    text-align: left;                    /* feature name column left-aligned */
    width: 35%;                          /* enough space for feature names */
}
```

**Category Header Token** (feature category heading row):
```css
.comparison-table .category-header td {
    font-family: var(--font-display);
    font-size: 16px;
    font-weight: 500;
    color: var(--text);
    padding: 32px 0 16px 0;             /* 32px above to separate categories */
    border-bottom: 1px solid var(--surface-2);
    /* optional: small icon before category */
}
```

**Data Row Token**:
```css
.comparison-table tbody tr {
    border-bottom: 1px solid var(--surface-2);
}

.comparison-table tbody td {
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 400;
    color: var(--text);
    padding: 16px 12px;
    line-height: 1.5;
}

.comparison-table tbody td:first-child {
    text-align: left;                    /* feature name */
}

.comparison-table tbody td:not(:first-child) {
    text-align: center;                  /* value columns centered */
}
```

**Evidence**: Notion, Linear, Slack, GitHub, Asana and 15+ other products
**Evidence status**: Cross-sample inference

---

## Check Mark & Value Display

```css
/* Feature present */
.check-yes {
    color: var(--text);
    opacity: 0.4;
    font-size: 16px;
    /* use ✓ character, not emoji or colorful icon */
}

/* Feature absent */
.check-no {
    color: var(--text);
    opacity: 0.2;
    font-size: 16px;
    /* use — character (em dash) */
}

/* Text value (e.g., "10GB", "Unlimited", "Up to 5") */
.value-text {
    font-family: var(--font-body);
    font-size: 14px;
    font-weight: 400;
    color: var(--text);
    /* opacity 1 — text values need full readability */
}
```

**Rules**:
- Boolean values use ✓ / — ; do not use Yes/No or ✓/✗
- Usage values written as plain text ("10GB", "Unlimited", "Up to 5 users")
- Do not use green for ✓; do not use red for — — follow system grayscale

---

## Pattern 2: Expandable Comparison

**When to use**:
- More than 15 features
- Don't want to show the full table on initial load (avoids excessive length)
- Users can expand on demand

**Execution**:
```css
.expand-trigger {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    color: var(--text);
    opacity: 0.5;
    background: none;
    border: none;
    cursor: pointer;
    padding: 16px 0;
    transition: opacity 0.3s linear;
}

.expand-trigger:hover {
    opacity: 1;
}
```

**Position**:
- "Compare all features" button / link placed below the tier cards and above the comparison table
- Or inside the comparison table section: show core features by default (5–8), expand to show all on click

**When not to use**:
- Fewer than 10 features — display all; no need to collapse

---

## CTA in Table Header

**When to use**:
- Comparison table is long (scroll distance exceeds one screen)
- Need to provide an action entry immediately after users finish comparing

**Execution**:
```css
.comparison-table thead .plan-cta {
    font-size: 12px;                     /* smaller than normal button */
    padding: 6px 12px;
    margin-top: 8px;
}
```

In the sticky header, place a small CTA button under each plan column (recommended tier uses `.btn-dark`; others use `.btn-outline`).

---

## Mobile Adaptation

**Option A: Sticky first column + horizontal scroll**
```css
@media (max-width: 767px) {
    .comparison-table-wrapper {
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
    }
    .comparison-table td:first-child,
    .comparison-table th:first-child {
        position: sticky;
        left: 0;
        background: var(--bg);
        z-index: 5;
        min-width: 160px;
    }
}
```

**Option B: Stack by plan into cards**
- Each plan becomes a standalone feature list card
- Suited for ≤ 3 plans

---

## Feature Category Suggestions

Common categories (use as category header):

| Category | Typical features |
|----------|-----------------|
| Core Features | Projects, tasks, views, templates |
| Collaboration | Members, sharing, real-time editing |
| Storage & Limits | Storage, file upload, API calls, rows |
| Admin & Security | SSO, SAML, audit logs, 2FA |
| Support | Email, chat, dedicated AM, SLA |
| Integrations | API access, webhooks, Zapier, custom |

**Rules**:
- 10+ features must be categorized — an uncategorized long list is hard to scan
- 3–8 features per category
- Category order: core features at the top, security / support at the bottom
