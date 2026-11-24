#!/usr/bin/env python3
"""Build the static site from the skills database.

skills/skills.json  (database)  ->  site/  (artifact)  ->  fly.io (execution)
"""
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
DB = ROOT / "skills" / "skills.json"
OUT = ROOT / "site"

skills = json.loads(DB.read_text())
e = html.escape

# Live, dependency-free demos that illustrate each skill's style of motion.
DEMOS = {
    "remotion": '<div class="d-spring">Q3</div>',
    "gsap-web": '<div class="d-split">' + "".join(
        f'<span style="--i:{i}">{c}</span>' for i, c in enumerate("TIMELINE")) + "</div>",
    "lottie": '<svg class="d-check" viewBox="0 0 52 52"><circle cx="26" cy="26" r="24"/><path d="M14 27l8 8 16-16"/></svg>',
    "hyperframes": '<div class="d-title"><b>Ship faster</b><i></i></div>',
    "gsap-remotion": '<svg class="d-morph" viewBox="0 0 100 100"><rect x="20" y="20" width="60" height="60"/></svg>',
    "manim": '<div class="d-eq">a² + b² = <span>c²</span></div>',
    "animejs": '<div class="d-grid">' + "".join(
        f'<i style="--d:{abs(r-4)+abs(c-4)}"></i>' for r in range(9) for c in range(9)) + "</div>",
    "threejs-webgl": '<div class="d-cube"><i></i><i></i><i></i><i></i><i></i><i></i></div>',
    "css-motion": '<div class="d-rise"><span>One</span><span>orchestrated</span><span>moment</span></div>',
    "algorithmic-art": '<canvas class="d-flow" width="480" height="220"></canvas>',
    "slack-gif-creator": '<div class="d-rocket">🚀</div>',
    "animated-video": '<div class="d-board"><i>Hook</i><i>Problem</i><i>Product</i><i>CTA</i></div>',
    "figma-motion": '<div class="d-panel"><i></i></div>',
}

FLOW_JS = """
document.querySelectorAll('.d-flow').forEach(cv=>{const x=cv.getContext('2d');let seed=7;
const rnd=()=>(seed=(seed*16807)%2147483647)/2147483647;
const P=[...Array(260)].map(()=>({x:rnd()*cv.width,y:rnd()*cv.height}));
const n=(a,b)=>Math.sin(a*.013+Math.cos(b*.011))*Math.cos(b*.009);
function f(t){x.fillStyle='rgba(13,15,26,.06)';x.fillRect(0,0,cv.width,cv.height);
x.fillStyle='#7cf';for(const p of P){const a=n(p.x+t*.02,p.y)*Math.PI*2;p.x+=Math.cos(a);p.y+=Math.sin(a);
if(p.x<0||p.x>cv.width||p.y<0||p.y>cv.height){p.x=rnd()*cv.width;p.y=rnd()*cv.height}x.fillRect(p.x,p.y,1.4,1.4)}
if(!matchMedia('(prefers-reduced-motion: reduce)').matches)requestAnimationFrame(f)}requestAnimationFrame(f)});
"""

COPY_JS = """
document.addEventListener('click',async ev=>{const b=ev.target.closest('[data-copy]');if(!b)return;
const t=document.getElementById(b.dataset.copy).innerText;
try{await navigator.clipboard.writeText(t);}catch(_){const r=document.createRange();
r.selectNodeContents(document.getElementById(b.dataset.copy));getSelection().removeAllRanges();getSelection().addRange(r);document.execCommand('copy');}
const o=b.textContent;b.textContent='✅ Copied';setTimeout(()=>b.textContent=o,1400);});
document.querySelector('.menu-toggle')?.addEventListener('click',()=>document.body.classList.toggle('nav-open'));
"""

_uid = 0


def block(code, label="📋 Copy", lang=""):
    """Code block with a copy button."""
    global _uid
    _uid += 1
    i = f"c{_uid}"
    return (f'<div class="code"><div class="code-bar"><span>{e(lang)}</span>'
            f'<button data-copy="{i}">{label}</button></div>'
            f'<pre id="{i}"><code>{e(code)}</code></pre></div>')


def menu(active, prefix):
    cats = {}
    for s in skills:
        cats.setdefault(s["category"], []).append(s)
    out = [f'<a class="brand" href="{prefix}index.html">🎬 Animate Skills</a>',
           f'<a href="{prefix}index.html" class="{"on" if active == "home" else ""}">🏠 Overview</a>',
           f'<a href="{prefix}index.html#pipeline">🗂️ Database → Artifact → Execution</a>',
           f'<a href="{prefix}index.html#claude-md">📄 CLAUDE.md</a>',
           f'<a href="{prefix}index.html#hooks">🪝 Hooks</a>']
    for c, items in cats.items():
        out.append(f'<h4>{e(c)}</h4>')
        for s in items:
            on = "on" if s["slug"] == active else ""
            out.append(f'<a class="{on}" href="{prefix}skills/{s["slug"]}.html">{s["emoji"]} {e(s["name"])}</a>')
    out.append('<a class="ext" href="https://skills.sh" target="_blank" rel="noopener">🔎 Browse skills.sh ↗</a>')
    return '<nav class="menu">' + "\n".join(out) + "</nav>"


def page(title, body, active, prefix=""):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(title)}</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🎬</text></svg>">
<link rel="stylesheet" href="{prefix}style.css">
</head><body>
<button class="menu-toggle" aria-label="Menu">☰ Menu</button>
{menu(active, prefix)}
<main>{body}
<footer>Built from <code>skills/skills.json</code> by <code>build.py</code> · served on fly.io · skills via <a href="https://skills.sh">skills.sh</a></footer>
</main>
<script>{COPY_JS}{FLOW_JS}</script>
</body></html>"""


def claude_md_for(s):
    return f"""## Animation skill: {s['name']}
- For {s['when'].rstrip('.').lower()}, load the `{s['slug']}` skill before writing code.
- Runtime: {s['runtime']}. Expected artifact: {s['output']}.
- Animate transform and opacity only; always respect prefers-reduced-motion.
- Put source in `animations/{s['slug']}/`, write rendered output to `out/` (git-ignored).
- After rendering, report the artifact path and how to preview it."""


def hook_for(s):
    cmd = (f"f=$(jq -r '.tool_input.file_path // empty'); "
           f"case \"$f\" in *.{s['hook_ext']}) {s['hook_cmd']} ;; esac; exit 0")
    return json.dumps({"hooks": {"PostToolUse": [{"matcher": "Write|Edit", "hooks": [
        {"type": "command", "command": cmd}]}]}}, indent=2, ensure_ascii=False)


def skill_page(s):
    steps = "".join(f"<li>{e(x)}</li>" for x in s["steps"])
    body = f"""
<header class="hero small"><p class="kicker">{s['emoji']} {e(s['category'])} skill</p>
<h1>{e(s['name'])}</h1><p class="lede">{e(s['summary'])}</p>
<div class="links"><a class="btn" href="{e(s['skills_sh'])}" target="_blank" rel="noopener">🔎 View on skills.sh</a>
<a class="btn ghost" href="{e(s['url'])}" target="_blank" rel="noopener">📦 Source</a></div></header>

<section class="demo">{DEMOS[s['slug']]}</section>

<section class="facts">
<div><span>⚙️ Runtime</span>{e(s['runtime'])}</div>
<div><span>🎁 Artifact</span>{e(s['output'])}</div>
<div><span>🏷️ Source</span>{e(s['source'])}</div>
<div><span>🎯 Use it for</span>{e(s['when'])}</div>
</section>

<h2>⚡ 1. Install (database)</h2>
<p>Pull the skill from the registry into <code>.claude/skills/</code> so the agent can discover it.</p>
{block(s['install'], lang='bash')}

<h2>💬 2. Prompt it (execution)</h2>
<p>Name the skill in your prompt so Claude loads its <code>SKILL.md</code> before acting.</p>
{block(s['prompt'], lang='prompt')}

<h2>🧠 What the agent does</h2><ol class="steps">{steps}</ol>

<h2>🧪 Core pattern (artifact)</h2>
{block(s['code'], lang='code')}

<h2>📄 CLAUDE.md snippet</h2>
<p>Paste into your project's <code>CLAUDE.md</code> so every session knows when to use this skill.</p>
{block(claude_md_for(s), lang='CLAUDE.md')}

<h2>🪝 Hook: check every edit</h2>
<p>Add to <code>.claude/settings.json</code>. After each Write/Edit of a <code>.{e(s['hook_ext'])}</code> file, Claude Code runs the check and the output comes back to the agent.</p>
{block(hook_for(s), lang='.claude/settings.json')}
"""
    return page(f"{s['name']} · Animate Skills", body, s["slug"], prefix="../")


def index():
    rows = "".join(
        f"""<tr><td><a href="skills/{s['slug']}.html">{s['emoji']} {e(s['name'])}</a></td>
<td>{e(s['output'])}</td><td class="cmd">{block(s['install'], '📋', 'bash')}</td>
<td><a href="{e(s['skills_sh'])}" target="_blank" rel="noopener">skills.sh ↗</a></td></tr>"""
        for s in skills)
    cards = "".join(
        f"""<a class="card" href="skills/{s['slug']}.html"><span class="emoji">{s['emoji']}</span>
<b>{e(s['name'])}</b><small>{e(s['category'])} · {e(s['runtime'])}</small></a>""" for s in skills)
    all_install = "\n".join(dict.fromkeys(s["install"] for s in skills if s["install"].startswith("npx")))
    claude_md = """# CLAUDE.md — animation projects

## Skills
- Animation skills live in `.claude/skills/` (installed from skills.sh with `npx skills add`).
- Before writing any animation code, pick the matching skill from `skills/skills.json`
  and load it: Remotion/HyperFrames for video, GSAP/Anime.js/CSS for web,
  Three.js for 3D, Manim for math, algorithmic-art / slack-gif-creator for generative output.

## Rules
- Animate transform and opacity; avoid layout-triggering properties.
- Respect `prefers-reduced-motion` in every artifact.
- Sources in `animations/<skill>/`, rendered artifacts in `out/` (git-ignored).
- When done, state the artifact path and the exact command to preview or render it."""
    hooks = json.dumps({"hooks": {
        "SessionStart": [{"hooks": [{"type": "command",
            "command": "echo \"🎬 Animation skills: $(jq -r '[.[].slug]|join(\", \")' skills/skills.json)\""}]}],
        "PostToolUse": [{"matcher": "Write|Edit", "hooks": [{"type": "command",
            "command": "f=$(jq -r '.tool_input.file_path // empty'); case \"$f\" in *.css|*.html) grep -q prefers-reduced-motion \"$f\" || echo \"⚠️ $f: no prefers-reduced-motion guard\" >&2 ;; esac; exit 0"}]}],
        "Stop": [{"hooks": [{"type": "command", "command": "ls -1 out/ 2>/dev/null | sed 's/^/🎁 artifact: /'"}]}]}},
        indent=2, ensure_ascii=False)
    body = f"""
<header class="hero"><p class="kicker">🧠 LLM skills for motion</p>
<h1>Every animation skill,<br><span class="grad">one place to start.</span></h1>
<p class="lede">{len(skills)} agent skills for making animations — video, web motion, 3D, math and generative art.
Each one gets its own page with a live demo, copy-paste install, a ready prompt, a <code>CLAUDE.md</code> snippet and a hook.</p>
<div class="links"><a class="btn" href="#quickstart">⚡ Quick start</a><a class="btn ghost" href="https://skills.sh" target="_blank" rel="noopener">🔎 skills.sh</a></div></header>

<section class="cards">{cards}</section>

<h2 id="pipeline">🗂️ Database → 🎁 Artifact → 🚀 Execution</h2>
<div class="pipe">
<div><h3>🗂️ Skills database</h3><p>Skills are folders with a <code>SKILL.md</code> (name, description, instructions, scripts). Registries like <a href="https://skills.sh">skills.sh</a> index them; <code>npx skills add owner/repo</code> copies them into <code>.claude/skills/</code>. This site's own database is <code>skills/skills.json</code>.</p></div>
<div><h3>🎁 Artifact</h3><p>What the skill produces: an MP4 from Remotion, HyperFrames or Manim; an HTML page from GSAP, Anime.js, CSS or Three.js; a GIF from slack-gif-creator. Here, <code>build.py</code> turns the database into this site.</p></div>
<div><h3>🚀 Execution</h3><p>Claude only reads each skill's short description until a prompt matches, then it loads the full <code>SKILL.md</code>, writes code, runs the renderer and hands back the artifact. Hooks check each step. This site runs on fly.io.</p></div>
</div>

<h2 id="quickstart">⚡ Quick start</h2>
<p>Install every npx-installable skill at once:</p>
{block(all_install, '📋 Copy all', 'bash')}
<p>Then ask for an animation by naming the skill:</p>
{block('Use the remotion skill to make a 5s animated intro for this repo and render it to out/intro.mp4', lang='prompt')}

<h2>📚 All skills</h2>
<div class="table"><table><thead><tr><th>Skill</th><th>Artifact</th><th>Install</th><th>Registry</th></tr></thead><tbody>{rows}</tbody></table></div>

<h2 id="claude-md">📄 CLAUDE.md</h2>
<p><code>CLAUDE.md</code> is loaded at the start of every session. Use it to tell Claude which animation skill to use and what a finished artifact looks like. This repo ships one; copy it as a starting point:</p>
{block(claude_md, lang='CLAUDE.md')}

<h2 id="hooks">🪝 Hooks</h2>
<p>Hooks are shell commands Claude Code runs at lifecycle events. <b>SessionStart</b> lists the available skills, <b>PostToolUse</b> checks each animation file after it's written, and <b>Stop</b> reports the artifacts that were produced. This is the same config as <code>.claude/settings.json</code> in this repo:</p>
{block(hooks, lang='.claude/settings.json')}

<h2>🛫 Deploy this site</h2>
{block('python3 build.py && fly deploy', lang='bash')}
"""
    return page("Animate Skills", body, "home"), claude_md, hooks


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "skills").mkdir(parents=True)
    shutil.copy(ROOT / "style.css", OUT / "style.css")
    shutil.copy(DB, OUT / "skills.json")
    for s in skills:
        (OUT / "skills" / f"{s['slug']}.html").write_text(skill_page(s))
    idx, claude_md, hooks = index()
    (OUT / "index.html").write_text(idx)
    # Keep the repo's own CLAUDE.md and hooks in sync with what the site shows.
    (ROOT / "CLAUDE.md").write_text(claude_md + "\n")
    (ROOT / ".claude").mkdir(exist_ok=True)
    (ROOT / ".claude" / "settings.json").write_text(hooks + "\n")
    print(f"Built {len(skills)} skill pages + index into {OUT}")


if __name__ == "__main__":
    main()
