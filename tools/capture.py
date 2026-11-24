#!/usr/bin/env python3
"""Screenshot (and optionally record a WebM of) an HTML animation output.

usage: capture.py "page.html?t=1.5" out.png [--wait MS] [--video out.webm --seconds S] [--size WxH] [--reduced]
"""
import argparse, shutil, tempfile
from pathlib import Path
from playwright.sync_api import sync_playwright

ap = argparse.ArgumentParser()
ap.add_argument("page"); ap.add_argument("png")
ap.add_argument("--wait", type=int, default=2500)
ap.add_argument("--video"); ap.add_argument("--seconds", type=float, default=4)
ap.add_argument("--size", default="1280x720")
ap.add_argument("--reduced", action="store_true", help="emulate prefers-reduced-motion: reduce")
a = ap.parse_args()
w, h = map(int, a.size.split("x"))
page, _, query = a.page.partition("?")
url = a.page if a.page.startswith("http") else Path(page).resolve().as_uri() + ("?" + query if query else "")

with sync_playwright() as p:
    b = p.chromium.launch()
    errors = []
    if a.video:
        tmp = tempfile.mkdtemp()
        ctx = b.new_context(reduced_motion="reduce" if a.reduced else "no-preference", viewport={"width": w, "height": h}, record_video_dir=tmp, record_video_size={"width": w, "height": h})
    else:
        ctx = b.new_context(reduced_motion="reduce" if a.reduced else "no-preference", viewport={"width": w, "height": h})
    pg = ctx.new_page()
    pg.on("pageerror", lambda e: errors.append(str(e)))
    pg.on("console", lambda m: m.type == "error" and errors.append(m.text))
    pg.goto(url, wait_until="networkidle")
    pg.wait_for_timeout(a.wait)
    pg.screenshot(path=a.png)
    if a.video:
        pg.wait_for_timeout(max(0, int(a.seconds * 1000) - a.wait))
        vid = pg.video.path(); ctx.close(); shutil.move(vid, a.video)
    else:
        ctx.close()
    b.close()
    print("errors:", errors or "none")
