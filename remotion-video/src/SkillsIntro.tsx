import { AbsoluteFill, Easing, Interactive, interpolate, useCurrentFrame, useVideoConfig } from "remotion";

const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

const Title: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <Interactive.Div
      name="Title"
      style={{
        fontSize: 120,
        fontWeight: 900,
        letterSpacing: -3,
        lineHeight: 1,
        textAlign: "center",
        background: "linear-gradient(90deg,#77ccff,#cc77ff)",
        WebkitBackgroundClip: "text",
        color: "transparent",
        scale: interpolate(frame, [0, 1 * fps], [0.6, 1], { ...clamp, easing: Easing.spring({ damping: 12 }), output: "perceptual-scale" }),
        opacity: interpolate(frame, [0, 0.4 * fps], [0, 1], clamp),
      }}
    >
      Animate
      <br />
      Skills
    </Interactive.Div>
  );
};

const Stat: React.FC<{ value: string; label: string; delay: number }> = ({ value, label, delay }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <Interactive.Div
      name={label}
      style={{
        width: 260,
        padding: "28px 0",
        borderRadius: 28,
        background: "#151829",
        border: "2px solid #262a44",
        textAlign: "center",
        translate: interpolate(frame, [delay * fps, (delay + 0.8) * fps], ["0px 120px", "0px 0px"], { ...clamp, easing: Easing.spring({ damping: 14 }) }),
        opacity: interpolate(frame, [delay * fps, (delay + 0.3) * fps], [0, 1], clamp),
      }}
    >
      <div style={{ fontSize: 96, fontWeight: 900, color: "#fff" }}>{value}</div>
      <div style={{ fontSize: 40, color: "#9a9db8" }}>{label}</div>
    </Interactive.Div>
  );
};

export const SkillsIntro: React.FC = () => {
  return (
    <AbsoluteFill
      style={{
        background: "radial-gradient(circle at 50% 35%, #1f2448, #0d0f1a 70%)",
        fontFamily: "system-ui, sans-serif",
        alignItems: "center",
        justifyContent: "center",
        gap: 90,
      }}
    >
      <Title />
      <div style={{ display: "flex", gap: 40 }}>
        <Stat value="14" label="skills" delay={1.2} />
        <Stat value="12" label="outputs" delay={1.5} />
        <Stat value="1" label="database" delay={1.8} />
      </div>
    </AbsoluteFill>
  );
};
