#!/usr/bin/env python3
"""Screenshots and a narrow-screen audit for generated pages. Works on macOS and Linux.

  python3 evals/screens.py page.html                  # desktop 1440px + mobile 390px screenshots next to the page
  python3 evals/screens.py page.html --mobile-audit   # also the layout audits: 390px overflow, duplicated nav, menu
                                                      # toggle; 1440px covered or clipped text, hero visual below the fold

Chrome is found in this order: $CHROME, Google Chrome on macOS, chrome/chromium on PATH, Playwright's Chromium.
The mobile audit needs Node with the `playwright` package (local or global); without it the audit is skipped.
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAC_CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
DESKTOP = (1440, 6000)


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    if Path(MAC_CHROME).exists():
        return MAC_CHROME
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser", "chrome"):
        if shutil.which(name):
            return shutil.which(name)
    roots = [os.environ.get("PLAYWRIGHT_BROWSERS_PATH"), "/opt/pw-browsers", str(Path.home() / ".cache/ms-playwright")]
    for root in filter(None, roots):
        hits = sorted(glob.glob(f"{root}/chromium-*/chrome-linux/chrome") + glob.glob(f"{root}/chromium-*/chrome-linux64/chrome"))
        if hits:
            return hits[-1]
    return None


def screenshot(page, out, width=DESKTOP[0], height=DESKTOP[1]):
    """Full-window screenshot of a local HTML file. Returns True when the PNG was written."""
    chrome = find_chrome()
    if not chrome:
        raise RuntimeError("no Chrome/Chromium found; set $CHROME")
    out = Path(out)
    out.unlink(missing_ok=True)
    subprocess.run([chrome, "--headless=new", "--hide-scrollbars", "--disable-gpu", "--no-sandbox",
                    f"--window-size={width},{height}", "--virtual-time-budget=6000",
                    f"--screenshot={out}", Path(page).resolve().as_uri()],
                   capture_output=True, timeout=120)
    return out.exists()


def mobile_screenshot(page, out):
    """390px screenshot through Playwright. Chrome's CLI clamps the window to ~500px, so a 390px CLI
    screenshot is a crop of a wider layout and shows overflow that isn't there. Returns False without
    Node + Playwright."""
    if not shutil.which("node"):
        return False
    out = Path(out)
    out.unlink(missing_ok=True)
    subprocess.run(["node", str(HERE / "mobile_audit.cjs"), str(Path(page).resolve()), str(out.resolve())],
                   capture_output=True, text=True, timeout=120, env=_node_env())
    return out.exists()


def shoot_both(page, out_dir=None):
    """Desktop and mobile screenshots: <stem>-desktop.png and <stem>-mobile.png.
    Returns (None, None) when either fails, including when there is no way to render a true 390px layout."""
    page = Path(page)
    out_dir = Path(out_dir or page.parent)
    desk, mob = out_dir / f"{page.stem}-desktop.png", out_dir / f"{page.stem}-mobile.png"
    if not mobile_screenshot(page, mob):
        print("  mobile screenshot needs node + playwright (Chrome's CLI can't render 390px)", file=sys.stderr)
        return None, None
    return (desk, mob) if screenshot(page, desk, *DESKTOP) else (None, None)


def _node_env():
    env = dict(os.environ)
    if shutil.which("npm"):
        root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        if root:
            env["NODE_PATH"] = os.pathsep.join(filter(None, [env.get("NODE_PATH"), root]))
    chrome = find_chrome()
    if chrome:
        env["PD_CHROME"] = chrome
    return env


def mobile_audit(page):
    """Run evals/mobile_audit.cjs at 390px. Returns a dict, or None when Node/Playwright is missing."""
    if not shutil.which("node"):
        return None
    proc = subprocess.run(["node", str(HERE / "mobile_audit.cjs"), str(Path(page).resolve())],
                          capture_output=True, text=True, timeout=120, env=_node_env())
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"error": (proc.stderr or proc.stdout).strip()[-300:]}
    return None if data.get("unavailable") else data


def desktop_audit(page):
    """Run evals/desktop_audit.cjs at 1440px. Returns a dict, or None when Node/Playwright is missing."""
    if not shutil.which("node"):
        return None
    proc = subprocess.run(["node", str(HERE / "desktop_audit.cjs"), str(Path(page).resolve())],
                          capture_output=True, text=True, timeout=180, env=_node_env())
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {"error": (proc.stderr or proc.stdout).strip()[-300:]}
    return None if data.get("unavailable") else data


FOLD_TEXT_LIMIT = 800   # the hero product's first line of text must start above this (900px fold, ~100px visible)


def desktop_problems(data):
    """Turn a desktop audit result into problems (empty = clean)."""
    if not data or data.get("error"):
        return []
    out = [f"text covered inside a product mock: {c}" for c in data.get("covered", [])]
    out += [f"text cut off at the left or right edge: {c}" for c in data.get("clipped", [])]
    top = data.get("hero_first_text_top")
    if top and top > FOLD_TEXT_LIMIT:
        out.append(f"hero product visual starts too low: first text at {top}px (want < {FOLD_TEXT_LIMIT}px on a 900px fold)")
    return out


def audit_problems(data):
    """Turn an audit result into a list of human-readable problems (empty = clean)."""
    if not data or data.get("error"):
        return []
    out = []
    if data["overflow_px"] > 1:
        wide = ", ".join(data["wide_elements"][:3])
        out.append(f"page scrolls sideways at 390px by {data['overflow_px']}px ({wide})")
    if data["visible_navs"] > 1:
        out.append(f"{data['visible_navs']} navigation bars visible at once at 390px")
    if data["nav_links_visible"] and not data["toggle"]:
        out.append(f"{data['nav_links_visible']} nav links shown inline at 390px with no menu toggle")
    if data["toggle"] and data["toggle_opens"] is False:
        out.append("mobile menu toggle does not reveal any links")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("pages", nargs="+")
    ap.add_argument("--out-dir")
    ap.add_argument("--mobile-audit", action="store_true")
    args = ap.parse_args()
    bad = 0
    for page in args.pages:
        desk, mob = shoot_both(page, args.out_dir)
        print(f"{page}: {desk or 'screenshot failed'} · {mob or ''}")
        if args.mobile_audit:
            data = mobile_audit(page)
            if data is None:
                print("  mobile audit: skipped (needs node + playwright)")
                continue
            if data.get("error"):
                print(f"  mobile audit error: {data['error']}")
                continue
            problems = audit_problems(data)
            bad += bool(problems)
            print("  mobile audit: " + ("; ".join(problems) if problems else "clean"))
            desk = desktop_problems(desktop_audit(page))
            bad += bool(desk)
            print("  desktop audit: " + ("; ".join(desk) if desk else "clean"))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
