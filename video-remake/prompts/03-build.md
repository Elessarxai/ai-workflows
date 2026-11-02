# Step 3: Build it as one page

The rules in this prompt are what keep the render clean, so paste them as they are. Break one and the stills stop matching the video: a timer makes the same second come out different on every run, and a library running on its own clock freezes or skips when you jump to a frame.

## Prompt

```text
Build the video as one self-contained index.html at exactly [1200x1500], following MAPPING.md.

Rules:
- The whole layout is visible from the first frame. Motion only happens on top.
- All motion comes from one function, seek(t), that draws the page at second t. No CSS animations, no timers, no unseeded randomness, so any frame can be rendered exactly.
- If you use an animation library, drive it from seek(t), never from its own clock.
- Keep every easing curve, duration and spring in one motion.js file and use only those. No numbers typed inline.
- One hero move at a time. Everything else holds still or dims until it lands.
- Load fonts from local files and expose window.ready that resolves once they've loaded.
- Test it: render the same second twice, each time in a fresh page. The two images must match pixel for pixel.
- Length: [36] seconds.

Also write render.py with Playwright: a 'stills' mode that screenshots the times I give it, and a 'video' mode that screenshots every frame at 30 fps as JPEG (quality 92) and pipes them into ffmpeg (libx264, crf 17, yuv420p, faststart). Write to a temporary name and rename only when ffmpeg succeeds.
```

## Notes

A working [render.py](../render.py) and a starting [motion.js](../motion.js) are in this folder. Copy both next to your index.html.

---
[← all steps](../README.md)
