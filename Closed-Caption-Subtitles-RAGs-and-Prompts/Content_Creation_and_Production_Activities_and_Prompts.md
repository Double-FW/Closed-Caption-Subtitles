# Closed Caption Subtitles: human-managed content creation and production activities and prompts

**Prepared:** 8 November 2026 · **Source revision:** `46cc2bee18bc49212788cb5f67e84c7387567dd2`  
**Source:** [Double-FW/Closed-Caption-Subtitles](https://github.com/Double-FW/Closed-Caption-Subtitles/tree/46cc2bee18bc49212788cb5f67e84c7387567dd2)  
**Audience:** authors, editors, designers, publishers, communication teams, producers, commissioners, access-service practitioners and technical/quality partners.

## Where the repository is useful

Use this repository to plan and produce synchronised, user-selectable Closed Caption Subtitles that preserve dialogue, speaker meaning, important sound and editorial treatment. CCS 001–033 connect commissioning, fidelity, structure, timing, sound, presentation, live work, formats and rendering. The QA and AI-governance sections support controlled production and review.

MUST/SHOULD/MAY describe conformance to this repository guideline within scope, not automatic legal or platform applicability. Reading rates, line limits, speaker styles, live latency and delivery choices need audience/language/service profiles; legacy or broadcaster defaults must not silently become universal. ASR output, dialogue-only subtitles, translations and transcripts are not interchangeable with complete CCS. File syntax, presentation, player access and audience outcomes require different evidence.

The activities below are an editorial application of the repository, not a claim that it already contains a complete organisational process. AI can organise material, draft options and scripts, identify inconsistencies and prepare specifications or evidence summaries. Authors and editors preserve factual meaning and editorial intent. Designers and technical practitioners implement and verify delivered formats. Qualified access-service specialists review their work, and affected audiences inform the experience. Accountable publishers/producers retain creative, acceptance, rights and release decisions. Assign these responsibilities to actual people locally; the examples do not establish a new team or approval body.

## How to use the prompts

1. Attach [RAG_Reference.md](RAG_Reference.md). For selective retrieval, use the source routes below and [Source_Coverage.md](Source_Coverage.md).
2. Replace bracketed inputs with the actual project brief, artefacts and evidence. Supply the target task, audience, platform/setting, constraints and intended decision. Treat missing information as unknown.
3. Use either example prompt for the activity. Both refer to this folder’s reference. Supply only appropriate project information; use anonymised research findings where possible.
4. Require source ID, filename and original section citations; distinguish source guidance, local proposal, observed result and uncertainty. Ask for evidence requests where an artefact cannot be inspected.
5. Review the result with the named human roles and record decisions. A prompt output is a draft editorial/production aid, not implementation or evidence that a test ran. Do not defer disabled people’s involvement until final testing.

**Reusable response contract:** “Use the attached RAG_Reference.md as the knowledge source. Cite source IDs, files and sections. Distinguish source statements, project evidence, recommendations and unknowns. Preserve applicable source identifiers. Do not invent research, capability, approvals or test results. Give a concrete content/production artefact, trade-offs, evidence requests and decisions for the human team.”

## Activity map

| Activity | Production stage | Expected output |
| --- | --- | --- |
| 1. Define the caption service and production profile | Commissioning and caption brief | A caption commissioning brief and profile register. |
| 2. Preserve speech fidelity and editorial treatment | Transcription and caption editing | An editorially checked draft and change/uncertainty log. |
| 3. Represent speakers, sound, music and vocal meaning | Caption editorial production | A speaker/sound convention sheet and cue-review plan. |
| 4. Author linguistic structure and meaningful timing | Caption segmentation and timing | A segmentation/timing profile and cue-level revision brief. |
| 5. Design readable positioning and adaptable presentation | Visual presentation and platform review | A presentation/positioning specification and device-check brief. |
| 6. Plan live captions and on-demand correction | Live production and catch-up management | A live-caption operating/rehearsal brief and catch-up plan. |
| 7. Choose formats and preserve meaning through transformations | Timed-text delivery and engineering handoff | A timed-text delivery profile and transformation test plan. |
| 8. Verify accessible caption controls and published playback | Player integration and publication QA | A scoped player/playback evaluation plan. |
| 9. Bound automation and retain editorial accountability | AI-assisted caption production | An AI-assisted workflow brief and review/decision record. |
| 10. Evaluate, accept and maintain caption quality | Quality assurance, release and change control | A caption acceptance/release draft and change/retest register. |

## 1. Define the caption service and production profile

**Production stage:** Commissioning and caption brief

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** Sections 1–3 and 11; CCS 031.

### Tasks the repository can support

- Define content, languages, audiences and live/prerecorded routes.
- Select contextual authoring/presentation/delivery profiles.
- Assign source materials, reviewers and unresolved decisions.

**Expected output:** A caption commissioning brief and profile register.

**Human review:** The producer and caption lead agree scope; distributors confirm actual current requirements.

### Example prompt 1

> Use the attached RAG to commission CCS for [production and destinations]. Define languages, audience/genre, live/prerecorded status, exact cut, source audio/materials and delivery chain. Propose authoring, timing and presentation profiles, marking current platform specifications and authority to confirm. Do not assume dialogue-only or automatic text is complete CCS.

### Example prompt 2

> Challenge [caption commissioning brief] with the RAG. Find language subtitles confused with CCS, fixed legacy limits applied everywhere and missing exact audio/picture versions. Produce a corrected scope and open decisions.

## 2. Preserve speech fidelity and editorial treatment

**Production stage:** Transcription and caption editing

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** CCS 001–006; CCS 022–023.

### Tasks the repository can support

- Represent meaningful speech faithfully and edit only for a documented reason.
- Verify names, numbers, negation and terminology.
- Retain source treatment of strong language, dialect and uncertainty.

**Expected output:** An editorially checked draft and change/uncertainty log.

**Human review:** A human caption editor compares the actual delivered soundtrack and approved references.

### Example prompt 1

> Using the RAG, review [caption draft and supplied source audio/transcript evidence] under CCS 001–006 and 022–023. Preserve wording, character, editorial treatment and meaning; verify supplied names/terms/numbers and mark uncertain words. Do not invent inaudible speech, sanitise language or simplify because viewers are Deaf.

### Example prompt 2

> Challenge [caption editing rationale] against the RAG. Identify unapproved paraphrase, translation inserted into a same-language track and meaningful hesitation or negation removed. Propose specific revisions and evidence checks without claiming unheard audio was verified.

## 3. Represent speakers, sound, music and vocal meaning

**Production stage:** Caption editorial production

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** CCS 016–023.

### Tasks the repository can support

- Identify ambiguous speakers without guessing identity.
- Preserve meaningful effects, music, lyrics and speech characteristics.
- Use redundant cues rather than colour-only identification.

**Expected output:** A speaker/sound convention sheet and cue-review plan.

**Human review:** Caption and editorial leads verify actual audio/visual evidence and appropriate conventions.

### Example prompt 1

> Use the RAG to specify speaker and sound treatment for [content and supplied evidence]. Apply CCS 016–023 to ambiguous/off-screen speakers, meaningful effects, music, lyrics and vocal characteristics. Use verified identifiers and more than colour alone; mark uncertain sounds for review rather than inventing labels.

### Example prompt 2

> Review [caption track excerpts] using the RAG. Identify missing sound-led story information, guessed speakers, lyric omissions and colour-only meaning. Propose consistent, proportionate labels that preserve the experience without needless clutter.

## 4. Author linguistic structure and meaningful timing

**Production stage:** Caption segmentation and timing

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** CCS 007–015.

### Tasks the repository can support

- Keep linguistic units and authored line breaks usable.
- Coordinate reading effort, visual demand, speech and shot boundaries.
- Protect reveals and avoid distracting cue gaps.

**Expected output:** A segmentation/timing profile and cue-level revision brief.

**Human review:** A timed playback review confirms meaning and effort; words-per-minute alone cannot establish readability.

### Example prompt 1

> Using the RAG, review [timed caption draft, language/audience profile and cut evidence]. Apply CCS 007–015 to phrase boundaries, line breaks, rendered width, reading time, speech/sound onset and shot changes. Treat source English speed ranges as starting profiles, not universal human limits, and preserve jokes/reveals at the intended moment.

### Example prompt 2

> Challenge [caption timing or speed report] against the RAG. Find aggressive edits made only to satisfy a metric, captions anticipating sound and shot alignment overriding essential words. Return cue-specific revisions and real playback questions.

## 5. Design readable positioning and adaptable presentation

**Production stage:** Visual presentation and platform review

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** CCS 008–009, 017 and 024–027; section 11.

### Tasks the repository can support

- Test rendered width, size, contrast and legibility in context.
- Avoid essential picture, graphics and signer collisions.
- Preserve user preferences where the actual player supports them.

**Expected output:** A presentation/positioning specification and device-check brief.

**Human review:** Caption, picture and platform teams inspect actual rendering; no styling promise is inferred from a text file.

### Example prompt 1

> Use the RAG to specify caption presentation for [aspect ratios, content and devices]. Cover actual rendered width, scalable size, contrast, speaker cues, essential picture protection and user styling where supported. Distinguish service defaults from universal limits and flag platform capabilities needing verification.

### Example prompt 2

> Review [caption render samples and layout] against the RAG. Identify clipping, collision with signers/graphics, colour-only speakers and user-style settings that lose content. Produce presentation fixes and the environments that still need testing.

## 6. Plan live captions and on-demand correction

**Production stage:** Live production and catch-up management

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** CCS 028–030.

### Tasks the repository can support

- Prepare glossaries, running orders and speaker information.
- Define competent monitoring, latency/accuracy goals and fallback.
- Review recordings as prerecorded assets before reuse.

**Expected output:** A live-caption operating/rehearsal brief and catch-up plan.

**Human review:** The producer and live-caption practitioners confirm real staffing, monitoring and recovery arrangements.

### Example prompt 1

> Using the RAG, plan live CCS for [event, languages and distribution]. Specify preparation material, names, glossary, running-order updates, captioner support, monitoring and fallback. Propose locally agreed quality/latency evidence without inventing universal thresholds. Include review and correction for the on-demand recording.

### Example prompt 2

> Challenge [live-caption plan] against the RAG. Identify no response to feed failure, unverified automation quality and a live track republished unchanged as final prerecorded captions. Return rehearsal, recovery and correction tasks.

## 7. Choose formats and preserve meaning through transformations

**Production stage:** Timed-text delivery and engineering handoff

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** CCS 031–033.

### Tasks the repository can support

- Select supported authoring/interchange/distribution profiles.
- Preserve times, encoding, breaks, regions, speaker/sound data and version links.
- Validate syntax separately from converted and rendered equivalence.

**Expected output:** A timed-text delivery profile and transformation test plan.

**Human review:** Engineering and caption leads verify the actual destination chain and current format/profile support.

### Example prompt 1

> Use the RAG to specify timed-text delivery for [authoring and distribution chain]. Apply CCS 031–033 to format/profile, timebase, frame rate, end-time semantics, encoding, metadata, regions and version links. Plan syntax validation and end-to-end conversion/rendering comparison; do not assume successful conversion preserves meaning.

### Example prompt 2

> Review [format conversion or packaging proposal] using the RAG. Find dropped speaker metadata, changed cue timing, lost layout or a supported-format claim based only on a catalogue. Produce a chain-specific validation and visual/editorial retest plan.

## 8. Verify accessible caption controls and published playback

**Production stage:** Player integration and publication QA

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** Section 13; section 14: Player operation and Transformation.

### Tasks the repository can support

- Check discovery, activation, naming and input access.
- Verify selection/state and presentation on relevant devices.
- Distinguish local asset quality from the published path.

**Expected output:** A scoped player/playback evaluation plan.

**Human review:** Platform testers and access specialists inspect real player behaviour; the producer retains unresolved publication checks.

### Example prompt 1

> Using the RAG, plan player verification for [published or test service and supported environments]. Cover finding, selecting, configuring and retaining CCS with keyboard, assistive technologies and relevant device controls. Check labels, track versions, seeking and transformation effects, recording actual evidence or Not tested.

### Example prompt 2

> Challenge [caption publication evidence] against the RAG. Identify an uploaded valid file treated as proof of operable controls, state lost after seeking or caption choices inaccessible to AT. Return precise integration defects and outstanding tests.

## 9. Bound automation and retain editorial accountability

**Production stage:** AI-assisted caption production

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001); [S003 — AGENTS.md](RAG_Reference.md#s003).

**Relevant source sections:** Section 15; AGENTS: derived artefacts and validation claims.

### Tasks the repository can support

- Identify automated stages and required human review.
- Constrain hallucinated wording, speakers, sounds and unapproved editorial changes.
- Maintain source/cut provenance and accountable correction.

**Expected output:** An AI-assisted workflow brief and review/decision record.

**Human review:** The caption editor and producer decide acceptance; algorithmic confidence or nominal accuracy does not replace review.

### Example prompt 1

> Use the RAG to design AI assistance for [caption workflow]. Separate transcription, diarisation, line breaking, timing, sound classification and validation tasks from human editorial decisions. Retain exact source versions, approved glossary, uncertainty, review scope and corrections. Do not approve unreviewed output or invent confidence thresholds.

### Example prompt 2

> Audit [automated-caption process and claims] against the RAG. Find hallucinated names/sounds, unapproved simplification, silent language translation and automatic validation claimed without a run. Produce a bounded review workflow and truthful evidence statement.

## 10. Evaluate, accept and maintain caption quality

**Production stage:** Quality assurance, release and change control

**Retrieve:** [S001 — Closed_Caption_Subtitle_Guidelines.md](RAG_Reference.md#s001).

**Relevant source sections:** Sections 14 and 16; CCS 001–033.

### Tasks the repository can support

- Combine availability, syntax, editorial, timing, visual, player and audience checks.
- Keep serious meaning-changing errors visible despite aggregate scores.
- Record exceptions, changes and targeted retest by exact version.

**Expected output:** A caption acceptance/release draft and change/retest register.

**Human review:** The authorised caption/production owner accepts based on actual scope and evidence; unresolved serious barriers are not a pass.

### Example prompt 1

> Using the RAG, prepare an acceptance plan for [caption assets, profiles and evidence]. Separate all QA layers, retain applicable CCS IDs and record actual results or Not tested. Identify serious omissions, speaker errors, spoilers, unreadable rendering and unreviewed automation. Include proportionate Deaf/hard-of-hearing audience evidence and a human decision record.

### Example prompt 2

> Challenge [caption QA summary or change request] against the RAG. Identify high aggregate accuracy hiding a meaning-changing defect, changed audio retaining stale captions and an exception mistaken for conformance. Return corrections, impact and retest needs.

## Editorial and production decision record

For each adopted result, record the project/task, source revision and sections used, observed editorial/production issue, barrier or opportunity, chosen option and rejected alternatives, expected outcome, evidence available, assumptions, unresolved constraints, accountable person, next check and review trigger. Use actual names and dates when agreed; leave them unassigned when unknown. Record acceptance and residual risk only when the accountable person has made the decision.

Revisit the reference when repository sources change, a new platform or context is introduced, implementation changes invalidate assumptions, or user feedback exposes a barrier. Compare changed sources rather than silently replacing the basis of existing decisions.
