# Billing Toggle — Design Knowledge

> Source: Mobbin research synthesis across 65+ SaaS product Pricing Page billing toggle components

---

## Pattern 1: Pill Toggle (Recommended Default)

**When to use**:
- Product offers both Monthly and Annual billing options
- Annual plan has a discount (typically 15–20%)
- Need to guide users toward choosing annual billing

**Execution**:

**Position**: centered, after the Header and before the Tier Cards — 48px spacing from the bottom of the header, 24px from the top of the tier cards.

**Toggle Token**:
```css
.billing-toggle {
    display: inline-flex;
    align-items: center;
    background: var(--surface-1);       /* #F5F5F5 (Light) / #141414 (Dark) */
    border-radius: 40px;               /* pill shape */
    padding: 4px;
    margin: 0 auto;
}

.billing-option {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    padding: 8px 16px;
    border-radius: 36px;               /* inner pill */
    border: none;
    background: transparent;
    color: var(--text);
    opacity: 0.5;
    cursor: pointer;
    transition: opacity 0.3s linear, background 0.3s linear;
}

.billing-option.active {
    background: var(--text);            /* #141414 (Light) / #EDEDED (Dark) */
    color: var(--text-inverse);         /* #FFFFFF (Light) / #0A0A0A (Dark) */
    opacity: 1;
}
```

**Size**: overall height 36–40px (padding 4px + option height 28–32px).

**Default state**: Annual selected by default (shows the lower monthly-equivalent price; promotes annual billing conversion).

**Variants**:
- **Inverted scheme**: active option uses `background: var(--bg); border: 1px solid var(--surface-2)`, inactive stays transparent. More subtle
- **No background scheme**: no pill container; two text options + underline / bottom indicator bar to show active state

**Evidence**: Notion, Linear, Vercel, GitHub, Slack and 15+ other products
**Evidence status**: Cross-sample inference

---

## Pattern 2: Tab Toggle

**When to use**:
- Product has multiple billing dimensions or plan categories (not only monthly / annual)
- Example: Plans vs API / Site vs Workspace / Individual vs Team

**Execution**:
```css
.billing-tabs {
    display: flex;
    gap: 0;
    border-bottom: 1px solid var(--surface-2);
    margin: 0 auto;
    max-width: max-content;
}

.billing-tab {
    font-family: var(--font-display);
    font-size: 14px;
    font-weight: 500;
    padding: 12px 24px;
    border: none;
    background: transparent;
    color: var(--text);
    opacity: 0.5;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    margin-bottom: -1px;
    transition: opacity 0.3s linear;
}

.billing-tab.active {
    opacity: 1;
    border-bottom-color: var(--text);
}
```

**When not to use**:
- Only two options (Monthly / Annual) — pill toggle is more compact
- 3+ tabs on mobile would be too cramped — consider a dropdown instead

**Evidence**: Vercel (Hobby/Pro/Enterprise tabs), Supabase
**Evidence status**: Cross-sample inference

---

## Discount Badge

**Position**: adjacent to the right of the Annual option, or below the toggle.

```css
.discount-badge-toggle {
    display: inline-block;
    font-family: var(--font-mono);
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0.72px;
    text-transform: uppercase;
    color: var(--text);
    opacity: 0.5;
    background: var(--surface-1);
    padding: 4px 8px;
    border-radius: 4px;              /* same spec as tier-cards.md .discount-badge */
    margin-left: 8px;
    vertical-align: middle;
}
```

**Text**: "SAVE 20%" or "-20%" — concise; no full sentences.

**Do not use**:
- Brand color / accent color background
- Animation effects (pulse, glow)
- Font size larger than 12px

---

## Linking Toggle to Tier Cards

When the toggle switches, prices in tier cards should update immediately (no page reload):
- Annual selected: display monthly-equivalent price + "/mo" + note "billed annually" below (12px / mono / 0.4 opacity)
- Monthly selected: display monthly price + "/mo", remove "billed annually" note

**Implementation — JS stub** (vanilla JS, no framework required):

Each price element needs two data attributes:
```html
<span class="price-amount" data-monthly="29" data-annual="19">$19</span>
<span class="price-billing-note">billed annually</span>
```

```js
(function() {
    var options = document.querySelectorAll('.billing-option');
    var prices  = document.querySelectorAll('.price-amount');
    var notes   = document.querySelectorAll('.price-billing-note');

    function setMode(mode) {
        options.forEach(function(btn) {
            btn.classList.toggle('active', btn.dataset.billing === mode);
        });
        prices.forEach(function(el) {
            el.textContent = '$' + (mode === 'annual' ? el.dataset.annual : el.dataset.monthly);
        });
        notes.forEach(function(el) {
            el.style.display = (mode === 'annual') ? '' : 'none';
        });
    }

    options.forEach(function(btn) {
        btn.addEventListener('click', function() { setMode(btn.dataset.billing); });
    });

    setMode('annual'); // default: annual selected
})();
```

Attach `data-billing="monthly"` / `data-billing="annual"` to each `.billing-option` button. The initial display value in HTML should match the default mode (`annual`) so pages render correctly without JS.

**When billing toggle is not needed**:
- User provided only one set of prices (e.g., monthly only) and did not ask for a toggle — never invent annual prices to fill one
- Product has only one billing period (monthly-only or annual-only)
- Usage-based product with no monthly / annual distinction; only pay-as-you-go
- Product has only one pricing plan (Simple Binary with a single paid tier and no billing cycle choice)
