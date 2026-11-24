# 🎬 animate-skills

A catalog of LLM agent skills for making animations (Remotion, HyperFrames, GSAP, Lottie, Anime.js, Three.js, Manim, CSS/WAAPI, algorithmic art, Slack GIFs, Figma motion) with a page per skill: live demo, copy-paste install from [skills.sh](https://skills.sh), a ready prompt, a `CLAUDE.md` snippet and a hook.

## 🗂️ Database → 🎁 Artifact → 🚀 Execution

| Stage | File |
|---|---|
| Database | `skills/skills.json` — one entry per skill |
| Artifact | `python3 build.py` → `site/` (index + `site/skills/<slug>.html`, shared menu) and regenerates `CLAUDE.md` + `.claude/settings.json` hooks |
| Execution | `fly deploy` (nginx serves `site/`) |

```bash
python3 build.py            # build
python3 -m http.server -d site 8000   # preview
fly deploy                  # ship
```

To add a skill: add an entry to `skills/skills.json`, add a demo in `DEMOS` in `build.py`, rebuild.
