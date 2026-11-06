# ai-voice web searches, 2026-11-06

All ten rows of the beat's `searches.md` (first scan of the month, so monthly rows too). Search summaries, not pages read, unless noted.

Nothing dated November 2026 turned up for new open models, local comparisons, ComfyUI nodes, singing, game backlash or union terms. The date term in these queries mostly returns older pages, so absence means little.

| topic | found | use |
|---|---|---|
| Hume | Date and data deletion repeated by Cartesia, Neocortex, Voice Over Herald and others; one search summary quotes "12:01 a.m. EST". Fetched Hume's intro, changelog, voice overview and TTS reference: all show only the Audio Decisions API, no notice. | Not confirmed from Hume. Treated as ending: `references/engines.md`. |
| Cartesia | Third-party tracker: voice agent rate cut from $0.06 to $0.03 a minute, week of 2026-11-02; LLM use billed separately. Not read on Cartesia's page. | Agents, outside this plugin's scope. Not added. |
| NO FAKES Act | One source: Senate Judiciary advanced it 2026-06-18 by voice vote, as S. 4591; other trackers still show S. 1367. Not law. | Check congress.gov before `references/rights.md` says anything. Not added. |
| SAG-AFTRA | TV animation contracts ran to 2026-06-30; renewal not confirmed. A "Framework Agreement" claim of 2026-03-05 comes from an unreliable site. | Not added. |
| Games | Arc Raiders re-recorded ping lines after backlash (March 2026, via an aggregator citing Polygon). | Already the general lesson. Not added. |
| Metallic sound | One Reddit report: artifacts growing past about 2 minutes of continuous generation, on Gemini TTS; chunking fixes it and shifts prosody. | Single report. Not added. |
| Singing | SoulX-Singer (arXiv 2602.07803, February). | Belongs to musicwright's boundary. Not added. |

## VIPBench, read 2026-11-06

Tang and Groh, arXiv 2611.05638, NeurIPS 2026. The first 100,000 of about 130,000 characters read through a fetch summary, not line by line.

P(same) by pair: same speaker real-real 0.69, same speaker real-clone 0.59, different speaker real 0.26, different speaker clone 0.27. The scout note's 41% reads worse than it is without the 31% real-real figure.

Models: eleven, CAM++ absent. Resemblyzer best (r 0.656, AUC 0.872); ECAPA-TDNN r 0.646, AUC 0.862; WeSpeaker ResNet34-LM r 0.627, AUC 0.851. A fixed cut-off is not recommended; Platt calibration is, for a confidence. Clones are nearly all Cartesia Sonic 3, with a 60-pair CosyVoice 2 subset too small to compare engines. Data at `sendfuze/vipbench` on Hugging Face; no licence stated on the page read, so it was not downloaded. Testing CAM++ on it needs that licence checked first.
