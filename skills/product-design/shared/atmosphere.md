# Atmosphere — Backgrounds and Texture

> Recipes for the one place a style is allowed atmosphere: the hero stage (and at most one bento tile). Each recipe lists when to use it, which styles may use it, and copy-ready code. Colors come only from the active style's DNA palette; derived tints use `color-mix()` of those colors.

## Rules for every recipe

1. **Texture never competes with text.** Heading and body text sit on a calm area (the light glow in Recipe 1, the upper sky in Recipe 2). Halftone and paper cutouts stay out of the text column. Check contrast of text against the lightest and darkest point behind it (≥ 4.5:1 body, ≥ 3:1 large).
2. **At least three hues + one light glow** for any gradient. A two-stop blue → violet linear gradient is the generic-AI look; never use it.
3. **No heavy JS by default.** Every recipe is pure CSS / inline SVG. Recipe 3b (WebGL) is an optional enhancement with a CSS fallback.
4. **Nothing moves.** Gradients, grain, clouds, and cutouts are static. If an enhancement animates, it is off under `prefers-reduced-motion: reduce`.
5. **Decorative layers are `aria-hidden="true"` and `pointer-events: none`.**

| Recipe | Minimal | Business | Colorful | Editorial |
|---|---|---|---|---|
| 1 Mesh gradient stage | — | ✅ hero stage + 1 bento tile | — | — |
| 2 Sky with grain | — | — | ✅ hero scene | — |
| 3 Halftone dots (CSS / Paper Shaders) | — | grain only (Recipe 1) | ✅ clouds | — |
| 4 Paper collage cutouts | — | — | ✅ only | — |
| 5 Floating app-icon tiles | — | ✅ only | — | — |

---

## Recipe 1 — Mesh gradient stage (Business)

**When**: the Business hero product stage (§10), and optionally one bento lead tile. **Not** on the page shell, text, or sections.

**Palette** (Calendly Scheduling hero SVG): `#175295`, `#1E5EA7`, `#4890E3`, `#6BB1FF`, `#5DDFD7`, `#B89FFA`, `#EBB0FF`. Layout, after the Calendly reference: sky blue top-left, lavender/pink bottom-left, mint/aqua right, a white glow behind the product card. The deep blues (`#175295`, `#1E5EA7`) are for small accents only, never a large field. If the user supplies brand colors, keep the structure (3+ hues + glow) and swap the hues.

```css
.mesh-stage {
  position: relative; isolation: isolate; overflow: hidden;
  border-radius: 48px;                                         /* Business §4 product stage */
  background:
    radial-gradient(38% 46% at 50% 62%, rgba(255,255,255,.95) 0%, rgba(255,255,255,0) 100%),  /* glow behind card */
    radial-gradient(48% 70% at 4% 6%,   #6BB1FF 0%, transparent 72%),                          /* sky top-left */
    radial-gradient(40% 60% at 30% 0%,  color-mix(in srgb, #4890E3 55%, #FFFFFF) 0%, transparent 70%),
    radial-gradient(46% 70% at 0% 100%, #B89FFA 0%, transparent 72%),                          /* lavender bottom-left */
    radial-gradient(40% 60% at 32% 104%,#EBB0FF 0%, transparent 70%),                          /* pink */
    radial-gradient(46% 72% at 100% 78%,#5DDFD7 0%, transparent 72%),                          /* mint right */
    radial-gradient(40% 55% at 96% 4%,  color-mix(in srgb, #6BB1FF 60%, #5DDFD7) 0%, transparent 70%),
    color-mix(in srgb, #6BB1FF 22%, #FFFFFF);                                                  /* base */
}
.mesh-stage::after {                                           /* fine grain: removes gradient banding */
  content: ""; position: absolute; inset: 0; z-index: -1; pointer-events: none;
  opacity: .12; mix-blend-mode: soft-light;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

**Frosted ring** — a translucent band between the mesh and the white card (Calendly: the card sits in a frosted frame):

```css
.frost-ring {
  position: relative; width: 74%; margin: 0 auto; padding: 12px 12px 0;
  border-radius: 52px 52px 0 0;                                /* card radius 40 + ring 12 */
  background: rgba(255,255,255,.38);
  border: 1px solid rgba(255,255,255,.7); border-bottom: 0;
  -webkit-backdrop-filter: blur(12px); backdrop-filter: blur(12px);   /* same blur value as nav */
}
.frost-ring > .card { background: #FFFFFF; border-radius: 40px 40px 0 0; }  /* Business §4 nested 48 → 40 */
```

**Dark theme**: drop the base color and the white glow; keep the hue radials at `color-mix(in srgb, <hue> 45%, transparent)` over `var(--surface-1)`. The ring becomes `rgba(255,255,255,.06)` with `inset 0 0 0 1px var(--surface-2)`.

---

## Recipe 2 — Sky with grain (Colorful)

**When**: the Colorful hero `.scene` (Craft "Sky / periwinkle field" `#B8CAF5`). The sky is deepest at the top and lightens toward the horizon where the product sits.

```css
.sky {
  position: relative; isolation: isolate; overflow: hidden;
  margin: 0 20px; border-radius: 24px;                         /* Colorful 20px canvas inset, §4 scene */
  background: linear-gradient(180deg,
    color-mix(in srgb, #B8CAF5 88%, #4890E3) 0%,               /* zenith: a touch deeper than the DNA sky */
    #B8CAF5 38%,                                               /* DNA sky */
    color-mix(in srgb, #B8CAF5 45%, #FCF9F7) 78%,              /* horizon haze toward canvas */
    color-mix(in srgb, #B8CAF5 25%, #FCF9F7) 100%);
}
.sky-grain {                                                   /* <div class="sky-grain" aria-hidden="true"> */
  position: absolute; inset: 0; z-index: 0; pointer-events: none;
  opacity: .22; mix-blend-mode: overlay;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='200' height='200'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3CfeColorMatrix type='saturate' values='0'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```

Note: `#4890E3` in the zenith tint is borrowed from the Calendly palette because Craft's DNA records only one sky value (gap — see end). Text contrast: `#030302` on the zenith tint ≈ 12:1.

**Faint giant outline wordmark** — the product name, behind the product, outline only:

```css
.wordmark { position: absolute; z-index: 0; left: 50%; transform: translateX(-50%); top: 470px; pointer-events: none;
  font-family: var(--font-display); font-weight: 400; font-size: 340px; line-height: 1; white-space: nowrap;
  color: transparent; -webkit-text-stroke: 1px rgba(3,3,2,.22); }
@media (max-width: 767px) { .wordmark { font-size: 140px; } }
```

Only the product's real name; never a slogan. Must sit below the CTA, never behind body text.

---

## Recipe 3a — Halftone dots, pure CSS (default)

**When**: Colorful soft clouds at the scene edges, or a fading dot field. Works offline, zero JS.

```html
<div class="ht-cloud cloud-a" aria-hidden="true"></div>
```
```css
.ht-cloud { position: absolute; z-index: 0; pointer-events: none; }
.ht-cloud::before, .ht-cloud::after { content: ""; position: absolute; inset: 0; -webkit-mask: var(--cloud); mask: var(--cloud); }
.ht-cloud::before { background: rgba(255,255,255,.55); filter: blur(14px); }                       /* soft body */
.ht-cloud::after  { background: radial-gradient(circle, #FFFFFF 1.3px, transparent 1.9px) 0 0 / 5px 5px; } /* dots */
.cloud-a { left: -60px; top: 230px; width: 300px; height: 230px;
  --cloud: radial-gradient(closest-side at 35% 60%, #000 55%, transparent),
           radial-gradient(closest-side at 65% 40%, #000 50%, transparent),
           radial-gradient(closest-side at 55% 75%, #000 45%, transparent); }
.cloud-b { right: -40px; top: 120px; width: 260px; height: 170px;
  --cloud: radial-gradient(closest-side at 40% 55%, #000 50%, transparent),
           radial-gradient(closest-side at 68% 45%, #000 50%, transparent); }
```

Clouds bleed off the left/right edges; keep them out of the centered text column (max 2–3 per hero). For a **fading dot field** instead of clouds, use one mask: `--cloud: linear-gradient(180deg, #000, transparent 70%)` with dots at `rgba(3,3,2,.08)`.

## Recipe 3b — Halftone dots, Paper Shaders (optional enhancement)

Verified 2026-10-09 against `@paper-design/shaders@0.0.81` in headless Chrome. The halftone shader is an **image filter**: it needs an `HTMLImageElement` (`u_image`), so we paint a cloud silhouette on a canvas and feed it in. Dot size follows luminance, so with `u_inverted: true` bright cloud areas get white dots. All sizing uniforms must be passed (the vertex shader reads them). `speed = 0` → renders once, no animation loop.

```html
<div class="sky">
  <div class="ht-shader" aria-hidden="true"></div>   <!-- inset:0, z-index:0, pointer-events:none -->
  <div class="ht-cloud cloud-a" aria-hidden="true"></div>  <!-- CSS fallback, hidden when shader runs -->
  ...
</div>
<script type="module">
const host = document.querySelector('.ht-shader');
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
if (host && !reduce) {
  try {
    const { ShaderMount, halftoneDotsFragmentShader, getShaderColorFromString, ShaderFitOptions } =
      await import('https://cdn.jsdelivr.net/npm/@paper-design/shaders@0.0.81/+esm');
    const c = document.createElement('canvas'); c.width = 720; c.height = 500;
    const x = c.getContext('2d'); x.fillStyle = '#000'; x.fillRect(0, 0, 720, 500);
    x.filter = 'blur(30px)'; x.fillStyle = '#fff';
    [[110,220,90],[190,190,110],[260,240,80],[600,120,70],[660,150,80]]   // cloud puffs [x, y, r]
      .forEach(([cx, cy, r]) => { x.beginPath(); x.arc(cx, cy, r, 0, 7); x.fill(); });
    const img = new Image(); img.src = c.toDataURL(); await img.decode();
    new ShaderMount(host, halftoneDotsFragmentShader, {
      u_image: img,
      u_colorFront: getShaderColorFromString('#FFFFFF'),
      u_colorBack: getShaderColorFromString('rgba(0,0,0,0)'),
      u_size: 0.025, u_grid: 1 /* hex */, u_radius: 1.0, u_contrast: 0.6, u_type: 0 /* classic */,
      u_originalColors: false, u_inverted: true,
      u_grainMixer: 0.2, u_grainOverlay: 0.1, u_grainSize: 0.5,
      u_fit: ShaderFitOptions.cover, u_scale: 1, u_rotation: 0, u_offsetX: 0, u_offsetY: 0,
      u_originX: 0.5, u_originY: 0.5, u_worldWidth: 0, u_worldHeight: 0,
    }, undefined, 0);
    document.querySelectorAll('.ht-cloud').forEach(el => el.hidden = true);   // swap only on success
  } catch (e) { /* module or WebGL failed: CSS clouds stay */ }
}
</script>
```

**Fallback**: the CSS clouds (3a) are in the markup from the start and are hidden only after the shader mounts. Offline, a blocked CDN, no WebGL, or reduced motion → the CSS version shows. Use 3b only when the user asks for higher fidelity; 3a is the default.

---

## Recipe 4 — Paper collage cutouts (Colorful only)

**When**: around the Colorful hero product window, as if paper scraps were laid on the table behind it. At most 2 pieces in the Colorful hero (the notebook sheet and the torn sheet — see visual-style-colorful.md), all behind the product window (`z-index` below it), clustered at the lower left and lower right; never behind the headline. **A cutout must never cover the product window** — it hides the rows the hero exists to show; it may only peek out from behind the window's edges. Colors: canvas white, ink `#030302`, peach `#F6CB98`, leaf `#9BD8A9`, lavender `#D5ACD8`, sky `#B8CAF5` (`craft.do.md`).

```css
.collage { position: relative; height: 520px; margin-top: 96px; }
.cut { position: absolute; z-index: 0; pointer-events: none; }
.collage > [data-mock] { position: relative; z-index: 1; }  /* the product window always sits on top */
/* Zigzag strip — white, notched top edge */
.cut-zigzag { left: -60px; bottom: 300px; width: 640px; height: 90px; background: #FFFFFF; transform: rotate(-6deg);
  clip-path: polygon(0 40%,4% 0,8% 40%,12% 0,16% 40%,20% 0,24% 40%,28% 0,32% 40%,36% 0,40% 40%,44% 0,48% 40%,52% 0,56% 40%,60% 0,64% 40%,68% 0,72% 40%,76% 0,80% 40%,84% 0,88% 40%,92% 0,96% 40%,100% 0,100% 100%,0 100%);
  filter: drop-shadow(0 3px 10px rgba(0,0,0,.08)); }
/* Torn sheet — white rim around a grey core (two clip-paths) */
.cut-torn { right: 120px; bottom: 300px; width: 300px; height: 210px; background: #FFFFFF;
  clip-path: polygon(0 100%,4% 62%,10% 70%,14% 40%,22% 48%,27% 22%,35% 30%,41% 6%,49% 18%,56% 0,63% 16%,70% 10%,76% 32%,84% 26%,88% 50%,95% 46%,100% 100%); }
.cut-torn::after { content: ""; position: absolute; inset: 10px 14px 0; background: color-mix(in srgb, #030302 12%, #FCF9F7);
  clip-path: polygon(0 100%,5% 66%,11% 72%,16% 46%,23% 52%,29% 28%,36% 36%,42% 14%,50% 24%,57% 8%,64% 22%,71% 18%,77% 38%,84% 34%,90% 58%,96% 54%,100% 100%); }
/* Ink scrap — black, torn all round */
.cut-ink { right: 10px; bottom: 270px; width: 250px; height: 70px; background: #030302; transform: rotate(-4deg);
  clip-path: polygon(0 50%,6% 20%,14% 34%,22% 8%,30% 26%,40% 4%,50% 22%,60% 0,70% 24%,80% 6%,90% 30%,100% 40%,96% 70%,86% 96%,74% 78%,62% 100%,50% 80%,38% 96%,26% 74%,14% 92%,4% 76%); }
/* Lined notebook sheet — peach with leaf rules, torn top */
.cut-notebook { right: -40px; bottom: -40px; width: 380px; height: 340px; transform: rotate(-8deg);
  background: repeating-linear-gradient(176deg, transparent 0 30px, color-mix(in srgb, #9BD8A9 80%, #030302) 30px 31px), #F6CB98;
  clip-path: polygon(0 18%,8% 14%,16% 19%,24% 11%,33% 16%,42% 8%,52% 13%,62% 5%,72% 10%,82% 3%,92% 8%,100% 0,100% 100%,0 100%); }
/* Colored blob — one scene color, irregular */
.cut-blob { left: 0; bottom: -30px; width: 300px; height: 300px; background: color-mix(in srgb, #B8CAF5 40%, #6A79E8 60%);
  border-radius: 46% 54% 40% 60% / 55% 45% 55% 45%; }
@media (max-width: 767px) { .collage { height: 380px; } .cut-ink, .cut-torn { display: none; } }
```

Gap: `#6A79E8` (blob, deeper periwinkle seen in the Craft hero) is not in the DNA file; prefer `#D5ACD8` lavender if staying strictly in-palette.

---

## Recipe 5 — Floating app-icon tiles (Business only)

**When**: the product integrates with real tools the user named (Gmail, Outlook, Slack…). 1–3 tiles overlapping the top-right corner of the stage card. Never invent integrations; no tiles if none are given.

```html
<span class="app-tile tile-1"><img src="https://api.iconify.design/logos/google-gmail.svg" alt="Gmail"></span>
<span class="app-tile tile-2"><img src="https://api.iconify.design/vscode-icons/file-type-outlook.svg" alt="Outlook"></span>
```
```css
.app-tile { position: absolute; width: 72px; height: 72px; border-radius: 16px; background: #FFFFFF;
  display: grid; place-items: center;
  box-shadow: 0 4px 5px rgba(71,103,136,.04), 0 8px 15px rgba(71,103,136,.03), 0 30px 50px rgba(71,103,136,.08); } /* Business §5 card */
.app-tile img { width: 40px; height: 40px; }
.tile-1 { right: -20px; top: -28px; }   /* relative to .frost-ring */
.tile-2 { right: -60px; top: 64px; }
@media (max-width: 767px) { .app-tile { display: none; } }
```

Logos: Iconify `logos:` set first (`google-gmail`, `google-calendar`, `slack-icon`, `zoom-icon`, `microsoft-teams`); Outlook is not in `logos:` → `vscode-icons:file-type-outlook` (verified 200). Confirm any other name returns HTTP 200 before use.

---

## Gaps

- Craft DNA records one sky value (`#B8CAF5`); the zenith tint borrows `#4890E3`, and the blob uses `#6A79E8` (observed in the reference screenshot, not in DNA).
- App tile size (72px / 16px radius / 40px logo) and frost ring (12px, `rgba(255,255,255,.38)`) are derived from the Calendly screenshot, not measured tokens.
- Grain opacities (.12 / .22) and halftone dot pitch (5px) were tuned by eye in the validation page.
