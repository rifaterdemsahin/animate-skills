"""Pythagorean theorem explainer (Manim Community Edition).

Render:  manim -pqh pythagoras.py Pythagoras
Needs:   pip install manim  (plus system cairo/pango, e.g. apt install libcairo2-dev libpango1.0-dev)
"""
from manim import (BLUE, DOWN, GREEN, LEFT, ORIGIN, RIGHT, UP, WHITE, YELLOW, Create, FadeIn,
                   MathTex, Polygon, Scene, Square, Transform, VGroup, Write)


class Pythagoras(Scene):
    def construct(self):
        a, b = 3, 4
        tri = Polygon(ORIGIN, RIGHT * a, UP * b, color=WHITE).shift(LEFT * 1.5 + DOWN * 1.5).scale(0.6)
        self.play(Create(tri))

        p0, p1, p2 = tri.get_vertices()
        sq_a = Square(side_length=a * 0.6, color=BLUE, fill_opacity=0.4).next_to(tri, DOWN, buff=0)
        sq_a.align_to(tri, LEFT)
        sq_b = Square(side_length=b * 0.6, color=GREEN, fill_opacity=0.4).next_to(tri, LEFT, buff=0)
        sq_b.align_to(tri, DOWN)
        hyp = Square(side_length=5 * 0.6, color=YELLOW, fill_opacity=0.4)
        hyp.move_to((p1 + p2) / 2).rotate(-0.9273).shift((RIGHT + UP) * 0.9)
        self.play(FadeIn(sq_a, shift=DOWN), FadeIn(sq_b, shift=LEFT))
        self.play(FadeIn(hyp, scale=0.5))

        eq = MathTex("a^2", "+", "b^2", "=", "c^2").to_edge(UP)
        eq[0].set_color(BLUE); eq[2].set_color(GREEN); eq[4].set_color(YELLOW)
        self.play(Write(eq))
        nums = MathTex("9", "+", "16", "=", "25").to_edge(UP)
        self.play(Transform(eq, nums))
        self.play(eq.animate.scale(1.4).set_color(YELLOW))
        self.wait()
