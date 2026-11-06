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

Models: eleven, CAM++ absent. Resemblyzer best (r 0.656, AUC 0.872); ECAPA-TDNN r 0.646, AUC 0.862; WeSpeaker ResNet34-LM r 0.627, AUC 0.851. A fixed cut-off is not recommended; Platt calibration is, for a confidence. Clones are nearly all Cartesia Sonic 3, with a 60-pair CosyVoice 2 subset too small to compare engines. Data at `sendfuze/vipbench` on Hugging Face, CC BY-NC 4.0 per its card.

### CAM++ on VIPBench, 2026-11-06

Mark asked for this as a private report: no threshold comes from it, and the audio stays in `voicewright-lab/vipbench` (scorer `vipbench_score.py`, per-pair scores `campp_scores.csv`). The model is voicewright's own CAM++, cosine, all 9,800 pairs of the main set. Only these aggregate figures are recorded here. Data: VIPBench, Tang and Groh, CC BY-NC 4.0.

Overall: Pearson r 0.635 to human P(same), AUC 0.833 to the human majority. Without morphs (1,700 pairs): r 0.789, AUC 0.903 to the majority, 0.996 to the true label.

| pair type | n | median score | mean human P(same) | share at 0.55 or over | r to P(same) |
|---|---|---|---|---|---|
| same recording | 100 | 0.898 | 0.907 | 100% | 0.276 |
| same speaker, real | 400 | 0.743 | 0.689 | 96.5% | 0.541 |
| same speaker, clone | 400 | 0.621 | 0.593 | 76% | 0.405 |
| different speakers, real | 400 | 0.180 | 0.263 | 0.3% | 0.449 |
| different speakers, clone | 400 | 0.166 | 0.274 | 0% | 0.372 |
| morphs | 8,100 | 0.448 | 0.381 | 34.4% | 0.587 |

Reading: CAM++ sits in the paper's model range, r 0.635 against 0.627 to 0.656, but this is my own scoring and fbank, with raw cosine and no Platt step, so it is not a formal entry on that table. At 0.55, 24% of same-speaker Cartesia clones fall short while different-speaker pairs almost never pass, which supports a low score meaning "listen", not "reject". Within any one type the correlation with listeners is modest, so the score cannot replace the ear. Clones are one engine, not ours; no threshold changed.
