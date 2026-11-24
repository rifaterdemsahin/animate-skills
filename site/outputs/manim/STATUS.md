# Manim: written, not rendered here

`pythagoras.py` is a complete Manim CE scene. It wasn't rendered on the build machine because Manim needs
**pycairo**. pycairo ships no Linux wheels, so building it needs the system `libcairo2-dev` and `pango`
headers, and those need sudo.

To render it yourself:
```bash
sudo apt install libcairo2-dev libpango1.0-dev ffmpeg
pip install manim
manim -pqh pythagoras.py Pythagoras
```
