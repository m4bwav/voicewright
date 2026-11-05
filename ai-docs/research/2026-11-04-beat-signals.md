# What the first ai-voice scan says for the build

Date: 2026-11-04. Source: everscout beat `ai-voice`, 29 notes in the everscout data folder for this beat. Note ids are the start of each file name.

How far to trust this: it is one scan over about two weeks. Most of the 407 items were off-topic. Most threads are opinion with no samples, and I did not listen to any audio. ElevenLabs is over-represented because its forum is on the watch list. Treat this as leads to test, not findings.

## Engines people use

- Finished work mixes engines. A weekly puppet show drafts on Chatterbox and bakes finals on ElevenLabs clones of the same samples (1xktfiq). A 14-chapter audio drama used ElevenLabs with Kokoro for a few parts (1xnx3yv).
- One commenter who says they run a commercial podcast studio ranks Fish Audio Drama 3, then Qwen, then Chatterbox (1xmwbkt). They credit very clean references. This is one voice, not a survey.
- No local winner exists. Pocket TTS, VibeVoice 7B, Chatterbox, Breeze, Ming 3.0, Omnivoice and SuperTonic all get named (1xcpkyg, 1xmwbkt). So the plugin should not hard-code a best engine.
- Licences are argued in the threads. Fish and Breeze are both challenged (1xcpkyg, 1xmwbkt). Read them at the source.
- Eleven v4 led the one preference score I could read, at Elo 1334 (web-de73d772). TTS Arena did not load, so there is no second blind source.
- Hume's Octave and EVI APIs are reported to end on 2026-11-13, with account data deleted (web-829296cc). The source is a competitor. Hume's docs pages I read showed no notice, though they now describe a different API. Confirm this, and do not build a route on Octave.

## Complaints

- Model upgrades change voices. On v4, serious voices turn happy, British turns American, and previews differ from output (1xjna00).
- Clones do not match on newer models, by several users' account (1xdrure).
- Voice verification may block cloning from AI-made samples (1xnphai). This is one user's report. Another account's missing clone options look account-specific (1xn5za0).
- Names are a lottery on Gemini TTS, and respelling did not help (1xmxcnp).
- Local Chatterbox sometimes adds breaths or a drone, so one tester checks every output (1xcpkyg).

## Consistency tricks

- Pin the model. Some hosted users stay on old versions for this reason (1xdrure). Record the engine version with every voice.
- Keep one reference set across draft and final (1xktfiq).
- Review takes on a page where a line is picked or marked for redo (1xktfiq).
- Make one call per speaker turn. Multi-speaker mode reassigned voices and truncated for one maker (1xmxcnp).
- Keep style instructions out of the spoken text. They were read aloud on about 2.5 percent of turns for that maker (1xmxcnp).
- Clone strength exists only for ElevenLabs professional clones (1xihsl6). Advice must name the clone type.
- Weighted voice mixing is one cheap way off presets, reported by one person with no measure (1xhsk63).

## Checks to build

- A Whisper check does not catch a wrong name, since Whisper fixes the spelling (1xmxcnp). Do not sell a transcript check as a pronunciation check.
- A listen or an automatic check is needed per take (1xcpkyg). I found nothing here on which automatic check works.

## Reception

- Several listeners blame the script first, then voices that are too perfect, too dramatic or recognisably one vendor (1xivxgn). This argues for a rewrite-for-speech step. A counterpoint in the same thread says audiobooks and ads want clean reads.
- Monotone delivery gets read as AI even when no AI may be involved (1xmewoc).
- Audiobook buyers filter AI out, and Libby's human-narrators preference was welcomed (1xkeyrx). Voice actors are hostile (1xnyhc6).
- Disclosure timing became the story for one game (web-49fc6587). Steam names sound but not voice in its AI section (web-48728e4b).
- Accent models aim to avoid caricature, and consent is used as a selling point (50227330). Listener acceptance was not tested.

## Law and consent

- NO FAKES is not law. A unanimous-consent attempt failed on 2026-09-30, per a secondary source (web-40f94b15).
- Performers treat silent contracts as a risk and reach for the NAVA AI rider (1xiddki). A consent checklist could point to it. Have a lawyer check any wording.

## Thin or missing

- Cleanup: one music-side thread on separation (1xl0diq). Nothing tested on metallic TTS output.
- Singing: one ComfyUI node with no independent results (1xmcemk).
- Why voices collapse into a few sounds: no direct evidence. Voice design demand shows, quality does not (1xhac0j).
- Searches for November 2026 releases, law and pricing found almost nothing dated this month.
- Non-English: one model card only (web-a5a50723).
