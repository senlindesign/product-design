// Desktop layout audit for a generated page, run by evals/screens.py.
// At 1440px it reports: text inside a product mock that another element covers, text cut off at the left or right
// (by the viewport or a clipping ancestor), and where the hero's product visual starts relative to the 900px fold.
// Prints JSON. Prints {"unavailable": true} when the playwright package can't be loaded.
let chromium;
try { ({ chromium } = require("playwright")); } catch (e) {
  try { ({ chromium } = require("playwright-core")); } catch (e2) { console.log(JSON.stringify({ unavailable: true })); process.exit(0); }
}

(async () => {
  const opts = process.env.PD_CHROME ? { executablePath: process.env.PD_CHROME } : {};
  const browser = await chromium.launch(opts);
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1, reducedMotion: "reduce" });
  const page = await ctx.newPage();
  await page.goto("file://" + process.argv[2], { waitUntil: "load" });
  await page.waitForTimeout(500);

  // Fold position first, at the real 900px viewport.
  const fold = await page.evaluate(() => {
    const hero = document.querySelector('[data-section="hero"]');
    const mock = hero && hero.querySelector("[data-mock]");
    if (!mock) return { hero_mock: false };
    const firstText = [...mock.querySelectorAll("*")].find((el) =>
      [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim().length > 1) && el.getBoundingClientRect().height > 0);
    return { hero_mock: true, hero_mock_top: Math.round(mock.getBoundingClientRect().top + scrollY),
             hero_first_text_top: firstText ? Math.round(firstText.getBoundingClientRect().top + scrollY) : null };
  });

  // Then a tall viewport so every element can be hit-tested without scrolling.
  const h = Math.min(await page.evaluate(() => document.documentElement.scrollHeight), 8000);
  await page.setViewportSize({ width: 1440, height: h });
  await page.waitForTimeout(300);
  await page.addStyleTag({ content: "*{pointer-events:auto!important}" });  // decorations often opt out of hit-testing

  const issues = await page.evaluate(() => {
    const own = (el) => [...el.childNodes].filter((n) => n.nodeType === 3).map((n) => n.textContent).join("").trim();
    const shown = (el) => { const s = getComputedStyle(el); return s.visibility !== "hidden" && s.display !== "none" && +s.opacity > 0.05; };
    const leaves = [...document.body.querySelectorAll("*")].filter((el) => own(el).length > 1 && shown(el)
      && !el.closest("nav,[aria-hidden='true'],.sr-only") && el.getBoundingClientRect().width > 0);
    const name = (el) => `${el.tagName.toLowerCase()}${el.className && typeof el.className === "string" ? "." + el.className.trim().split(/\s+/)[0] : ""}`;
    const covered = [], clipped = [];
    for (const el of leaves) {
      const r = el.getBoundingClientRect();
      // Horizontal clipping by the viewport or by an ancestor that hides overflow. Vertical crops are intentional.
      let left = 0, right = innerWidth;
      for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) {
        const s = getComputedStyle(a);
        if (["hidden", "clip"].includes(s.overflowX)) { const ar = a.getBoundingClientRect(); left = Math.max(left, ar.left); right = Math.min(right, ar.right); }
      }
      const style = getComputedStyle(el);
      const ellipsis = style.textOverflow === "ellipsis";
      if (!ellipsis && (r.left < left - 2 || r.right > right + 2) && r.right > left && r.left < right) {
        clipped.push(`"${own(el).slice(0, 40)}" (${name(el)})`);
        continue;
      }
      // Covered: sample the start and the middle of the text; a hit that is neither the element nor related to it covers it.
      if (!el.closest("[data-mock]")) continue;
      const y = r.top + r.height / 2;
      for (const x of [r.left + Math.min(6, r.width / 2), r.left + r.width / 2]) {
        if (x < 0 || x >= innerWidth || y < 0 || y >= innerHeight) continue;
        const hit = document.elementFromPoint(x, y);
        if (hit && hit !== el && !el.contains(hit) && !hit.contains(el)) {
          covered.push(`"${own(el).slice(0, 40)}" under ${name(hit)}`);
          break;
        }
      }
    }
    return { covered: [...new Set(covered)].slice(0, 8), clipped: [...new Set(clipped)].slice(0, 8) };
  });
  await browser.close();
  console.log(JSON.stringify({ ...fold, ...issues }));
})().catch((e) => { console.log(JSON.stringify({ error: String(e).slice(0, 300) })); });
