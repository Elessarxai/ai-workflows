"""Render a seek(t) HTML page to stills or to an MP4.

The page must define a global seek(t) that draws the frame at second t,
and window.ready, a promise that resolves once fonts are loaded.

  python render.py stills 0 6.5 18 35.9
  python render.py video out.mp4 --duration 36
  python render.py --width 1080 --height 1920 video out.mp4 --duration 20

--page, --width, --height and --fps go before the mode (defaults:
index.html next to this script, 1200, 1500, 30).
Stills go to build/still_<t>.png next to the page.
Needs: pip install playwright, playwright install chromium, ffmpeg on PATH.
"""
import argparse
import os
import subprocess
from pathlib import Path

from playwright.sync_api import sync_playwright


def open_page(p, args):
    browser = p.chromium.launch()
    page = browser.new_page(viewport={'width': args.width, 'height': args.height}, device_scale_factor=1)
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.goto(Path(args.page).resolve().as_uri())
    page.evaluate('window.ready')
    page.wait_for_timeout(200)
    return browser, page, errors


def stills(args):
    out_dir = Path(args.page).resolve().parent / 'build'
    out_dir.mkdir(exist_ok=True)
    with sync_playwright() as p:
        browser, page, errors = open_page(p, args)
        for t in args.times:
            page.evaluate(f'seek({t})')
            path = out_dir / f'still_{t:g}.png'
            page.screenshot(path=str(path))
            print('saved', path)
        browser.close()
    if errors:
        print('page errors:', errors[:3])


def video(args):
    frames = int(round(args.duration * args.fps))
    out = Path(args.out).resolve()
    tmp = out.with_name(out.stem + '.part.mp4')
    ffmpeg = subprocess.Popen(
        ['ffmpeg', '-y', '-v', 'error',
         '-f', 'image2pipe', '-framerate', str(args.fps), '-c:v', 'mjpeg', '-i', '-',
         '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '17', '-pix_fmt', 'yuv420p',
         '-r', str(args.fps), '-movflags', '+faststart', str(tmp)],
        stdin=subprocess.PIPE)
    with sync_playwright() as p:
        browser, page, errors = open_page(p, args)
        for i in range(frames):
            page.evaluate(f'seek({i / args.fps})')
            ffmpeg.stdin.write(page.screenshot(type='jpeg', quality=92))
            if i % (args.fps * 5) == 0:
                print(f'frame {i}/{frames}', flush=True)
        browser.close()
    ffmpeg.stdin.close()
    if ffmpeg.wait() == 0:
        os.replace(tmp, out)
        print('done', out)
    else:
        print('ffmpeg failed, nothing was overwritten')
    if errors:
        print('page errors:', errors[:3])


def main():
    ap = argparse.ArgumentParser(description='Render a seek(t) HTML page.')
    ap.add_argument('--page', default=str(Path(__file__).resolve().parent / 'index.html'))
    ap.add_argument('--width', type=int, default=1200)
    ap.add_argument('--height', type=int, default=1500)
    ap.add_argument('--fps', type=int, default=30)
    sub = ap.add_subparsers(dest='mode', required=True)
    s = sub.add_parser('stills', help='screenshot the given seconds')
    s.add_argument('times', nargs='+', type=float)
    v = sub.add_parser('video', help='render every frame to an MP4')
    v.add_argument('out')
    v.add_argument('--duration', type=float, default=36.0)
    args = ap.parse_args()
    stills(args) if args.mode == 'stills' else video(args)


if __name__ == '__main__':
    main()
