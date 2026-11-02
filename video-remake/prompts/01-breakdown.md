# Step 1: Take the reference apart

Most remakes fail here, because people describe the video from memory. This makes Claude look at it instead and write down what it sees as numbers. "Make it look like the reference" lets it copy whatever stands out most and miss the structure underneath, while a hex code, a font size and "one new row every half second" can't be misread.

## Prompt

```text
There's a reference video in this folder. Before we build anything, break it down.

1. Duration, resolution, frame rate, and whether it has sound.
2. Make a contact sheet (one frame per second) and pull full-size frames at the 4 busiest moments. Look at all of them.
3. Layout map: every box and panel with its position and size in pixels, what it shows, and what changes in it over time.
4. Style: sample the exact colours as hex, name the closest free font, its size and line height.
5. Timeline: what happens when, how often something updates, what's on screen in the very first frame, and how it ends. If it has music, give the tempo and which changes land on the beat.
6. Motion: for every moving thing, does it snap, slide at constant speed, ease in or out, or bounce? Give rough durations.

Describe it all as numbers and rules, for someone who will never see the video. Write it to BREAKDOWN.md. Don't build anything yet.
```

## Notes

Read BREAKDOWN.md yourself. If something you noticed in the video is missing, tell Claude now, not after the render.

---
[← all steps](../README.md)
