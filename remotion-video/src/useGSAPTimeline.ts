// Bridge from the gsap-animation skill: a paused GSAP timeline seeked to frame / fps.
import gsap from "gsap";
import { useEffect, useRef, useState } from "react";
import { continueRender, delayRender, useCurrentFrame, useVideoConfig } from "remotion";

export function useGSAPTimeline(build: (tl: gsap.core.Timeline, root: HTMLDivElement) => void) {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const ref = useRef<HTMLDivElement>(null);
  const tl = useRef<gsap.core.Timeline | null>(null);
  const [handle] = useState(() => delayRender("gsap timeline + fonts"));

  useEffect(() => {
    let ctx: gsap.Context | undefined;
    document.fonts.ready.then(() => {
      if (!ref.current) return;
      ctx = gsap.context(() => {
        const t = gsap.timeline({ paused: true });
        build(t, ref.current!);
        tl.current = t;
        t.seek(frame / fps);
      }, ref);
      continueRender(handle);
    });
    return () => ctx?.revert();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  useEffect(() => {
    tl.current?.seek(frame / fps);
  }, [frame, fps]);

  return ref;
}
