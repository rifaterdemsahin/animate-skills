// animated-video skill, Path B: multi-scene storyboard rendered with Remotion.
// Storyboard: hook 2s → problem 3s → product 4s → CTA 3s, joined by 0.5s transitions.
import { linearTiming, springTiming, TransitionSeries } from "@remotion/transitions";
import { fade } from "@remotion/transitions/fade";
import { slide } from "@remotion/transitions/slide";
import { wipe } from "@remotion/transitions/wipe";
import { AbsoluteFill, Easing, interpolate, useCurrentFrame, useVideoConfig } from "remotion";

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const font = "system-ui, sans-serif";

const Hook: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ background: "#0d0f1a", alignItems: "center", justifyContent: "center", fontFamily: font, color: "#fff" }}>
      <div style={{ fontSize: 140, fontWeight: 900, letterSpacing: -4, scale: interpolate(frame, [0, 0.6 * fps], [1.4, 1], { ...clamp, easing: Easing.bezier(0.16, 1, 0.3, 1) }), opacity: interpolate(frame, [0, 0.3 * fps], [0, 1], clamp) }}>
        14 skills.
      </div>
      <div style={{ fontSize: 72, color: "#77ccff", opacity: interpolate(frame, [0.7 * fps, 1 * fps], [0, 1], clamp) }}>One command each.</div>
    </AbsoluteFill>
  );
};

const PAIN = ["Hand-tuned keyframes", "Render pipelines", "Reduced-motion bugs"];
const Problem: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ background: "#16130f", alignItems: "center", justifyContent: "center", gap: 36, fontFamily: font }}>
      {PAIN.map((p, i) => (
        <div key={p} style={{ position: "relative", fontSize: 84, fontWeight: 800, color: "#f6f3ec", opacity: interpolate(frame, [(0.2 + i * 0.35) * fps, (0.5 + i * 0.35) * fps], [0, 1], clamp) }}>
          {p}
          <div style={{ position: "absolute", left: -10, right: -10, top: "52%", height: 10, background: "#e0592a", transformOrigin: "left", scale: `${interpolate(frame, [(1.5 + i * 0.25) * fps, (1.9 + i * 0.25) * fps], [0, 1], { ...clamp, easing: Easing.bezier(0.65, 0, 0.35, 1) })} 1` }} />
        </div>
      ))}
    </AbsoluteFill>
  );
};

const CMD = "npx skills add remotion-dev/skills";
const Product: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const chars = Math.floor(interpolate(frame, [0.3 * fps, 1.8 * fps], [0, CMD.length], clamp));
  return (
    <AbsoluteFill style={{ background: "radial-gradient(circle at 50% 30%, #1f2448, #0d0f1a 70%)", alignItems: "center", justifyContent: "center", gap: 60, fontFamily: font }}>
      <div style={{ width: 1400, borderRadius: 24, background: "#0a0c16", border: "2px solid #262a44", padding: "40px 48px", fontFamily: "ui-monospace, monospace", fontSize: 52, color: "#e8e9f3" }}>
        <span style={{ color: "#6f9" }}>$ </span>
        {CMD.slice(0, chars)}
        <span style={{ opacity: frame % 20 < 10 ? 1 : 0 }}>▍</span>
      </div>
      <div style={{ display: "flex", gap: 40 }}>
        {["🎬 MP4", "🌀 HTML", "🚀 GIF"].map((label, i) => (
          <div key={label} style={{ fontSize: 64, fontWeight: 800, color: "#fff", padding: "28px 48px", borderRadius: 28, background: "#151829", border: "2px solid #cc77ff",
            translate: interpolate(frame, [(2 + i * 0.2) * fps, (2.6 + i * 0.2) * fps], ["0px 80px", "0px 0px"], { ...clamp, easing: Easing.spring({ damping: 14 }) }),
            opacity: interpolate(frame, [(2 + i * 0.2) * fps, (2.3 + i * 0.2) * fps], [0, 1], clamp) }}>
            {label}
          </div>
        ))}
      </div>
    </AbsoluteFill>
  );
};

const CTA: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ background: "linear-gradient(135deg, #77ccff, #cc77ff)", alignItems: "center", justifyContent: "center", fontFamily: font, color: "#0d0f1a" }}>
      <div style={{ fontSize: 60, fontWeight: 700, opacity: 0.8 }}>Browse more at</div>
      <div style={{ fontSize: 200, fontWeight: 900, letterSpacing: -6, scale: interpolate(frame, [0, 0.8 * fps], [0.8, 1], { ...clamp, easing: Easing.spring({ damping: 10 }), output: "perceptual-scale" }) }}>skills.sh</div>
    </AbsoluteFill>
  );
};

export const Storyboard: React.FC = () => {
  const { fps } = useVideoConfig();
  return (
    <TransitionSeries>
      <TransitionSeries.Sequence name="Hook" durationInFrames={2 * fps}>
        <Hook />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={wipe({ direction: "from-left" })} timing={linearTiming({ durationInFrames: 0.5 * fps })} />
      <TransitionSeries.Sequence name="Problem" durationInFrames={3 * fps}>
        <Problem />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={slide({ direction: "from-bottom" })} timing={springTiming({ config: { damping: 200 }, durationInFrames: 0.5 * fps })} />
      <TransitionSeries.Sequence name="Product" durationInFrames={4 * fps}>
        <Product />
      </TransitionSeries.Sequence>
      <TransitionSeries.Transition presentation={fade()} timing={linearTiming({ durationInFrames: 0.5 * fps })} />
      <TransitionSeries.Sequence name="CTA" durationInFrames={3 * fps}>
        <CTA />
      </TransitionSeries.Sequence>
    </TransitionSeries>
  );
};
