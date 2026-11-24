import { Composition } from "remotion";
import { GsapTitle } from "./GsapTitle";
import { SkillsIntro } from "./SkillsIntro";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition id="SkillsIntro" component={SkillsIntro} durationInFrames={120} fps={30} width={1080} height={1080} />
      <Composition id="GsapTitle" component={GsapTitle} durationInFrames={150} fps={30} width={1920} height={1080} />
    </>
  );
};
