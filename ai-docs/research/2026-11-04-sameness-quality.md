# Voicewright research: sameness, quality, checks, stereotype

Date checked for every claim: 2026-11-04, shown after each source.
Sureness: H = primary source or paper read. M = paper snippet, or several practitioners. L = one anecdote, vendor blog or my inference.
Reddit was only seen through search results and one mirror. Arctic Shift and Gemini grounding were not used. Nothing was installed.

## Read this first: what the evidence does not show

- I found no test of a denoiser run on TTS output. The "denoisers harm TTS" case below rests on nearby evidence. Voicewright should measure this itself.
- I found no controlled test of RVC over a base performance, of formant shifting on TTS, or of seed search as a way to widen range.
- I found no sourced thresholds for sibilance, breath count or metallic sound. Numbers marked "starter" are my guesses and need calibration.
- Search snippets were thin on forum reports. Vendor and tool docs are over-represented in places.

## 1. Why AI voices sound the same

### Stock counts

- [H] Kokoro has 54 voices: 29 female, 25 male. Only 28 are English (20 American, 8 British). Grades run from A (only af_heart) to F+ (am_adam). Less training audio gives a lower grade. https://huggingface.co/hexgrad/Kokoro-82M/raw/main/VOICES.md (2026-11-04)
- [H] OpenAI has 13 built-in voices. Marin and cedar are recommended for best quality. Custom voices need a consent recording. tts-1, tts-1-hd and gpt-4o-mini-tts shut down on 2027-01-06. https://developers.openai.com/api/docs/guides/text-to-speech (2026-11-04)
- [H] Gemini lists 30 curated voices, plus an Extended Voice Library with "hundreds more". It now offers voice replication from reference and consent audio, with a quota of 200 stored voices per project. Third-party blogs saying "no cloning" conflict with this; trust the doc. https://aistudio.google.com/docs/speech-generation (2026-11-04)
- [M] VibeVoice realtime 0.5B ships 25 baked preset voices per one mirror. One setup lists 9. The 1.5B and 7B models clone from samples, for up to 4 speakers. https://huggingface.co/AEmotionStudio/vibevoice-models/blob/main/README.md and https://github.com/vibevoice-community/VibeVoice (2026-11-04)

### What text prompting really reaches

- [H] Prompting moves delivery, not identity. OpenAI instructions control accent, emotion, intonation, speed, tone and whispering. https://developers.openai.com/api/docs/guides/text-to-speech (2026-11-04)
- [H] Google now says long director's-notes blocks are "the most common cause of voice drift". Asking to "maintain identical timbre" adds drift. Do not put age, gender, names or a permanent accent in style. Pick a voice instead, and keep style short or empty. https://aistudio.google.com/docs/speech-generation (2026-11-04)
- [M] Prompted voice design defaults toward one group. ElevenLabs v2 voices prompted with adjectives only: listeners heard them as white (93%), male (86.6%), US-accented (60%). 30 voices, 60 listeners. Ross, Markl, Lai, Hall-Lew, CHI 2026. Figures come from a search summary; a direct fetch of the PDF returned 404. https://repository.essex.ac.uk/43154/1/3772363.3798657.pdf (2026-11-04)

### Methods that widen range

**Embedding blending.** Works, with limits.
- [H] KTH blended XTTS speaker embeddings on 20 VCTK speakers with 7 weights. ECAPA similarity between output and a source voice: 0.12 +/- 0.11 at weight 0, 0.32 +/- 0.14 at weight 0.5, 0.52 +/- 0.11 at weight 1. XTTS's own encoder: 0.27, 0.44, 0.61. So a midpoint blend is measurably between the two voices. Even an unblended voice only scored 0.52 on ECAPA. https://www.speech.kth.se/~jocke/publications/francis25_ssw.pdf (2026-11-04)
- [H] Same paper: outputs get less consistent when few training voices sit near the blend (cosine 0.6 or higher). Consistency plateaus at about 400 to 450 nearby embeddings on the XTTS encoder. Blends in empty regions are unstable, and those are also the novel ones. No listening test was done. Same URL (2026-11-04)
- [M] Kokoro practitioners blend accents and add a little of a voice for a trait: "a bit of Heart to make flatter voices slightly more melodic", "a bit of Nicole" for punchier consonants. One author. https://github.com/hexgrad/kokoro/pull/127 (2026-11-04)
- [M] Tool docs warn that results vary and that same-language, similar voices blend best. https://pykokoro.readthedocs.io/en/stable/advanced_features.html (2026-11-04)
- [M] One 2025 method (INSIDE) uses SLERP and blends within gender groups to avoid crossing major acoustic boundaries. https://arxiv.org/html/2508.19210v1 (2026-11-04; URL attribution inferred from the search listing)
- [L] My inference: averaging many voices pulls toward the centre. Blend 2 or 3 distinct voices, not many.

**Seed search.** Real only on some engines.
- [H] Dia is not tuned to one voice, so each run can give a different voice. Fix the seed or use an audio prompt to hold it. https://github.com/nari-labs/dia (2026-11-04)
- [M] VibeVoice: same text, voice and seed gives the same read. https://floyo.ai/workflows/vibevoice-single-speaker-text-to-spe-64e224cms1m1 (2026-11-04)
- [L] Inference: seed search finds new identities only on engines with no fixed speaker. A good take must then be frozen as a reference clip.

**Voice conversion over a base performance.** Keeps a chosen read, with artifact risk.
- [M] A 2025 study found RVC leaves pitch contours nearly unchanged and changes formant structure. https://arxiv.org/pdf/2507.03641 (2026-11-04)
- [H] Users report metal on S sounds and breaths. Training longer did not cure it. One reply: small datasets may do better with shorter training. Another: 20+ minutes of data can smooth it slightly. https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/issues/119 (2026-11-04)
- [L] Fix reported in that thread by one user: a de-esser on the result, or split at 6 kHz, compress the top band heavily, lower it and merge. Same URL (2026-11-04)
- [M] Another report: every trained model sounded metallic, at 90 to 220 epochs, with or without the index, even on training clips. A commenter's 15 minutes of ElevenLabs-made data also came out robotic. Unresolved. https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI/issues/2689 (2026-11-04)
- [M] Lower index rate reduces artifacts. Protect guards consonants and breaths; 0.33 is one default, 0.5 disables it. https://git.tdem.in/blaise-tk/RVC_CLI/blob/main/README.md and https://replicate.com/meta-innovation/ultimate_rvc/versions/5598e8029cbd7e9268db84ce8c2a334eab6ebccbee67b78cf63c38e964379e15/api (2026-11-04)

**Unusual reference material.** Untested as a range method.
- [M] Engines copy what is in the clip, noise and music included. Chatterbox: https://dev.to/pekisko/fine-tuning-chatterbox-on-a-low-resource-language-7-things-that-mattered-13e1 . VibeVoice: floyo URL above. Paper on copying noise style: https://arxiv.org/html/2406.05699v1 (2026-11-04)
- [L] Inference from KTH: voices far from the training data render less stably, so odd references may lose accuracy or slide toward the middle. Test with a speaker model before and after.

**Formant and pitch work.** No quality test found.
- [M] RVC has semitone pitch control (-24 to +24), and RVC-CLI has optional formant shifting. Config docs only. https://git.tdem.in/blaise-tk/RVC_CLI/blob/main/README.md (2026-11-04)
- [L] Formants look like the right lever given the RVC study above. Verify by ear and by embedding.

**Model merging.**
- [M] Averaging the weights of two fine-tuned TTS models gives in-between attributes with no new data. https://www.themoonlight.io/review/an-attribute-interpolation-method-in-speech-synthesis-by-model-merging (paper arXiv 2407.00766, 2026-11-04)

## 2. Why they sound bad, and what people do

### Reference clips

- [H] Dia: 5 to 10 seconds, with the transcript before the generation text. https://github.com/nari-labs/dia (2026-11-04)
- [M] VibeVoice: clean 5 to 10 seconds; one checkpoint rejects clips over 30 seconds. https://huggingface.co/thangylvp/vibevoice-0.5b-custom (2026-11-04)
- [M] Chatterbox guides disagree: 10 to 30 seconds, 15 to 30 if the match is poor, one API takes 7 to 20. https://docs.clore.ai/guides/audio-and-voice/chatterbox-tts (2026-11-04)
- [M] Ambience in the clip is carried into every generation. See the Chatterbox and VibeVoice links above.
- [L] Voices recorded in different rooms leave audible reverb differences in a multi-voice model. One HN listener. https://news.ycombinator.com/item?id=45114872 (2026-11-04)
- [M] A Microsoft paper calls enhancing the clip first "the most naive approach": enhancement models "inevitably cause processing artifacts" that degrade TTS, and its noise-robust training beat enhance-first on intelligibility, similarity and quality. Abstract-level only, and the authors are selling their alternative. https://arxiv.org/html/2406.05699v1 (2026-11-04)

### Chunking

- [H] Length windows are engine-specific. Dia: under 5 seconds sounds unnatural, over about 20 seconds runs unnaturally fast. https://github.com/nari-labs/dia (2026-11-04)
- [M] Chatterbox Turbo: above about 350 characters users report heavy hallucination. https://github.com/resemble-ai/chatterbox/issues/424 (2026-11-04)
- [M] Chatterbox also fails the other way: "Hi!", "Why?", "Yes", single letters give gibberish. Changing cfg, exaggeration, temperature and seed did not help that user. An audiobook builder saw the same on short lines. https://github.com/resemble-ai/chatterbox/issues/97 (2026-11-04)
- [M] Tail faults: long hallucination, silence or breathing at the end of a take. Title only read. https://github.com/resemble-ai/chatterbox/issues/388 (2026-11-04)
- [M] Common practice: split by sentence, generate each, join with a short crossfade. https://dev.to/pekisko/fine-tuning-chatterbox-on-a-low-resource-language-7-things-that-mattered-13e1 (2026-11-04)

### Text normalization and prosody

- [M] Numbers, abbreviations and currency need expansion, plus pronunciation dictionaries. Vendor source. https://www.plushcap.com/content/deepgram/blog/deepgram-open-source-text-to-speech-production-implementation-guide (2026-11-04)
- [L] A local-assistant builder: Kokoro and Piper train on read speech, so conversation gets wrong breath groups and function-word stress, and numbers and addresses sound off. One commenter, whose comment links a vendor. https://news.ycombinator.com/item?id=47402966 (2026-11-04)

### Inference settings

- [M] Chatterbox defaults are exaggeration 0.5 and cfg 0.5. Fast reference voice: cfg about 0.3. Dramatic: cfg about 0.3 with exaggeration 0.7 or more, since exaggeration speeds speech up and lower cfg slows it. cfg 0 can cut accent carry-over between languages. https://huggingface.co/ModelsLab/chatterbox (2026-11-04)
- [H] Dia: non-verbal tags used too much or off-list cause artifacts. https://github.com/nari-labs/dia (2026-11-04)

### Do denoisers add their own artifacts to TTS?

Short answer: likely, but untested on TTS output in what I found. Sureness M for the mechanism, L for the size.
- [H] Enhancement can invent sound. A hallucinated speech-like artifact appeared in the first half second when training leaned on a quality predictor. 16 listeners partly heard it as background. This concerns models trained that way, not stock tools. https://arxiv.org/html/2403.11732v2 (2026-11-04)
- [M] URGENT 2025: listening MOS can ignore intelligibility and phone errors, so pair it with ESTOI or a content check. https://arxiv.org/pdf/2507.11306 (2026-11-04)
- [M] Adobe Enhance reviews: can sound artificial, worst on recordings that were already decent. Reports of metallic and hollow voices and lost breaths. A second pass can compound it. Lower the strength. Reviews, not measurement. https://diyai.io/ai-tools/audio-generation/reviews/adobe-podcast-ai-enhancer-review/ and https://www.ruzuku.com/learn/tools/adobe-podcast/clean-up-audio (2026-11-04)
- [L] A practitioner piece also says noise removal often leaves a "thin" or "metallic" voice. https://dev.to/ezinne_anne/why-your-ai-voiceovers-sounds-robotic-and-how-to-fix-them-4ga3 (2026-11-04)
- [H] Resemble Enhance has two stages. The enhancer restores distortion and extends bandwidth, so it generates content. A `--denoise_only` mode exists. Licence MIT per GitHub. https://github.com/resemble-ai/resemble-enhance (2026-11-04)
- [M] Issue search on resemble-enhance for "artifacts" and "metallic" gave 0 hits; recent titles are mostly installs. One issue says the web UI and public model differ (#64, title only). Absence of reports is not evidence of safety. https://github.com/resemble-ai/resemble-enhance/issues/64 (2026-11-04)
- [L] DeepFilterNet is praised for noise, with one HN user preferring Adobe for quality. No TTS test found. GitHub shows its licence as NOASSERTION, so read the repo before bundling. https://news.ycombinator.com/item?id=48888313 (2026-11-04)
- [L] Inference: clean TTS has little noise to remove, so a denoiser mainly risks harm. Default: do not denoise TTS output unless a check finds noise. Compare before and after by ear, ASR and speaker similarity.
- iZotope RX: no test reports on TTS found.

### Room tone, EQ matching, final mix

- [M] iZotope Dialogue Match profiles a clip's EQ, noise floor and space, and applies it to dialogue of 3 seconds or more. Pro Tools AudioSuite, listed at about $599. https://www.prosoundweb.com/izotope-launches-new-dialogue-match-tool-for-audio-post-production/ and https://www.rspeaudio.com/izotope-dialogue-match (2026-11-04)
- [L] Acon Extract Dialogue 2 splits voice, room reverb and noise. Promotional source. https://www.podcastvideos.com/mastering-dialogue-perspective-automating-workflows-with-acon-digital-extract-dialogue-2/ (2026-11-04)
- [L] Room tone at -50 to -60 dB under the voice, ducked 1 to 2 dB while speaking. AI voices often pierce at 2 to 4 kHz; cut slightly. https://dev.to/ezinne_anne/why-your-ai-voiceovers-sounds-robotic-and-how-to-fix-them-4ga3 (2026-11-04)
- [L] Reddit post via a mirror: a dry voice needs matched convolution reverb, a constant bed sidechained to the voice, trimmed highs for distance, added breaths and uneven pauses. Order: EQ, reverb, level and pan. The reply was itself a Gemini-written guide, so it counts as opinion. https://reddit.sentinel-team.org/posts/1tdoc54/snapshots/2026-05-16T01%3A45%3A46.711269Z (2026-11-04)
- [M] ACX, a useful delivery yardstick: RMS -23 to -18 dBFS, peak at or below -3 dBFS, noise floor at or below -60 dBFS RMS. Sources disagree on whether silence counts in RMS. https://webcf.waybackmachine.org/web/20210510175948/https://www.acx.com/help/acx-audio-submission-requirements/201456300 and https://forum.audacityteam.org/t/meeting-acx-audio-submission-requirements/58706 (2026-11-04)

## 3. What a script can detect

### Plain signal checks (no licence issue)

"Starter" values are my guesses (L). Calibrate on known good and bad clips first.

| Fault | Measure | Starter value | Basis |
|---|---|---|---|
| Clipping | runs of 3+ samples near full scale | any run | L, common practice |
| Peak | true peak | above -3 dBFS | M, ACX |
| Level | RMS or LUFS per file | -23 to -18 dBFS RMS | M, ACX |
| Noise floor | quietest 10% of frames | above -60 dBFS | M, ACX |
| Digital silence | exact zero between words | any long gap in a mixed file | L |
| Level jump | short-term loudness change across a chunk join | over 3 dB | L |
| Fake bandwidth | energy above a cutoff, sudden shelf | sharp drop below 16 kHz in a 44.1 kHz file | M, see below |
| Sibilance | 5 to 9 kHz energy over total, bursts | relative to the voice's own median | L, no source found |
| Harsh band | 2 to 4 kHz over the mean | relative to reference | L |
| Metallic sound | spectral flatness in top bands, frame-to-frame HF flux | relative to reference | L, no validated metric found |
| Breaths | low-level broadband unvoiced bursts between phrases | zero in 60 s is suspicious | L |
| Room tone | noise spectrum in pauses | differs between chunks | L |
| Tail junk | energy after the last ASR word | over 0.5 s | M for the fault, L for the value |
| Wrong words | ASR against script (WER) | any content miss | M, URGENT advice |

- [M] Patent method: resampled audio shows near-zero energy above half the original rate. Codecs cause the same shape, so this flags an upsample, not synthesis. https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12067995 (2026-11-04; which patent said this is inferred from the listing)
- [M] Synthesis artifacts concentrate above 6 kHz in one 2024 study; generators may neglect background noise and high frequencies. https://www.arxiv.org/pdf/2402.05567 (2026-11-04)
- [M] High-frequency and fine sub-band features detect synthetic speech best. https://www.isca-archive.org/interspeech_2015/sahidullah15_interspeech.html (2026-11-04)

### Learned quality metrics

| Metric | Licence | Fit | Limit |
|---|---|---|---|
| NISQA-TTS | code MIT, weights CC BY-NC-SA 4.0, ONNX copies inherit it | The only one here made for TTS naturalness | Not commercial. A public plugin should let the user fetch it, not bundle it |
| DNSMOS | DNS-Challenge repo: CC BY 4.0 (LICENSE) plus MIT (LICENSE-CODE). Which covers the models is not stated | Built to judge noise suppressors | Weak fit for TTS; can be gamed |
| SQUIM (torchaudio) | not verified | Estimates PESQ, STOI, SI-SDR, MOS with no reference | 16 kHz only, so blind to HF faults |
| PESQ, ViSQOL, STOI | not checked | Need a reference | TTS has no reference |

- [H] NISQA licences: https://pypi.org/project/nisqa/ and https://huggingface.co/TigreGotico/nisqa-onnx (2026-11-04)
- [H] DNSMOS repo files: https://github.com/microsoft/DNS-Challenge/blob/master/LICENSE (2026-11-04)
- [M] DNSMOS scope: https://arxiv.org/abs/2010.15258v1 (2026-11-04). TTS papers still report it next to NISQA-TTS: https://arxiv.org/pdf/2607.02763 (2026-11-04)
- [M] DNSMOS and SQUIM correlated weakly with listener MOS in CHiME-7 UDASE, as cited by https://arxiv.org/html/2403.11732v2 (2026-11-04)
- [M] Non-intrusive metrics often miss phoneme omissions and speaker inconsistency in TTS data. https://arxiv.org/pdf/2511.13300v1 (2026-11-04; URL attribution inferred from the listing)
- [M] SQUIM: https://docs.pytorch.org/audio/master/tutorials/squim_tutorial.html (2026-11-04)
- [L] Conclusion: use metrics only to compare takes of one voice, never as a pass mark. Keep ASR and speaker checks beside them.

### Speaker embedding models

| Model | ONNX | Size | Licence | EER, VoxCeleb1-O |
|---|---|---|---|---|
| WeSpeaker CAM++ (and _LM) | yes, sherpa-onnx | 27 MB | code Apache-2.0; VoxCeleb models CC BY 4.0 per dataset | 0.654% |
| WeSpeaker ResNet34 (and _LM) | yes | 25 MB | same | not read |
| WeSpeaker ResNet221_LM | yes | 90 MB | same | 0.505% |
| WeSpeaker ECAPA512/1024 | yes per its page | not read | same | 0.728% (variant not read) |
| 3D-Speaker CAM++ en | yes, sherpa-onnx | 28 MB | repo Apache-2.0; each model has its own | not read |
| SpeechBrain ECAPA | not in that release | 79 MB checkpoint | Apache-2.0 | 0.80% |
| NeMo TitaNet small/large | yes | 38 / 96 MB | check the model | not read |
| ReDimNet b0 to b6 | none mentioned | 1 to 15M params | repo MIT; weights not stated | not read |

- [H] Sizes: GitHub API on https://github.com/k2-fsa/sherpa-onnx/releases/tag/speaker-recongition-models (floored to MB; each model has its own licence, 2026-11-04)
- [H] WeSpeaker licence and ONNX: https://github.com/wenet-e2e/wespeaker/blob/master/docs/pretrained.md (2026-11-04). CC BY 4.0 needs attribution.
- [H] ECAPA checkpoint size: https://huggingface.co/speechbrain/spkrec-ecapa-voxceleb (API listing, 2026-11-04)
- [H] ReDimNet: https://github.com/IDRnD/redimnet (2026-11-04)
- [M] EERs: https://arxiv.org/pdf/2306.15161v2.pdf (WeSpeaker). https://arxiv.org/pdf/2303.00332 gives ECAPA 0.89% and CAM++ with 51% fewer parameters and 18% lower EER, so papers differ by recipe. (2026-11-04)
- [L] Pick: WeSpeaker CAM++ ONNX, 27 MB, with attribution. It fits a small package. Check whether CC BY 4.0 on the weights suits you, and fetch at first use.

### Thresholds in the literature: all model-specific

Cosine scores do not carry over between models. Calibrate per model.
- [H] SpeechBrain ECAPA default: verify at 0.25. https://raw.githubusercontent.com/speechbrain/speechbrain/develop/speechbrain/inference/speaker.py (2026-11-04)
- [M] One EER-tuned verifier in a protection paper: 0.697. https://arxiv.org/pdf/2507.02606 (2026-11-04)
- [H] KTH treats 0.6 as "nearby speaker" on its embeddings. https://www.speech.kth.se/~jocke/publications/francis25_ssw.pdf (2026-11-04)
- [M] ReDimNet2+ sample code uses 0.79, an example and not calibrated. https://huggingface.co/lab260/redimnet2-plus (2026-11-04)
- [M] Genuine same-speaker scores are typically 0.6 to 0.8 per one preprint. https://arxiv.org/pdf/2601.02914 (2026-11-04)
- [M] Real same-speaker SIM-o (WavLM) is 0.73 on test-en and 0.75 on test-zh. F5-TTS clones score 0.66 on LibriSpeech-PC, and about 0.67 and 0.76 on Seed-TTS per a secondary page. So clones sit close to real. https://arxiv.org/pdf/2410.06885 and https://arxiv.org/pdf/2606.03455 (2026-11-04; which paper holds the ground-truth row is inferred)

### How clones fool these models

- [H] ECAPA (VoxCeleb), threshold set for 0.01% false accept, 20 minutes of training audio per speaker: Bert-VITS2 bypass 82.7%, similarity 0.679. GPT-SoVITS 56.2%, 0.598. RVC 43.1%, 0.558. A preprint. https://arxiv.org/html/2601.02914v1 (2026-11-04)
- [M] A contrary finding: a Deep Speaker verifier resisted Real-Time Voice Cloning clones that listeners could not tell apart. An old cloner. https://mdpi.com/2079-9292/12/21/4458 (2026-11-04)
- [L] Practical meaning: a high score does not prove a good voice. Use embeddings for three jobs only: same voice across chunks (consistency), distance from stock voices and earlier cast (originality), and match to a reference. Never for quality or "is it human".
- [H] Reference for "different": in KTH, output against the zero-weighted VCTK voice scored about 0.12 +/- 0.11 on ECAPA, and against its own source about 0.52 +/- 0.11. So set consistency bars on takes from that engine. https://www.speech.kth.se/~jocke/publications/francis25_ssw.pdf (2026-11-04)

## 4. What "stereotypical" means

### Evidence

- [M] CHI 2026 (see section 1): no demographics prompted, heard as mostly white, male, US. "Kind" links to white American and British women. "Polite" and "educated" link to white British men. The authors argue no acoustic feature makes a voice inherently professional. https://repository.essex.ac.uk/43154/1/3772363.3798657.pdf (2026-11-04)
- [H] FAccT 2025: 307 survey listeners on stock Speechify and ElevenLabs voices in five accents, each hearing their own accent. Technical performance differs by accent. Interviewees spoke of feeling unrepresented. https://arxiv.org/pdf/2504.09346 (2026-11-04)
- [M] Same paper: listeners heard stock voices mainly as British or American, and African, Indian and Australian labels often mismatched. So a label is not an accent, and the costume can fail for the people it names. Summary from search.
- [M] 85 Americans rated non-native-accented TTS tutors as less competent and helpful. https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2024.1436341/pdf (2026-11-04)
- [L] Listeners told a voice is AI may still judge by accent stereotype. Work in progress. https://www.uni-trier.de/fileadmin/fb2/PHO/IAFPA_2026/WiP/IAFPA2026_WiP_Liu_etal.pdf (2026-11-04)
- [L] Sexualised personas in synthetic voice encode gendered power gaps. 2026 preprint, title only read. https://arxiv.org/pdf/2606.21366 (2026-11-04)
- [L] Humans too: listeners rated older men most competent and young women most trustworthy. Human voices, blog summary. https://blogs.uni-due.de/lifespanchange/?p=440 (2026-11-04)
- Gaps: I found no study naming "accent as costume", the "sweet young woman" stock or the "gravel-voiced man" as such, nor one measuring age range in TTS training data. Those terms are shorthand here, sureness L. Bias work is mostly on gender, as the CHI authors say.

### What moves a voice off the default

- [H] ElevenLabs treats age, tone and gender as the foundation. It offers "gravelly", "airy", "tinny" as timbre words, and says "foreign" or "exotic" give inconsistent results. "Thick" works better than "strong". Pair accent with tone, age or pacing. Quality phrases reduce accuracy for niche voices. https://elevenlabs.io/docs/eleven-creative/voices/voice-design (2026-11-04)
- [L] Voice Design v3 was retrained on broader accent data for rare combinations. Vendor claim. https://elevenlabs.io/blog/voice-design-v3 (2026-11-04)
- [L] Describing how an accent changed over a life gives fewer stereotyped accents. One tutorial. https://growwstacks.com/blog/elevenlabs-ai-voice-generator-text-to-speech-tutorial/ (2026-11-04)
- [H] Google: fix identity in voice design, then keep per-line style short. https://aistudio.google.com/docs/speech-generation (2026-11-04)
- [L] Nobody I found has tested acoustic-traits-only prompts against demographic prompts. The CHI result suggests adjectives alone slide to the default, so traits-only prompts might too. This is a test for voicewright: same brief, both forms, listeners plus embedding distance.
- [L] Proposed casting form, unproven: a specific biography (region, work, life), then measurable traits (pitch range, pace, breathiness, rasp, resonance), then one flaw (short breath, a clipped ending), with no adjective of competence or warmth. Check the result for distance from stock voices.

## Candidate checker defaults (all L until calibrated)

- Hard fails: clipping, wrong words, tail junk, peak above -3 dBFS.
- Warnings: noise floor above -60 dBFS, RMS outside -23 to -18, chunk level jump over 3 dB, HF shelf, room tone change between chunks.
- Consistency: compare each chunk to the voice's reference with one model. Set the bar from that engine's own take-to-take spread (mean minus 2 SD), never a borrowed cosine.
- Originality: score against all stock voices and the project's cast. On ECAPA-scale scores for cloned output, under about 0.3 reads as clearly separate given KTH's 0.12 and 0.32 points; over about 0.5 reads as the same voice.
