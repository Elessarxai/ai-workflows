// motion.js: every timing value in one place. Use these, never numbers typed inline.
// All functions are pure, so seek(t) can draw any frame on its own.

export const FPS = 30;

// Standard curves (easings.net), as cubic-bezier control points
export const EASE = {
  enter: [0.16, 1, 0.3, 1],     // ease-out-expo: panels, titles, logos coming in
  soft:  [0.22, 1, 0.36, 1],    // ease-out-quint: calmer entrances
  move:  [0.76, 0, 0.24, 1],    // ease-in-out-quart: moving across the screen
  exit:  [0.7, 0, 0.84, 0],     // ease-in-expo: leaving, always shorter than entering
  pop:   [0.34, 1.56, 0.64, 1], // ease-out-back: small overshoot, use rarely
};

// Durations in frames at 30 fps
export const FRAMES = { tap: 5, move: 12, hero: 22, exit: 8, stagger: 3 };

// Cubic-bezier curve value at progress p (0..1)
export function bezier([x1, y1, x2, y2], p) {
  if (p <= 0) return 0;
  if (p >= 1) return 1;
  const f = (a, b, s) => 3 * a * s * (1 - s) ** 2 + 3 * b * s * s * (1 - s) + s ** 3;
  let lo = 0, hi = 1, s = p;
  for (let i = 0; i < 30; i++) {          // find s where x(s) = p
    s = (lo + hi) / 2;
    if (f(x1, x2, s) < p) lo = s; else hi = s;
  }
  return f(y1, y2, s);
}

// Eased progress of a move that starts at second `start` and lasts `frames`
export function tween(t, start, frames, curve = EASE.enter) {
  return bezier(curve, (t - start) / (frames / FPS));
}

// Spring with no simulation: progress 0 -> 1 at `dt` seconds after it starts.
// damping 1 = no bounce, 0.8 = expensive, 0.5 = playful. hz = how fast it moves.
export function spring(dt, damping = 0.8, hz = 2) {
  if (dt <= 0) return 0;
  const w = 2 * Math.PI * hz;
  if (damping >= 1) return 1 - Math.exp(-w * dt) * (1 + w * dt);
  const wd = w * Math.sqrt(1 - damping * damping);
  return 1 - Math.exp(-damping * w * dt) *
    (Math.cos(wd * dt) + (damping * w / wd) * Math.sin(wd * dt));
}

// Item i of a list starts FRAMES.stagger frames after the one before it
export const staggerStart = (start, i) => start + (i * FRAMES.stagger) / FPS;
