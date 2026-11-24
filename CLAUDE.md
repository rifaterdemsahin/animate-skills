# CLAUDE.md — animation projects

## Skills
- Animation skills live in `.claude/skills/` (installed from skills.sh with `npx skills add`).
- Before writing any animation code, pick the matching skill from `skills/skills.json`
  and load it: Remotion/HyperFrames for video, GSAP/Anime.js/CSS for web,
  Three.js for 3D, Manim for math, algorithmic-art / slack-gif-creator for generative output.

## Rules
- Animate transform and opacity; avoid layout-triggering properties.
- Respect `prefers-reduced-motion` in every artifact.
- Sources in `animations/<skill>/`, rendered artifacts in `out/` (git-ignored).
- When done, state the artifact path and the exact command to preview or render it.
