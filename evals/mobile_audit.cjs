// Narrow-screen audit for a generated page, run by evals/screens.py.
// Opens the page at 390px and reports sideways overflow, duplicated navigation, and whether the mobile menu opens.
// Prints JSON. Prints {"unavailable": true} when the playwright package can't be loaded.
// Usage: node mobile_audit.cjs <page.html> [screenshot.png]  (the screenshot is the first three 390px screens)
let chromium;
try { ({ chromium } = require("playwright")); } catch (e) {
  try { ({ chromium } = require("playwright-core")); } catch (e2) { console.log(JSON.stringify({ unavailable: true })); process.exit(0); }
}

const page_path = process.argv[2];
const shot_path = process.argv[3];

const VISIBLE = `(el) => {
  const s = getComputedStyle(el), r = el.getBoundingClientRect();
  return s.display !== "none" && s.visibility !== "hidden" && +s.opacity > 0.05 && r.width > 0 && r.height > 0
    && r.bottom > 0 && r.top < innerHeight && r.right > 0 && r.left < innerWidth;
}`;

(async () => {
  const opts = process.env.PD_CHROME ? { executablePath: process.env.PD_CHROME } : {};
  const browser = await chromium.launch(opts);
  const ctx = await browser.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 1, reducedMotion: "reduce" });
  const page = await ctx.newPage();
  await page.goto("file://" + page_path, { waitUntil: "load" });
  await page.waitForTimeout(500);
  if (shot_path) {
    // Taken before the audit clicks the menu toggle. Chrome's CLI can't render below ~500px wide, so mobile
    // screenshots must come from here.
    const h = await page.evaluate(() => document.documentElement.scrollHeight);
    await page.screenshot({ path: shot_path, fullPage: true, clip: { x: 0, y: 0, width: 390, height: Math.min(2532, h) } });
  }

  const before = await page.evaluate((VISIBLE_SRC) => {
    const visible = eval(VISIBLE_SRC);
    const doc = document.documentElement;
    const overflow_px = Math.max(doc.scrollWidth, document.body.scrollWidth) - innerWidth;
    const label = (el) => el.tagName.toLowerCase() + (el.id ? "#" + el.id : "")
      + (el.classList.length ? "." + [...el.classList].slice(0, 2).join(".") : "");
    // Widest offenders: elements whose right edge passes the viewport and whose parent does not clip them.
    const wide = [];
    if (overflow_px > 1) {
      for (const el of document.body.querySelectorAll("*")) {
        const r = el.getBoundingClientRect();
        if (r.right <= innerWidth + 1 || r.width === 0) continue;
        let clipped = false;
        for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) {
          const o = getComputedStyle(p).overflowX;
          if (o === "hidden" || o === "clip" || o === "auto" || o === "scroll") { clipped = true; break; }
        }
        if (!clipped) wide.push([Math.round(r.right - innerWidth), label(el)]);
      }
      wide.sort((a, b) => b[0] - a[0]);
    }
    // Navigation bars visible at the top of the first screen (outermost only).
    const navs = [...document.querySelectorAll('nav, [data-section="nav"]')]
      .filter((n) => visible(n) && n.getBoundingClientRect().top < 200)
      .filter((n, _, all) => !all.some((o) => o !== n && o.contains(n)));
    const top = navs[0];
    const links = top ? [...top.querySelectorAll("a")].filter(visible) : [];
    const toggle = top ? [...top.querySelectorAll("button, [aria-expanded], [aria-controls], [class*=menu], [class*=toggle], [class*=burger]")]
      .find((b) => visible(b) && b.tagName !== "A") : null;
    if (toggle) toggle.setAttribute("data-pd-toggle", "1");
    const count = [...document.querySelectorAll("a")].filter(visible).length;
    return {
      overflow_px, wide_elements: wide.slice(0, 5).map(([px, l]) => `${l} +${px}px`),
      visible_navs: navs.length,
      nav_links_visible: Math.max(0, links.length - 1),  // minus the logo link
      toggle: !!toggle, links_on_screen: count,
    };
  }, VISIBLE);

  let toggle_opens = null;
  if (before.toggle) {
    try {
      await page.click("[data-pd-toggle]", { timeout: 2000 });
      await page.waitForTimeout(500);
      const after = await page.evaluate((VISIBLE_SRC) => {
        const visible = eval(VISIBLE_SRC);
        return [...document.querySelectorAll("a")].filter(visible).length;
      }, VISIBLE);
      toggle_opens = after > before.links_on_screen;
    } catch (e) { toggle_opens = false; }
  }
  await browser.close();
  console.log(JSON.stringify({ ...before, toggle_opens }));
})().catch((e) => { console.log(JSON.stringify({ error: String(e).slice(0, 300) })); });
