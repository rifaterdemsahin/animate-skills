# Storyboard: "14 skills, one command each" (animated-video skill, Path B)

| # | Scene | Duration | Motion |
|---|-------|----------|--------|
| 1 | Hook: "14 skills. One command each." | 2s | scale-in title, subtitle fade |
| 2 | Problem: three pain points struck through | 3s | staggered fade-in, then strike lines draw on |
| 3 | Product: `npx skills add` typed in a terminal, then the MP4 / HTML / GIF cards | 4s | typewriter, spring-up cards |
| 4 | CTA: skills.sh | 3s | spring scale |

Transitions: wipe → slide (spring) → fade, 0.5s each, so the total is 12s − 1.5s = 10.5s (315 frames at 30fps).
Source: `remotion-video/src/Storyboard.tsx`. Render with `npx remotion render Storyboard out.mp4`.
