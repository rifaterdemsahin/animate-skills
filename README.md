# 🎬 animate-skills

14 LLM agent skills for making animations: video, web motion, 3D, math and generative art.
12 were installed from [skills.sh](https://skills.sh) with `npx skills add` and **actually used** to make the outputs below.
Each skill has its own page with the real output, a copy-paste install, a ready prompt, a `CLAUDE.md` snippet and a hook.

🌐 **Live site:** [https://animate-skills.fly.dev](https://animate-skills.fly.dev) · 📄 [index.html](index.html) (open locally after `python3 build.py`) · 🎁 [Outputs gallery](https://animate-skills.fly.dev/#outputs) · 🗂️ [skills database](skills/skills.json)

![rocket emoji made with slack-gif-creator](outputs/slack-gif-creator/rocket-emoji.gif)

## 🎁 Skills and their outputs

| Skill (page) | Output made with it | Installed skill | Registry |
|---|---|---|---|
| 🎬 [Remotion](https://animate-skills.fly.dev/skills/remotion.html) | [skills-intro.mp4](outputs/remotion/skills-intro.mp4) [source](remotion-video/src/SkillsIntro.tsx) | [`remotion-best-practices`](.claude/skills/remotion-best-practices) | [skills.sh](https://skills.sh/remotion-dev/skills/remotion-best-practices) |
| 🌀 [GSAP Web Animation](https://animate-skills.fly.dev/skills/gsap-web.html) | [pipeline-hero.html](outputs/gsap-web/pipeline-hero.html) [source](outputs/gsap-web/pipeline-hero.html) | [`gsap-web`](.claude/skills/gsap-web), [`accessible-animation`](.claude/skills/accessible-animation) | [skills.sh](https://skills.sh/iart-ai/web-animation-skills/gsap-web) |
| 〰️ [SVG Animation](https://animate-skills.fly.dev/skills/svg-animation.html) | [route.html](outputs/svg-animation/route.html) [source](outputs/svg-animation/route.html) | [`svg-animation`](.claude/skills/svg-animation) | [skills.sh](https://skills.sh/iart-ai/web-animation-skills/svg-animation) |
| 🫧 [Lottie](https://animate-skills.fly.dev/skills/lottie.html) | [skill-installed.html](outputs/lottie/skill-installed.html) [source](outputs/lottie/skill-installed.json) | [`lottie-animation`](.claude/skills/lottie-animation) | [skills.sh](https://skills.sh/iart-ai/web-animation-skills/lottie-animation) |
| 🎞️ [HyperFrames](https://animate-skills.fly.dev/skills/hyperframes.html) | [title-card.mp4](outputs/hyperframes/title-card.mp4) [source](hyperframes-video/compositions/title.html) | [`hyperframes`](.claude/skills/hyperframes), [`hyperframes-cli`](.claude/skills/hyperframes-cli) | [skills.sh](https://skills.sh/heygen-com/hyperframes/hyperframes) |
| 🧩 [GSAP in Remotion](https://animate-skills.fly.dev/skills/gsap-remotion.html) | [gsap-title.mp4](outputs/gsap-remotion/gsap-title.mp4) [source](remotion-video/src/GsapTitle.tsx) | [`gsap-animation`](.claude/skills/gsap-animation) | [skills.sh](https://skills.sh/notedit/happy-skills/gsap-animation) |
| 📐 [Manim](https://animate-skills.fly.dev/skills/manim.html) | _source only_ [source](outputs/manim/pythagoras.py) | — | [skills.sh](https://skills.sh/nousresearch/hermes-agent) |
| ✨ [Anime.js](https://animate-skills.fly.dev/skills/animejs.html) | [dot-ripple.html](outputs/animejs/dot-ripple.html) [source](outputs/animejs/dot-ripple.html) | [`animejs`](.claude/skills/animejs) | [skills.sh](https://skills.sh/avabillions2040/claudedesignskills-02-02-2026/animejs) |
| 🧊 [Three.js / WebGL](https://animate-skills.fly.dev/skills/threejs-webgl.html) | [particle-orbit.html](outputs/threejs-webgl/particle-orbit.html) [source](outputs/threejs-webgl/particle-orbit.html) | [`threejs-animation`](.claude/skills/threejs-animation) | [skills.sh](https://skills.sh/iart-ai/webgl-animation-skills/threejs-animation) |
| 💅 [CSS & Web Animations API](https://animate-skills.fly.dev/skills/css-motion.html) | [one-moment.html](outputs/css-motion/one-moment.html) [source](outputs/css-motion/one-moment.html) | [`frontend-design`](.claude/skills/frontend-design), [`accessible-animation`](.claude/skills/accessible-animation) | [skills.sh](https://skills.sh/anthropics/skills/frontend-design) |
| 🎨 [Algorithmic Art](https://animate-skills.fly.dev/skills/algorithmic-art.html) | [tidal-memory.html](outputs/algorithmic-art/tidal-memory.html) [source](outputs/algorithmic-art/tidal-memory.html) | [`algorithmic-art`](.claude/skills/algorithmic-art) | [skills.sh](https://skills.sh/anthropics/skills/algorithmic-art) |
| 🚀 [Slack GIF Creator](https://animate-skills.fly.dev/skills/slack-gif-creator.html) | [rocket-emoji.gif](outputs/slack-gif-creator/rocket-emoji.gif) [source](outputs/slack-gif-creator/make_rocket.py) | [`slack-gif-creator`](.claude/skills/slack-gif-creator) | [skills.sh](https://skills.sh/anthropics/skills/slack-gif-creator) |
| 📽️ [Animated Video (design kit)](https://animate-skills.fly.dev/skills/animated-video.html) | [storyboard.mp4](outputs/animated-video/storyboard.mp4) [source](remotion-video/src/Storyboard.tsx) | [`animated-video`](.claude/skills/animated-video) | [skills.sh](https://skills.sh/bluzir/claude-code-design/animated-video) |
| 🎛️ [Figma Motion (MCP)](https://animate-skills.fly.dev/skills/figma-motion.html) | _not run_  | — | [skills.sh](https://skills.sh/?q=figma) |

## 🗂️ Database → 🎁 Artifact → 🚀 Execution

| Stage | Where |
|---|---|
| 🗂️ Database | [`skills/skills.json`](skills/skills.json), with the real skills in [`.claude/skills/`](.claude/skills) ([`skills-lock.json`](skills-lock.json)) |
| 🎁 Artifact | [`outputs/`](outputs) (MP4, GIF, HTML), made in [`remotion-video/`](remotion-video), [`hyperframes-video/`](hyperframes-video) and `outputs/*/` |
| 🚀 Execution | [`build.py`](build.py) → `site/` → [`Dockerfile`](Dockerfile) + [`fly.toml`](fly.toml) → [https://animate-skills.fly.dev](https://animate-skills.fly.dev) |

Also generated from the database: [`CLAUDE.md`](CLAUDE.md) and the hooks in [`.claude/settings.json`](.claude/settings.json).

## ⚡ Quick start

```bash
npx skills add remotion-dev/skills -s remotion-best-practices      # install a skill
python3 build.py                                                   # rebuild site/, README.md, CLAUDE.md, hooks
python3 -m http.server -d site 8000                                # preview
fly deploy                                                         # ship
```

To add a skill: install it, make an output in `outputs/<slug>/`, add an entry to `skills/skills.json`, then run `python3 build.py`.

> README.md is generated by `build.py`. Edit the generator or the database, not this file.
