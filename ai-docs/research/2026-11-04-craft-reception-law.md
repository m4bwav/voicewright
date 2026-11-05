# voicewright research: craft, reception, law

Date: 2026-11-04. Purpose: ground a public plugin for original, consistent, high-quality AI voices.
Not legal advice. Have a lawyer check anything that ships commercially.

## How to read the tags

Each claim ends with `[sureness, how, date checked] URL`.

- H, M, L: my sureness in the claim.
- READ: I opened the page, through a fetch tool that summarises. Quotes passed through that tool, so check them before reprinting.
- SNIP: search result text only. I did not open the page.
- MEM: from memory. Not checked today.

## Limits of this pass

- Blocked or unreadable today: congress.gov, GovTrack, sagaftra.org, Backstage, Audiokinetic blog, Justia, Netflix partner pages, GameSpot. Claims that needed them rest on secondary sources.
- I did not read the bill text of NO FAKES, the SAG-AFTRA contract, the final EU guidelines or the Code. The Lovo opinion PDF was fetched but not extracted, so its holdings come from Skadden's summary.
- Reddit: the one permitted snippet search returned no Reddit threads. So player reaction here comes from press. Arctic Shift and Gemini grounding were not used.
- Search found no primary studio document on voice bibles. The craft section is weakest there.

---

## 1. How voice work is done

### Casting and direction

- A voice director works from two scripts. The actor's script is minimal: scene setup, feed line, brief inflection cues. [H, READ, 2026-11-04] https://www.gamedeveloper.com/audio/insights-into-audio-recording-from-two-voice-directors
- The director's script adds feed lines, character position (distance, elevation), private pickup notes, numbered selects, false-start notes, and each line's filename. [H, READ, 2026-11-04] same URL
- Cinematics use screenplay format. Branching dialogue and barks use modular spreadsheets. [H, READ, 2026-11-04] same URL
- A casting breakdown covers age range, vocal texture, personality, emotional extremes and technical demands. Low-authority source, but it matches trade practice. [M, SNIP, 2026-11-04] https://app.studyraid.com/en/read/99669/4471880/voice-acting-direction-and-syncing
- ACX tells authors to share a vision as inspiration, not to ask for imitations of other characters or performers. [H, READ, 2026-11-04] https://www.acx.com/mp/blog/directors-notes-for-your-acx-production

### Pronunciation and audiobook prep (ACX)

- List unfamiliar, ambiguous and non-standard names and places. Include the author's name phonetically. Invented names and languages need guidance because the narrator cannot look them up. Sci-fi, fantasy and LitRPG need a bigger guide. [H, READ, 2026-11-04] https://www.acx.com/mp/blog/directors-notes-for-your-acx-production
- Character chart: name, accent, origin, relationships, motivation, backstory, self-image versus how others see them, how they sound. [H, READ, 2026-11-04] same URL
- Flag heavy or funny moments where the text alone may not show it. Give foreshadowing the narrator must know and the listener must not. Agree a 15-minute checkpoint before the full run. [H, READ, 2026-11-04] same URL
- Keep the pronunciation guide after the book, so later titles in a series match. Vendor and author blogs. [M, SNIP, 2026-11-04] https://narrationbox.com/blog/pronunciation-consistency-harder-than-voice-quality-audiobook-guide

### Pickups

- Pickups are routine. Lines get missed, scripts change, QA flags issues. Schedule and budget for them. The page body did not load through the fetch tool. [M, SNIP, 2026-11-04] https://side.inc/lab/demystifying-game-vo-directing-recording-postproduction
- Directors keep private pickup notes such as "the acting was weak in this middle section". [H, READ, 2026-11-04] https://www.gamedeveloper.com/audio/insights-into-audio-recording-from-two-voice-directors

### Keeping a character consistent over years

- A "living bible" holding vocal references, emotional baseline, accent rules, forbidden reads and relationship notes is recommended by a training site. I found no studio primary source. Its "40% less direction time" figure is unverified; do not reuse it. [L, SNIP, 2026-11-04] https://app.studyraid.com/en/read/99669/4471880/voice-acting-direction-and-syncing
- Recasts can force old lines to be redone. Bungie re-recorded Ghost's old Destiny lines with Nolan North for The Taken King (2015). A critic heard the cadence echoed but not a full match. [M, SNIP, 2026-11-04] https://gamesbeat.com/?p=105030
- Cyberpunk 2077: Phantom Liberty (2023). A new actor performed lines in the late Polish actor's style, then an algorithm built with the family's permission adjusted the audio. This is performance first, conversion second, with consent. [H, SNIP, 2026-11-04] https://pcgamer.com/cyberpunk-2077-phantom-liberty-used-ai-to-reproduce-late-polish-voice-actors-performance-as-viktor-vektor-with-the-familys-blessing
- My inference, not a sourced fact: the working toolkit is a voice sheet, a locked set of reference clips, a pronunciation table, and a per-line session log (take, settings, select, reason). AI needs extra pins that a person does not: model version, seed, and settings. Model updates can change a voice the way a recast does.

### Loudness targets by destination

BS.1770 loudness (LUFS, LKFS) and ACX RMS are different measures. Do not convert one to the other by assumption.

| Destination | Target | True peak | Sureness and source |
|---|---|---|---|
| Audiobook (ACX) | -23 to -18 dB RMS per file | Peaks below -3 dB; noise floor no higher than -60 dB RMS | H, READ, 2026-11-04, https://help.acx.com/s/article/what-are-the-acx-audio-submission-requirements |
| Narration, podcast (Apple) | -16 dB LKFS, +/-1 dB | At or below -1 dB FS, BS.1770-5 | H, READ, 2026-11-04, https://podcasters.apple.com/support/audio-requirements |
| Film, streaming (Netflix) | -27 LKFS dialogue-gated | -2 dBTP | M, SNIP, 2026-11-04. Tolerance conflicts between sources, +/-2 LU or +/-0.5 LU. Primary page did not render. https://www.forasoft.com/learn/audio-for-video/articles-audio/lufs-targets-per-platform-2026 |
| Broadcast, Europe (EBU R128) | -23 LUFS, +/-0.5 LU | -1 dBTP | M, SNIP, 2026-11-04, same URL |
| Broadcast, US (ATSC A/85) | -24 LKFS | -2 dBTP | M, SNIP, 2026-11-04, same URL |
| Game, console | -24 LUFS, +/-2 LU, 30-minute minimum capture | -1 dBTP | M, SNIP, 2026-11-04. Audiokinetic citing PlayStation guidance as of Feb 2024. Whole-game mix, not a per-line target. https://audiokinetic.com/en/mastering-a-game-with-wwise-part1 |
| Game, mobile, portable | -18 LUFS, +/-2 LU | -1 dBTP | M, SNIP, 2026-11-04, same URL |
| YouTube | Often quoted as -14 LUFS | | L. No official page found today. Do not enforce. |

ACX other numbers. [H, READ, 2026-11-04] https://help.acx.com/s/article/what-are-the-acx-audio-submission-requirements

- 44.1 kHz MP3, 192 kbps or higher, constant bit rate.
- Room tone 1 to 5 seconds at start and end of each file, never above 5.
- Each file no longer than 120 minutes.
- Opening and closing credits required. Retail sample 5 minutes or less.
- "Your submitted audiobook must be narrated by a human unless otherwise authorized." Unauthorized TTS and AI recordings are prohibited.

My inference: a skill cannot set a per-line "game dialogue" number from these sources. Game targets apply to the mix. Keep lines internally matched and leave the final level to the mix.

---

## 2. What pros and listeners hate

### Tells of AI voice

- Reduced pitch variation (F0) lowered naturalness and similarity ratings. ElevenLabs clones rated about as high as human speech; StyleTTS-2 and XTTS-v2 lower. Prior AI experience did not change ratings. Bakkouche et al., Interspeech 2025. [H, READ, 2026-11-04] https://www.isca-archive.org/interspeech_2025/bakkouche25_interspeech.html
- Players call Arc Raiders traders and quest NPCs "robotic", "monotone", "soulless". Complaints name flat, repeated, context-free quips. Blog-level source. [M, SNIP, 2026-11-04] https://allthings.how/arc-raiders-and-ai-voices-what-players-are-hearing
- The Finals drew a specific objection: AI dialogue beside human or in-house exertion sounds felt inconsistent. [M, SNIP, 2026-11-04] https://www.pcgamesn.com/the-finals/ai-voice-acting
- I found no study isolating breaths as a cue. Do not present "add breaths" as proven. [M, search result, 2026-11-04]
- Blind tests can favour AI. A Spoken-funded Edison survey of 1,005 fiction audiobook fans: 61% favourable for an AI multi-cast version versus 53% for a human narrator, and 61% of those exposed took AI for human. Vendor-funded. [L, SNIP, 2026-11-04] https://rainnews.com/?p=57345
- Takeaway: the anger is often about knowing it is AI and about labour, not only about sound. Quality alone will not remove it. This is my reading.

### Store rules

- Steam, re-read today. Pre-generated AI content that ships and is consumed by players must be disclosed, and is reviewed like non-AI content. Covers artwork, sound, narrative, localization. Efficiency tools are not the focus. [H, READ, 2026-11-04] https://partner.steamgames.com/doc/gettingstarted/contentsurvey
- Steam live-generated AI: you must also tell Valve the guardrails against illegal content. Live-generated adult-only sexual content is not allowed. [H, READ, 2026-11-04] same URL
- Steam, January 2026 form change: "AI powered tools" need no disclosure. "AI to generate content for the game" and "AI content generated during gameplay" do. A text box describes the use. Marketing and store page assets count. [H, READ, 2026-11-04] https://www.gamedeveloper.com/business/valve-tweaks-and-clarifies-ai-disclosure-rules-for-steam
- Voice is not named on the Steam page. "Sound" is. Voice as sound is my reading. [M, 2026-11-04]
- Open question: TTS used only as a placeholder and removed before ship looks like a workflow tool. That is my inference from the wording, not a Valve statement. If any remains in the build, disclose. [M, 2026-11-04]
- ACX: human narration unless authorized (see above). Audible's Virtual Voice runs through KDP and is labelled "Narrated By: Virtual Voice". [H, READ, 2026-11-04] https://techcrunch.com/2025/05/13/audible-is-expanding-its-ai-narrated-audiobook-library/

### Real cases, with dates

| Date | Case | What happened | Sureness and source |
|---|---|---|---|
| 2023-09 | Cyberpunk 2077: Phantom Liberty | Late actor's voice recreated with family consent. Coverage mostly accepting: the positive model. | H, SNIP, 2026-11-04, https://pcgamer.com/cyberpunk-2077-phantom-liberty-used-ai-to-reproduce-late-polish-voice-actors-performance-as-viktor-vektor-with-the-familys-blessing |
| 2023-10 to 11 | The Finals | Developer podcast said contestant barks and commentators were AI. Voice actor Gianni Matragrano shared the clip. Embark then said it used a mix of recordings and TTS and that games without actors were not the goal. | H, SNIP, 2026-11-04, https://www.axios.com/2023/10/31/the-finals-embark-ai-voice and https://www.neowin.net/news/embark-backtracks-somewhat-on-its-claims-of-ai-voice-actor-use-for-the-finals/ |
| 2024-05 onward | Audible Virtual Voice | Over 40,000 titles reported in May 2024, over 50,000 by May 2025. Publisher expansion announced 2025-05-13. Narrators fear job loss; critics fear quality loss. One report says listeners cannot filter them out on the site. | M, READ and SNIP, 2026-11-04, https://techcrunch.com/2025/05/13/audible-is-expanding-its-ai-narrated-audiobook-library/ and https://www.techspot.com/news/102875-40000-ai-narrated-audiobooks-flood-audible-dividing-authors.html |
| 2025-05 | Fortnite AI Darth Vader | James Earl Jones replica, estate-approved. SAG-AFTRA still filed an unfair labor practice charge against Llama Productions (Epic), over not bargaining. Lesson: estate consent does not end union exposure. | H, SNIP, 2026-11-04, https://www.pcgamer.com/games/battle-royale/sag-aftra-files-unfair-labor-practice-complaint-against-epic-over-fortnites-ai-powered-darth-vader-we-must-protect-our-right-to-bargain-terms-and-conditions-around-uses-of-voice-that-replace-the-work-of-our-members |
| 2025-08 to 09 | Tomb Raider IV-VI Remastered | Patch 2 (2025-08-14) allegedly added AI versions of Francoise Cadol's French Lara and the Brazilian voice of Lene Bastos. Cadol sent legal notice. A hotfix reportedly removed the vocals. Aspyr told Bastos a partner added it. Outcome not found. Lesson: vendors and localization need the same check. | M, SNIP, 2026-11-04, https://www.engadget.com/gaming/remastered-tomb-raider-games-allegedly-used-ai-to-change-lara-crofts-french-voice-183922036.html and https://www.timeextension.com/news/2025/09/tomb-raider-voice-actor-takes-legal-action-over-alleged-ai-generated-vocals |
| 2025-09 to 10 | Tilly Norwood | SAG-AFTRA: a computer character "trained on performers' work without permission", and contracts require notice and bargaining. Shows a wholly designed performer still draws attack. Image and persona, not voice first. | H, SNIP, 2026-11-04, https://techcrunch.com/2025/10/01/hollywood-is-not-taking-kindly-to-the-ai-generated-actress-tilly-norwood |
| 2025-11-10 | Arc Raiders review | Eurogamer 2/5, naming AI voices. Sales stayed strong: over four million in the first month reported. Lesson: loud reputational cost, little visible sales cost for a hit. An indie may differ; I found no indie data. | M, SNIP, 2026-11-04, https://80.lv/articles/eurogamer-s-2-5-arc-raiders-review-splits-the-gaming-community/ and https://wccftech.com/amidst-arc-raiders-success-embarks-use-of-gen-ai-voices-bubbles-over-even-epics-ceo-joins-the-fray/ |
| 2026-03-14 | Arc Raiders reversal | CEO Soderlund: "A real professional actor is better than AI; that's just how it is." Some lines re-recorded. Keeps TTS as a way to "test 15 different lines" first. Actors paid for TTS licensing. | H, READ, 2026-11-04, https://www.pcgamesn.com/arc-raiders/ai-voices-replaced |
| 2026-11-02 | Arc Raiders, all quest lines | Report that all quest lines were re-recorded. Unnamed source, marked unverified by the outlet itself. | L, READ, 2026-11-04, https://gameriv.com/arc-raiders-reportedly-re-records-all-quest-lines-with-real-voice-actors-following-ai-backlash/ |

---

## 3. Law and consent

Summary: **a voice built from a named or identifiable person is the danger zone. A designed voice is not safe by default. Most of the rest is unsettled.**

### Licences of output

- ElevenLabs terms updated 2026-10-09. You retain rights in output. Paid plans may use it commercially; free plans may not. Output may not be unique. You license content to them to improve services, with a training opt-out. A voice model must be your voice or one you may share. [H, READ, 2026-11-04] https://elevenlabs.io/terms-of-use
- Consequence of "may not be unique": a stock or designed voice gives you no exclusive claim. Two products may sound alike. This is my reading. [M, 2026-11-04]
- Voice Library use has a separate addendum I did not read. Library voices may carry creator terms; iconic marketplace voices need rights-holder approval. [M, SNIP, 2026-11-04] https://elevenlabs.io/voice-guide and https://the-decoder.com/elevenlabs-opens-a-marketplace-for-iconic-ai-voices/
- Open-weight model licences and their training sets were not covered in this pass. Another research pass must check each model's weights licence, output terms and data consent. [gap]

### Can you own a designed voice? Is it original?

- Copyright protects recordings, not the abstract qualities of a voice. Imitating recordings are not infringing derivatives. Lehrman v. Lovo, S.D.N.Y., July 2025. [H, READ, 2026-11-04] https://www.skadden.com/insights/publications/2025/07/new-york-court-tackles-the-legality-of-ai-voice-cloning
- US Copyright Office Part 1 (July 2024) says copyright does not protect voice or likeness as such. Part 2 (2025-01-29): prompts alone do not make authorship; human selection, arrangement or editing can be protected. [H, SNIP, 2026-11-04] https://ipwatchdog.com/2025/01/29/part-two-copyright-office-ai-report-says-creative-prompting-doesnt-constitute-authorship/
- So nobody can claim a clean "our voice" copyright. Protect the character, script, and edited work instead. My inference. **UNSETTLED** for sound recordings specifically; the sources do not address them. [M, 2026-11-04]
- Sound-alike risk exists without any training on that person. Midler v. Ford (9th Cir. 1988) and Waits v. Frito-Lay (9th Cir. 1992) found liability for deliberately imitating a distinctive voice in advertising. Not re-read today. [M, MEM, 2026-11-04]
- ELVIS Act "voice" covers a sound "readily identifiable and attributable to a particular individual", actual or simulated. [H, SNIP, 2026-11-04] https://chatgptiseatingtheworld.com/2024/03/22/elvis-act-text-pdf-tennessee-passes-law-to-stop-ai-deepfakes-of-voice-in-addition-to-name-photograph-likeness/
- California's test is "readily identifiable as the voice or visual likeness of an individual". [H, READ, 2026-11-04] https://www.fenwick.com/insights/publications/californias-new-ai-laws-limit-uses-of-digital-likeness
- **UNSETTLED**: whether a designed voice that happens to resemble someone infringes without intent. Whether a voice blended from several people infringes any of them. Intent matters in the older cases, but statutes turn on identifiability. No case on either found.
- Practical test (my proposal): never prompt by person name; compare against a blocklist by ear and by speaker embedding where possible, knowing no threshold has legal standing.

### Training data suits

- Lovo: training claim dismissed with leave to amend. NY Civil Rights §§ 50-51, consumer protection and contract claims survived. Ongoing model output could count as ongoing replication for limitations. [H, READ, 2026-11-04] Skadden URL above
- Lovo filed Chapter 7 on 2026-05-27, and the case was stayed. So no merits ruling is coming soon from it. [M, SNIP, 2026-11-04] https://news.bloomberglaw.com/ip-law/voice-actors-suit-against-lovo-paused-amid-ai-firms-bankruptcy
- Vacker v. ElevenLabs settled after mediation; terms not found. [M, SNIP, 2026-11-04] https://chatgptiseatingtheworld.com/category/vacker-v-eleven-labs/
- BIPA class action against ElevenLabs, filed 2026-05-12 in Illinois: voiceprints of journalists and voice actors collected to train without written consent. The same group filed nine suits against firms including Amazon, Adobe, Google, Apple, Microsoft, Meta and NVIDIA. Pending. [M, SNIP, 2026-11-04] https://sifted.eu/articles/elevenlabs-lawsuit-2026 and https://fox2now.com/news/illinois-journalists-podcasters-sue-tech-companies-over-using-their-voice-to-train-ai/
- **UNSETTLED**: whether voice model training is lawful without consent under copyright or biometric law. "Original" outputs may rest on disputed data.

### US state laws

- **Tennessee ELVIS Act**: signed 2024-03-21. Effective 2024-07-01 in most sources; one says 07-21. Adds voice. Reaches public distribution with knowledge of no authorization, and tools whose primary purpose is producing a person's likeness or voice without authorization. [M on date, H on content, SNIP, 2026-11-04] https://www.hklaw.com/en/insights/publications/2024/04/first-of-its-kind-ai-law-addresses-deep-fakes-and-voice-clones
- **California AB 2602** (Labor Code 927): a contract term is against public policy if it lets a replica replace in-person work, lacks a reasonably specific list of uses, and the person lacked counsel or a union. New performances from 2025-01-01. [H, READ, 2026-11-04] https://www.fenwick.com/insights/publications/californias-new-ai-laws-limit-uses-of-digital-likeness
- **California AB 1836** (Civil Code 3344.1): consent needed for a deceased person's replica in an audiovisual work or sound recording. Greater of $10,000 or actual damages. Exceptions: news, comment, satire, fleeting uses. Effective 2025-01-01. [H, READ and SNIP, 2026-11-04] same URL and https://www.cozen.com/news-resources/publications/2024/new-california-ai-laws-protect-against-unauthorized-use-of-ai-replicas
- **New York S.8420-A**: signed 2025-12-11, effective 2026-06-09. Ads must conspicuously disclose a synthetic performer. **Audio ads are exempt.** So are ads for expressive works including games, when use matches the work. $1,000 first violation, $5,000 after. [H, READ, 2026-11-04] https://www.nysenate.gov/legislation/bills/2025/S8420/amendment/A and https://www.cooley.com/news/insight/2026/2026-01-29-new-york-enacts-synthetic-performer-disclosure-law-for-advertisements-including-those-using-generative-ai
- **New York S.8391**: post-mortem replica consent, amends Civil Rights Law 50-f. Sources differ on scope. [M, SNIP, 2026-11-04] https://www.sagaftra.org/gov-hochul-signs-union-backed-ai-bills-sag-aftra-new-york-office
- **Illinois HB 4875**: voice and likeness replicas, effective 2025-01-01. HB 4762 covers contracts. HB 3178 voids some service terms for new replica performances from 2026-01-01. [M, SNIP, 2026-11-04] https://ipwatchdog.com/2024/08/15/illinois-becomes-second-state-ban-unauthorized-digital-replicas-created-generative-ai/
- Federal executive order sets an AI Litigation Task Force against some state AI laws. I found no suit against a replica law. **UNSETTLED.** [M, SNIP, 2026-11-04] https://www.axios.com/local/chicago/2025/06/10/ai-laws-ban-budget-bill-senate-house (context only; order text not read)
- Other states not checked in this pass.

### NO FAKES Act, as of today

**Not law.**

- S. 4591 and H.R. 8915 introduced 2026-05-20. [H, READ, 2026-11-04] https://www.manatt.com/insights/newsletters/client-alert/congress-reintroduces-the-no-fakes-act-what-s-new-in-the-2026-bill
- Senate Judiciary advanced it by unanimous voice vote on 2026-06-18. One law blog says June 22; the others say June 18. [H, READ, 2026-11-04] https://www.hklaw.com/en/insights/publications/2026/06/senate-judiciary-committee-advances-legislation-to-protect-name
- On 2026-09-30 Sen. Blackburn asked unanimous consent. Sen. Cruz objected, citing unclear satire exceptions. Reports date it Sept 30 or Oct 1. [H, SNIP and READ, 2026-11-04] https://www.dailyjournal.com/article/395055-no-fakes-act-dead-for-now-as-cruz-objects-to-unanimous-consent-request and https://www.rawstory.com/ted-cruz-marsha-blackburn/
- No House markup found. No action found after early October. congress.gov was blocked, so re-check before relying on this. [M, 2026-11-04]
- The 119th Congress ends 2027-01-03. A new bill would be needed after that. [H, SNIP, 2026-11-04]
- If passed: licensable right for every person, reach to platforms and to some products and services, $5,000 to $25,000 statutory damages per violative replica, future state laws preempted. [M, READ, 2026-11-04] https://www.bytebacklaw.com/2026/08/a-federal-shift-in-ai-and-the-right-of-publicity-no-fakes-act-advances-in-congress/

### EU AI Act Article 50

- Applies since 2026-08-02. Omnibus (Regulation 2026/1744) gave only providers with systems already on the market until 2026-12-02 for machine-readable marking. Fine up to 15 million euros or 3% of turnover. [H, READ, 2026-11-04] https://www.goodwinlaw.com/en/insights/publications/2026/08/alerts-technology-dpc-eu-ai-act-transparency-obligations-now-in-force
- 50(2): providers mark synthetic audio machine-readably, as far as technically feasible. [H, READ, 2026-11-04] https://artificialintelligenceact.eu/article/50/
- 50(4): deployers disclose deepfake audio. For evidently artistic, creative, satirical or fictional works the duty narrows to disclosing it exists, without hampering the work. [H, READ, 2026-11-04] same URL
- 50(5): at the latest at first exposure, clear and accessible. [H, READ, 2026-11-04] same URL
- 50(1) chatbot-style live NPCs: telling people they are interacting with AI may apply. Paragraph not read today. [M, MEM, 2026-11-04]
- Commission adopted guidelines 2026-07-20. I read only commentary. [H on date, READ, 2026-11-04] Goodwin URL
- Draft guidelines: intent is irrelevant; a realistic fictitious person can be a deepfake; obvious fantasy (dragon, talking animal) falls outside. One commentator says a fully synthetic voice with no likeness to the character's identity is not a deepfake, while another reading is that a voice that "sounds like a real person" can qualify. Draft text; confirm against final. **UNSETTLED for a realistic designed human voice.** [M, READ and SNIP, 2026-11-04] https://natlawreview.com/article/deepfakes-chatbots-ai-generated-text-european-commission-details-transparency
- Code of Practice on marking and labelling: final, voluntary, published 2026-06-10. [H, SNIP, 2026-11-04] https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content

### Unions

- SAG-AFTRA 2025 Interactive Media Agreement approved about 95%, ending the strike. [H, SNIP, 2026-11-04] https://graphicpolicy.com/2025/07/10/sag-aftra-members-approve-the-2025-video-game-agreement/
- Consent must be clear, conspicuous, in writing, separate or a signed rider, with a reasonably specific use description. Generally not obtainable at hire for future games. Must say if sensitive content is involved. [H, READ, 2026-11-04] https://technologylaw.fkks.com/post/102mewu/inside-the-new-sag-aftra-interactive-media-agreement-new-standards-for-ai-and-di
- Vocal replica pay is per lines generated, a line being about ten words. Usage report within 90 days of release. Real-time uses must be specifically described. [H, READ, 2026-11-04] same URL
- ICDRs (replicas from non-union material or by prompting a name) still generally need consent and bargaining. [H, READ, 2026-11-04] same URL. Term stated as to October 2028 by one summary; check it. [L, SNIP]
- Synthetic performers require notice and bargaining, per the union's public statement. [M, SNIP, 2026-11-04] https://www.foxbusiness.com/media/sag-aftra-condemns-ai-synthetic-performers-after-artificial-actress-goes-viral
- Equity UK, ACTRA, and the French #TouchePasMaVF campaign: only the French campaign surfaced, in Tomb Raider coverage. Others not covered. [gap]
- If the user is not a union signatory, these do not bind them directly. The terms remain a good standard to copy. My reading.

### FTC and FCC

- FTC final rule covers impersonation of government and businesses. Extension to individuals and to tool providers with knowledge was proposed 2024-03-01. **Status in 2026 not found.** [M, SNIP, 2026-11-04] https://www.jdsupra.com/legalnews/ftc-issues-supplemental-rulemaking-to-4025204/
- FTC staff say existing law reaches voice cloning harm. [M, SNIP, 2026-11-04] https://ftc.gov/policy/advocacy-research/tech-at-ftc/2023/11/preventing-harms-ai-enabled-voice-cloning
- FCC, 2024-02-08: AI voices are "artificial" under the TCPA, so robocalls with them need consent. [H, SNIP, 2026-11-04] https://www.akingump.com/en/insights/ai-law-and-regulation-tracker/fcc-issues-declaratory-ruling-on-ai-generated-voice-robocalls
- My inference: false claims such as "human narrated" or "no AI" create deception exposure. Say only what is true.

### What is unsettled, in one list

1. Whether designed or blended voices can infringe by accidental resemblance.
2. Whether training on voices without consent is lawful (copyright, BIPA).
3. Copyright in purely AI-generated speech recordings.
4. Whether a realistic designed human voice in fiction is an Article 50 deepfake, and what label satisfies it.
5. Fate of NO FAKES, and federal pressure on state laws.
6. FTC individual impersonation rule.

---

## 4. Book and literature leads

Titles only. Marked V if search confirmed the title exists today, otherwise from memory: check before citing.

**Voice acting and direction**
- James Alburger, The Art of Voice Acting, 7th ed. (V, Routledge) https://www.routledge.com/The-Art-of-Voice-Acting-The-Craft-and-Business-of-Performing-for-Voiceover/Alburger/p/book/9781032370682
- Yuri Lowenthal and Tara Platt, Voice-Over Voice Actor (V) https://www.bugbotpress.com/news/2021/7/24/voice-over-voice-actor-the-extended-edition-is-an-amazon-best-seller
- Judith Weston, Directing Actors
- Hester Schell, Casting Revealed
- Backstage list of voice acting books, unread (403): https://www.backstage.com/magazine/article/voice-acting-books-list-75018/

**Actor's voice and accents**
- Kristin Linklater, Freeing the Natural Voice (V)
- Cicely Berry, Voice and the Actor (V)
- Patsy Rodenburg, The Actor Speaks (V)
- Robert Blumenfeld, Accents: A Manual for Actors

**Speech science**
- Jody Kreiman and Diana Sidtis, Foundations of Voice Studies
- John Laver, The Phonetic Description of Voice Quality
- Ingo Titze, Principles of Voice Production
- Gunnar Fant, Acoustic Theory of Speech Production
- Kenneth Stevens, Acoustic Phonetics
- Peter Ladefoged, A Course in Phonetics
- John Wells, Accents of English
- Clifford Nass and Scott Brave, Wired for Speech
- Paul Taylor, Text-to-Speech Synthesis

**Papers**
- Bakkouche et al., Interspeech 2025, doi 10.21437/Interspeech.2025-947 (V)

**Game audio**
- Gina Zdanowicz and Spencer Bambrick, The Game Audio Strategy Guide

---

## 5. Rules proposed for the skill

These are my recommendations from the above, not legal requirements.

1. Refuse to clone or imitate an identifiable person without a written consent record naming uses.
2. Refuse prompts by real person or character-actor name, including "sounds like X".
3. Record voice provenance per voice: model, version, licence, plan, seed, settings, source clips, date. No record, no ship.
4. Check a resemblance list before locking a voice. Say that no check gives legal clearance.
5. Keep one voice sheet per character: casting brief, emotional range, forbidden reads, locked reference clips.
6. Keep one pronunciation table per project, and reuse it across a series.
7. Keep a session log per line: take, select, reason. Pickups must match against reference clips.
8. Pin the model. Re-test references before any model update, and treat a change as a recast.
9. Direct with scene context, feed line and intent, not adjectives only.
10. Fail flat reads: check pitch variation, and listen to repeated barks in a row.
11. Master to destination. Enforce the table above, and refuse an unknown target.
12. ACX: block upload advice unless the user has authorization; AI narration is prohibited there otherwise.
13. Steam: draft the disclosure text whenever AI voice ships or appears in marketing. Add guardrails for live generation.
14. EU: add the Article 50 note, and an unobtrusive credit line for fiction.
15. Say truthfully what is AI. Never write "no AI" or a human narrator credit unless true.
16. Check vendors and localization partners for the same rules, as in the Tomb Raider case.
17. Warn that union status changes obligations, and suggest the IMA terms as a standard.
18. Offer the temp-track route: AI first to test lines, humans for hero lines. Arc Raiders ended up here.
19. Stamp the legal notes with a check date. Re-check NO FAKES at each use.

## 6. Next research passes

- Read NO FAKES bill text at congress.gov from a browser, for its definition and tool liability.
- Read the final Article 50 guidelines for voice and fiction.
- Read the IMA contract text on sagaftra.org.
- Open-weight model licences and training data.
- Studio primary sources on voice bibles (GDC talks, game audio conference notes).
- Indie sales impact of AI voice disclosure.
- Equity UK, ACTRA, NAVA; other state laws.
