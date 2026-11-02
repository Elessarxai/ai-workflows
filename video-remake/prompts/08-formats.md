# Extra: One page, three formats

Don't crop a 4:5 video into 9:16, you'll cut the panels in half. Keep the timeline and give each format its own layout.

## Prompt

```text
Keep the seek(t) timeline and the beat sheet exactly as they are, and add layouts for 1080x1920 and 1080x1080. In vertical, stack the panels. In square, drop the least important one. Same seconds, same beats, different layout. Render stills of all three formats at the same 4 seconds so I can compare them.
```

## Notes

render.py takes the size before the mode: `python render.py --width 1080 --height 1920 video vertical.mp4 --duration 36`.

---
[← all steps](../README.md)
