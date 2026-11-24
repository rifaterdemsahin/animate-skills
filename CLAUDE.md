# CLAUDE.md — animate-skills

## Layout
- `skills/skills.json` — the skills database (one entry per animation skill). Edit this, then run `python3 build.py`.
- `.claude/skills/` — the real skills, installed with `npx skills add <repo> -s <skill>` (lockfile: `skills-lock.json`).
- `outputs/<slug>/` — what each skill produced (MP4, GIF, HTML), plus the source that made it.
- `remotion-video/` — Remotion project (SkillsIntro, GsapTitle, Storyboard compositions).
- `hyperframes-video/` — HyperFrames project (title card).
- `tools/capture.py` — Playwright screenshots of HTML outputs: `python3 tools/capture.py "page.html?t=1.5" out.png [--reduced]`.
- `build.py` → `site/` (served by nginx on fly.io via `Dockerfile` + `fly.toml`). Never edit `site/` or this file by hand.

## Skills
- Before writing any animation code, pick the matching skill from `skills/skills.json` and load it:
  Remotion/HyperFrames/animated-video for video, gsap-web/animejs/svg-animation/frontend-design for web,
  threejs-animation for 3D, algorithmic-art and slack-gif-creator for generative output.
- Follow each skill's "Deliver & verify" loop: freeze with `?t=N`, screenshot start/mid/end, then check both normal and reduced motion.

## Rules
- Animate transform and opacity; avoid layout-triggering properties.
- Respect `prefers-reduced-motion` in every artifact (tier it, don't just switch it off).
- No ffmpeg is installed system-wide. For HyperFrames renders, set `HYPERFRAMES_FFMPEG_PATH` (imageio-ffmpeg static build in `.pydeps/`)
  and `HYPERFRAMES_FFPROBE_PATH` (Remotion's compositor `ffprobe`).
- After changing outputs: `python3 build.py`, commit, push, `fly deploy`.
