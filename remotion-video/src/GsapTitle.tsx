import gsap from "gsap";
import { DrawSVGPlugin } from "gsap/DrawSVGPlugin";
import { SplitText } from "gsap/SplitText";
import { AbsoluteFill } from "remotion";
import { useGSAPTimeline } from "./useGSAPTimeline";

gsap.registerPlugin(SplitText, DrawSVGPlugin);

export const GsapTitle: React.FC = () => {
  const ref = useGSAPTimeline((tl, root) => {
    const split = SplitText.create(root.querySelector(".headline"), { type: "chars", mask: "chars" });
    tl.from("#ring", { drawSVG: "0%", duration: 1.2, ease: "power2.inOut" })
      .from(split.chars, { yPercent: 110, stagger: 0.04, duration: 0.7, ease: "back.out(1.8)" }, "-=0.6")
      .from(".sub", { opacity: 0, y: 30, duration: 0.6, ease: "power3.out" }, "-=0.2")
      .to("#ring", { rotate: 180, transformOrigin: "50% 50%", duration: 1.6, ease: "expo.inOut" }, "+=0.3")
      .to(split.chars, { color: "#77ccff", stagger: { each: 0.03, from: "center" }, duration: 0.3 }, "<");
  });

  return (
    <AbsoluteFill style={{ background: "#0d0f1a", alignItems: "center", justifyContent: "center", fontFamily: "system-ui, sans-serif" }}>
      <div ref={ref} style={{ position: "relative", display: "grid", placeItems: "center" }}>
        <svg width={900} height={900} viewBox="0 0 900 900" style={{ position: "absolute" }}>
          <circle id="ring" cx={450} cy={450} r={400} fill="none" stroke="#cc77ff" strokeWidth={10} strokeLinecap="round" />
        </svg>
        <div className="headline" style={{ fontSize: 150, fontWeight: 900, color: "#fff", letterSpacing: -4 }}>
          GSAP × Remotion
        </div>
        <div className="sub" style={{ fontSize: 48, color: "#9a9db8", marginTop: 20 }}>
          paused timeline · seek(frame / fps)
        </div>
      </div>
    </AbsoluteFill>
  );
};
