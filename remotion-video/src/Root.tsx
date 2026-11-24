import { Composition } from "remotion";
import { GsapTitle } from "./GsapTitle";
import { SkillsIntro } from "./SkillsIntro";
import { Storyboard } from "./Storyboard";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition id="SkillsIntro" component={SkillsIntro} durationInFrames={120} fps={30} width={1080} height={1080} />
      <Composition id="GsapTitle" component={GsapTitle} durationInFrames={150} fps={30} width={1920} height={1080} />
      {/* 12s of scenes minus three 0.5s transition overlaps = 10.5s */}
      <Composition id="Storyboard" component={Storyboard} durationInFrames={315} fps={30} width={1920} height={1080} />
    </>
  );
};
