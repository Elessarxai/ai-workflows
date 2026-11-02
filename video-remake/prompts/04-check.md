# Step 4: Check stills before you render

A full render takes minutes and a still takes a second, so check stills first and render once.

## Prompt

```text
Render stills at 0 seconds, at the busiest moment, at the last frame, and at every state change plus a frame just before and just after it. Look at each one at full size and list every problem: text running out of a box, lines hidden behind boxes, labels overlapping, a weak or empty first frame. Then shrink them to phone width (about 400 px) and list what you can't read anymore. For every problem give the second, what's wrong and the smallest fix. Fix them, render the stills again, and show me the before and after.
```

## Notes

The usual suspects: text overflowing its box, lines drawn underneath panel backgrounds, and a first frame that is empty or full of zeros.

When you add notes of your own, give Claude a second and a thing, not a feeling. "It feels off" gives it nothing to work with. "At 12.4 s the label covers the counter" is a fix it can make in one line.

---
[← all steps](../README.md)
