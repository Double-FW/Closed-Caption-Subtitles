---
title: "Closed Caption Subtitle Guidelines"
short_title: "Closed Caption Subtitles"
language: "en-GB"
document_type:
  - "production_guideline"
  - "accessibility_standard"
  - "editorial_guideline"
  - "technical_delivery_reference"
  - "ai_governance_reference"
content_status: "organisation_agnostic_synthesis"
date_processed: "2026-09-18"
version: "1.0"
jurisdictional_context:
  - "international"
standards_context:
  - "WCAG_2.2"
  - "EBU_TT"
  - "EBU_TT_D"
  - "TTML"
  - "IMSC"
  - "WebVTT"
primary_domains:
  - "closed_captions"
  - "subtitling"
  - "broadcast_accessibility"
  - "streaming_accessibility"
  - "audiovisual_production"
  - "media_player_accessibility"
audiences:
  - "caption_authors"
  - "subtitle_editors"
  - "live_captioners"
  - "producers"
  - "commissioners"
  - "content_teams"
  - "accessibility_specialists"
  - "quality_assurance_teams"
  - "media_player_developers"
  - "platform_engineers"
  - "localisation_teams"
  - "ai_governance_systems"
defined_term:
  term: "Closed Caption Subtitles"
  abbreviation: "CCS"
  definition: "A synchronised, user-selectable text track that conveys spoken dialogue and the non-speech audio information needed to understand or experience audiovisual content."
source_basis:
  primary_source: "BBC Subtitle Guidelines version 1.2.5, March 2026"
  secondary_sources:
    - "WCAG 2.2 and W3C WAI media guidance"
    - "EBU Tech 3350, EBU-TT Part 1"
    - "EBU Tech 3380, EBU-TT-D"
editorial_treatment:
  - "Removed BBC-specific commissioning, metadata, file-naming and playout instructions."
  - "Retained the BBC approach to fidelity, timing, synchronisation, speaker identification, sound, music, placement and editorial judgement."
  - "Changed the defined term from subtitles to Closed Caption Subtitles as requested."
  - "Separated universal accessibility requirements from language-specific and platform-specific production defaults."
  - "Reframed colour as a supporting cue rather than the only means of identifying a speaker."
  - "Reframed fixed character limits as legacy or delivery-profile constraints rather than universal readability rules."
  - "Added WCAG requirements for prerecorded and live captions and for accessible player controls."
  - "Added EBU format guidance for interchange and IP distribution."
  - "Added governance for automated transcription and AI-assisted authoring."
normative_language:
  must: "A requirement necessary to claim conformance with this guideline."
  should: "A strong recommendation that may be varied for a documented editorial, linguistic or technical reason."
  may: "A permitted option."
ai_ingestion_guidance:
  - "Use this document to generate production requirements, authoring prompts, validation rules, test cases and governance checks for Closed Caption Subtitles."
  - "Treat MUST, SHOULD and MAY according to the normative language definitions in the metadata."
  - "Do not convert a BBC-specific or legacy Teletext constraint into a universal requirement."
  - "Do not use colour as the sole method of identifying a speaker."
  - "Do not treat dialogue-only subtitles, transcripts or automatic speech recognition output as equivalent to Closed Caption Subtitles."
  - "Do not simplify, censor, translate or sanitise speech unless the source audio or an authorised editorial decision requires it."
  - "Do not invent a speaker identity, sound, lyric, accent or inaudible word. Mark uncertainty for human review."
  - "Apply timing and reading-speed recommendations in the context of language, genre, age, visual complexity and delivery platform."
  - "Retrieve the current delivery profile and applicable law before selecting a file format or making a compliance claim."
  - "Require human review of machine-generated captions before prerecorded publication."
  - "For live content, disclose and manage the expected accuracy and latency of the selected captioning method."
---

# Closed Caption Subtitle Guidelines

## Purpose

These guidelines define how to create, deliver and govern high-quality Closed Caption Subtitles for prerecorded and live audiovisual content. They are intended for broadcasters, streaming services, publishers, employers, educators, public bodies, production companies and other organisations. They are not tied to a particular brand, commissioning process or distribution platform.

The guidelines use the editorial and technical approach established by the BBC Subtitle Guidelines. They supplement that approach with WCAG 2.2 requirements and European Broadcasting Union specifications. The result is a production standard concerned with both technical availability and the audience's experience.

Technical presence is not enough. A caption track can exist and still fail because it is inaccurate, late, too fast, badly positioned, incomplete or impossible to select. Good Closed Caption Subtitles provide access to meaning, character, tone, timing and relevant sound without demanding more attention than the content itself.

## Contents

1. Scope and terminology
2. Principles
3. Roles and workflow
4. Editorial accuracy and fidelity
5. Caption structure and line breaks
6. Timing and synchronisation
7. Speaker identification
8. Sound effects music and speech characteristics
9. Visual presentation and positioning
10. Live Closed Caption Subtitles
11. Children and other audience contexts
12. Technical formats and delivery
13. Accessible media player requirements
14. Quality assurance and acceptance tests
15. AI-assisted production governance
16. Exceptions and change control
17. Sources

## 1. Scope and terminology

### Closed Caption Subtitles

In this document, **Closed Caption Subtitles**, abbreviated to **CCS**, means a synchronised text track that viewers can turn on or off. It conveys spoken dialogue and the non-speech audio needed to understand or experience the content, including meaningful sound effects, music, speaker identity and relevant vocal delivery.

The phrase is used here as a defined organisational term. Industry terminology varies. WCAG usually uses *captions* for same-language access to speech and meaningful sound, while *subtitles* may mean a translation that contains dialogue only. In the United Kingdom, *subtitles* commonly includes the access service provided for Deaf and hard-of-hearing viewers. The defined term CCS prevents either regional usage from silently narrowing the service.

### Related services

CCS must not be confused with the following:

| Service | Function | Why it is not equivalent to CCS |
| --- | --- | --- |
| Dialogue-only subtitles | Present spoken words, often in another language | They may omit speaker identity, sound effects, music and other audio information |
| Open captions | Are permanently embedded in the picture | They cannot be turned off and usually cannot be restyled by the viewer |
| Transcript | Presents audio information as a separate document | It is not necessarily synchronised with the audiovisual content |
| Automatic transcript | Records machine-recognised speech | It may be inaccurate and usually omits editorial sound information and reliable speaker identification |
| Audio description | Describes important visual information through audio | It serves a different sensory access need |
| Sign-language interpretation | Presents content in a signed language | A signed language is not a visual encoding of written or spoken language |

### Coverage

These guidelines apply to prerecorded and live video with meaningful audio. They cover editorial authoring, presentation, delivery, player behaviour, quality assurance and governance.

WCAG 2.2 Success Criterion 1.2.2 requires captions for prerecorded audio in synchronised media at Level A, subject to its stated exception for media that is an alternative for text. Success Criterion 1.2.4 requires captions for live audio in synchronised media at Level AA. Legal and regulatory duties may extend beyond WCAG and vary by jurisdiction and service type.

## 2. Principles

### Preserve access to the soundtrack

CCS should give viewers the fullest reasonable access to the soundtrack. Spoken words, meaningful pauses, sound effects, music, tone and speaker changes can all carry information. Caption authors should not remove information merely to make the track look tidy.

### Prefer fidelity over unnecessary simplification

Use the speaker's words where reading time and presentation permit. Do not automatically remove conversational language, repetition, names, strong language, dialect or apparent grammatical errors. These features can convey character, identity, humour, emotion and plot.

Fidelity does not mean mechanically transcribing every sound. The caption author must decide which audio information is relevant and how to express it clearly. Editing may be required when speech is too fast, several conversations overlap or the visual action also demands attention.

### Design for reading and watching together

Viewers must divide their attention between the picture and the caption. Timing, line breaks, position and density should allow them to follow both. A caption that is accurate but absorbs all available attention does not provide an equivalent experience.

### Keep meaning synchronised

CCS should appear with the sound it represents. A caption must not reveal a joke, answer, entrance, alarm, impact or other dramatic event before it occurs. Delayed captions can be equally disruptive because they detach words from speakers and reactions.

### Preserve control

The viewer must be able to find, activate and deactivate a closed track. Where the platform permits, the viewer should also be able to adjust size, colour, background and position. Author styling should provide a reliable default without unnecessarily overriding user preferences.

### Use more than one cue

Do not rely on colour alone to identify speakers or convey meaning. Colour may support labels, punctuation, placement or context. This adapts the BBC's established speaker-colour method to the WCAG principle that colour must not be the only visual means of conveying information.

### Treat automation as assistance

Speech recognition, diarisation, translation and language models may accelerate production. They do not remove the need for editorial judgement, synchronisation, sound description, name checking or quality review.

## 3. Roles and workflow

Accessibility should be planned before production rather than added after delivery.

| Role | Responsibility |
| --- | --- |
| Commissioner or content owner | Defines which content requires CCS, the languages, service level, deadlines and approval authority |
| Producer | Supplies final or stable media, scripts, running orders, names, terminology, music information and contextual notes |
| Caption author or live captioner | Creates accurate, synchronised and editorially complete CCS using these guidelines |
| Caption editor | Reviews fidelity, sound information, speaker identification, timing, line breaks and language |
| Technical operations | Selects the format, validates the file, packages the track and preserves synchronisation through distribution |
| Player or platform team | Provides discoverable, operable caption controls and renders the track reliably across supported devices |
| Quality assurance | Tests the file, rendering, content, player and representative journeys |
| Accessibility lead | Owns the guideline, resolves accessibility exceptions and includes audience evidence in revisions |

The production workflow should include the following controls:

1. Confirm the master media version, frame rate, aspect ratio, language and delivery platforms.
2. Obtain scripts and names as references, but caption the final audio rather than assuming that the script is accurate.
3. Create or import the timed track.
4. Edit for accuracy, sound information, reading, synchronisation and picture interaction.
5. Validate the file against the selected technical profile.
6. Review the rendered CCS with the final media on representative players and devices.
7. Correct failures and retain the approved source, delivery files and quality record.
8. Revalidate the track after any edit, conversion, transcode or platform migration.

## 4. Editorial accuracy and fidelity

### CCS 001 Provide complete access to meaningful audio

CCS **must** include:

- all dialogue needed to understand the content;
- speaker identification when the speaker is not visually or contextually clear;
- non-speech sounds that affect meaning, atmosphere, action, humour or participation;
- music or lyrics when they carry meaning or are a focus of the content; and
- relevant vocal information, such as whispering, shouting or speech being drowned out, when it cannot be inferred reliably from the picture.

Omitting dialogue or important sound information can fail WCAG 2.2 Success Criterion 1.2.2 or 1.2.4.

### CCS 002 Prefer verbatim speech

Prepared CCS **should** be verbatim when the words can be read in the available time. Small conversational words can alter tone and meaning. Names used to address someone can identify relationships or who is expected to respond. Keep the first and last words of visible speech wherever possible because they are prominent to viewers who lip-read.

Do not simplify language on the assumption that Deaf or hard-of-hearing viewers need simplified content. Do not translate within a same-language CCS track. A simplified or translated version may be offered as a separate, clearly identified service.

### CCS 003 Edit only for a defined reason

Editing is permitted when verbatim text would be unreadable, would obscure essential picture information or would prevent the viewer from following the action. Preserve meaning, register, order, character and emotional effect.

When editing:

- remove expendable material across the passage rather than deleting one complete idea merely because it is convenient;
- retain plot, factual and safety information;
- preserve names, technical terms, jokes, rhymes and catchphrases when relevant;
- do not change tense or grammatical relationships accidentally;
- keep visible words that are easy to lip-read; and
- review the following caption because one edit can alter its meaning or grammar.

### CCS 004 Preserve editorial treatment

CCS **must** reflect the audio actually delivered to the audience. Do not censor strong language independently. If the programme bleeps, mutes or replaces a word, represent the treatment rather than reconstructing audio the audience did not receive.

Examples include `[bleep]`, a supplied replacement word, or a concise label such as `[word muted]`. Choose one convention and apply it consistently. Labels should not reveal material deliberately withheld by the source edit.

### CCS 005 Verify names terms and numbers

People, places, organisations, technical vocabulary, quotations, scores, dates and figures **must** be checked against an authoritative source when available. A plausible spelling generated by speech recognition is not evidence.

Numbers should be formatted consistently and for rapid reading. Use numerals for scores, measurements and dense numerical information unless words better preserve the spoken emphasis or avoid ambiguity. Language and regional conventions must be defined in the applicable style profile.

### CCS 006 Include relevant on-screen text when necessary

Do not duplicate legible on-screen text without a reason. If essential text is too small, too brief, obscured or degraded in the delivered image, include it in the CCS when it is necessary to understand or act. Examples may include a speaker's identity, a location, a warning or contact information.

The caption and graphic must not obscure one another. Where possible, production teams should make the source graphic accessible rather than forcing the caption track to repair it.

## 5. Caption structure and line breaks

### CCS 007 Use complete linguistic units

Each caption **should** contain one complete sentence or a coherent part of a longer sentence. Short sentences may share a caption when timing requires it. Long sentences may continue across captions, but each segment should form a natural phrase or clause.

Do not split:

- an article from its noun;
- a preposition from the phrase that follows;
- a pronoun from its verb;
- an auxiliary from the main verb;
- a conjunction from the clause it introduces; or
- a word across lines.

Punctuation is usually the strongest place to break a line. Linguistic coherence has priority over producing lines of equal length.

### CCS 008 Limit line count

Use no more than two lines for landscape and square video as the normal default. Up to three lines may be used for vertical video or an exceptional picture layout when the track remains readable and does not obscure essential information.

Line count is an editorial control, not permission to fill every available line. A short caption should remain short.

### CCS 009 Control rendered width

Caption width should be governed by the rendered region, font and device rather than by character count alone. Proportional characters occupy different widths, and viewers may change presentation settings.

For 16:9 landscape content, the BBC model uses a caption line occupying no more than roughly 68% of video width within a central presentation area. For 4:3, square and vertical content, a wider proportion may be needed. These values are starting points to test, not universal conformance thresholds.

A limit of 37 monospaced characters is a legacy Teletext constraint. Apply it only when the target broadcast or interchange profile requires it. Do not impose it on every web, application or IP-delivered track.

### CCS 010 Prefer authored line breaks

Caption authors **should** insert meaningful line breaks. Automatic wrapping can separate closely related words or alter a carefully placed caption. Players must still handle reflow safely when the viewer changes text size or when the target renderer uses a different font.

When timing, accurate editing and ideal line breaking cannot all be achieved, preserve meaning and timing before visual symmetry.

## 6. Timing and synchronisation

### CCS 011 Use a reading-speed profile

For prepared English-language CCS, 160 to 180 words per minute is a useful starting range. It equates to approximately 0.33 to 0.375 seconds per word. A four-word caption would normally remain for about 1.2 seconds or longer.

This is not a universal human limit. Language, age, vocabulary, genre, visual complexity, caption position and familiarity affect reading. Viewers often prefer faithful text, and aggressive editing solely to meet a numerical target can remove meaning. Each language and service should maintain an evidence-based timing profile.

Give more time for unfamiliar terms, long figures, multiple speakers, complex graphics, unusual placement or visually busy scenes. Faster presentation may be justified to preserve a joke, visible lip movements, lyrics, critical factual information or deliberately rapid delivery. Record persistent departures from the service profile during quality review.

### CCS 012 Synchronise with speech

CCS **must** begin at, or as close as technically possible to, the onset of the speech or sound it represents. It should normally end with the corresponding audio. A caption left after speech ends may be reread or attributed to the wrong shot or speaker.

Do not anticipate speech or sound merely to gain reading time. Never reveal a dramatic sound, answer or punchline before the audience hears it. Prepared CCS should not lag materially behind speech. The BBC model treats a delay of more than two seconds as unacceptable and encourages much tighter synchronisation when a visible speaker can be lip-read.

### CCS 013 Respect shot and scene changes

Align caption changes with shot changes when this improves comfort and preserves the relationship between text and image. Avoid beginning in one shot and ending midway through an unrelated shot when the caption can be split or timed more naturally.

Do not carry a caption into a new scene when the speaker or sound no longer belongs there. Do not leave text over a reaction shot if it obscures the reaction or spoils the timing. Shot alignment is a means of supporting meaning, not an excuse to remove essential words.

### CCS 014 Avoid distracting gaps and flicker

Use available time for reading. Do not create a brief blank interval merely to represent a natural pause if the result is visual flicker. If the delivery format requires a small technical gap between cues, follow the platform profile without creating a perceptible break in continuous speech.

### CCS 015 Represent hesitation and interruption consistently

Use a documented punctuation convention for pauses, unfinished speech, interruption and continuation. Do not scatter ellipses through captions merely because a sentence crosses cue boundaries. Indicate hesitation only when it contributes to character, meaning or dramatic rhythm.

## 7. Speaker identification

### CCS 016 Identify ambiguous speakers

The viewer must be able to determine who is speaking when the picture and context do not make it clear. Use the least intrusive reliable method.

Permitted methods include:

- a concise speaker label, such as `MAYA:`;
- a dash for each speaker when two speakers share a caption;
- consistent placement near the speaker when the platform, picture and user settings support it;
- a directional cue for an off-screen voice; and
- a consistent speaker colour as a supporting cue.

Labels should use names when known. Do not assign gender, age, ethnicity, disability or another characteristic merely to fill an information gap. Use a neutral functional label such as `INTERVIEWER:`, `CALLER:` or `OFF-SCREEN VOICE:` when identity is unknown.

### CCS 017 Do not depend on colour alone

The BBC broadcast tradition uses white, yellow, cyan and green text on black to distinguish speakers. An organisation may retain this familiar palette, provided every speaker change remains understandable without colour. Context, labels, dashes or placement must supply the additional cue.

Apply a speaker's colour consistently within a scene or programme. Do not reuse a colour for speakers who may be confused with one another. Test the track in monochrome and with colour-vision simulations.

### CCS 018 Preserve speaker metadata

Where the format permits, identify speakers through machine-readable metadata as well as visible presentation. Metadata supports search, transformation, quality checks and alternative rendering. It must not expose confidential or inferred personal information.

## 8. Sound effects music and speech characteristics

### CCS 019 Caption meaningful sounds

Caption sounds that affect understanding, atmosphere, timing, humour or action. Do not caption every audible event. A sound that is obvious from the picture may need no label, while the same sound off screen may be essential.

Describe the sound rather than the visible action. `[floorboards creak]` describes audio; `[they walk upstairs]` describes an action. Prefer concise active wording. If direction matters and is not visually clear, position the label or add a restrained directional cue.

Sentence case in square brackets is the recommended neutral default because long passages of capitals are harder to read. An established service may use uppercase labels consistently, particularly in legacy broadcast workflows.

### CCS 020 Represent music according to its function

Identify music when it is part of the action, significant to the story, needed for atmosphere or otherwise relevant to the audience's experience. Name a recognisable work when the title and attribution can be verified. For unidentified music, describe only the quality that matters, such as `[tense music]` or `[upbeat dance music]`.

Do not add a subjective mood label when the music is incidental and its function is already clear. Do not identify a work from uncertain machine recognition.

### CCS 021 Caption lyrics when relevant

Caption lyrics when they are foreground content, advance the story, carry humour or are intended to be followed. Synchronise them with the performance and preserve rhythm where possible. Use a consistent music marker, such as `♪`, when supported by the delivery profile.

Lyrics may need timings outside the ordinary speech-speed range. Do not reveal a lyric early to satisfy a reading-speed rule. Rights and localisation teams should determine whether translated or reproduced lyrics require separate clearance.

### CCS 022 Preserve accent dialect and grammar respectfully

Do not use phonetic spelling merely to mark a person as different. Preserve relevant vocabulary, syntax and grammar without caricature. Identify an accent only when it matters to the content and is not otherwise apparent. A label should be factual and specific enough to serve the editorial purpose.

Do not tidy incoherent or non-standard speech in drama when the way of speaking is part of the character or action. In factual content, light editing may be used when spoken phrasing becomes incomprehensible in writing, but it must not change the person's meaning or make them appear more or less articulate for editorial convenience.

### CCS 023 Explain inaudible or obscured speech

When words cannot be recovered, explain why rather than inventing them. Examples include `[music drowns speech]`, `[speech indistinct]` or `[speaks away from microphone]`. Avoid judgemental labels such as *incomprehensible* when the cause is uncertain.

If a prolonged silence might make viewers think the service has failed, a relevant label such as `[long pause]` or `[introductory music]` may reassure them that the track remains active.

## 9. Visual presentation and positioning

### CCS 024 Provide a readable default

The default presentation should use a clear proportional sans-serif font with high contrast. White text on a black or sufficiently opaque dark background is a reliable default. Padding should separate the text from the background edge, and adjacent line backgrounds should not leave distracting gaps.

Avoid decorative fonts, condensed faces, thin weights, excessive italics and long passages in capitals. Capitalisation, italics or another style may indicate emphasis only when the meaning remains available to viewers who override the styling.

### CCS 025 Meet contrast requirements

Text and background must meet the applicable WCAG contrast requirement in the rendered player. Test every permitted speaker colour against its actual background. A black box is useful only if it remains opaque enough over the brightest and most complex frames.

Do not assume that a colour name or nominal RGB value guarantees the final contrast. Rendering, opacity, HDR presentation and user preferences can alter the result.

### CCS 026 Use scalable and resolution-independent sizing

Authoring should use relative units or the selected timed-text profile rather than fixed pixels. The BBC model authors line height at approximately 7% to 8% of active video height for landscape, 4:3 and square content, and approximately 3.9% to 4.5% for vertical video. Treat these as reference values that require device testing.

Players should support user adjustment where the platform permits. Scaling must not cause clipping, lost text, unsafe overlap or unannounced rewrapping. If the platform cannot determine a safe reduced size, it should preserve the authored default rather than risk illegibly small text.

### CCS 027 Protect essential picture information

Place captions toward the lower part of the image by default, but move them when they would obscure a speaker's mouth, an identity caption, a score, a demonstration, a sign-language interpreter or other essential information. Vertical movement usually causes less confusion than horizontal movement.

Player controls, notifications, advertising overlays and system UI must not cover CCS. The layout should reserve space, move the captions or pause presentation while a blocking overlay is displayed. Caption placement must be tested in full-screen, embedded, mobile, landscape and portrait modes.

## 10. Live Closed Caption Subtitles

### CCS 028 Plan live captioning

Live CCS requires preparation. Supply captioners or the managed service with names, specialist vocabulary, scripts, running orders, likely questions, locations, music and prerecorded inserts. Provide a clean audio feed and a communication route for production changes.

### CCS 029 Prioritise meaning accuracy and latency

Live CCS should remain as close to verbatim as the speed and genre allow. Accuracy and latency must be assessed together. A perfectly transcribed caption that arrives too late to connect with the speaker or action is not a good outcome.

The service must define how it measures:

- recognition and editorial accuracy;
- serious or meaning-changing errors;
- delay from audio to display;
- speaker identification;
- completeness of speech and meaningful sound; and
- recovery after the captioner falls behind.

Do not rush a backlog onto the screen merely to catch up. Skip safely, summarise where the authorised live method permits, and resume at the current point. Meaning-changing errors should be corrected promptly when the correction will help rather than further confuse the viewer.

### CCS 030 Treat recordings as prerecorded content

A recording made from a live event becomes prerecorded media when published later. Review and correct the live track before reuse. The availability of captions during the event does not prove that the archived track meets the standard for prerecorded content.

## 11. Children and other audience contexts

Caption timing and language should reflect the intended audience without withholding the content available to hearing viewers. Children who are still developing reading fluency may need slower captions, simpler line structures and more time to look at the picture. This does not justify rewriting character, humour or subject matter into a different programme.

Services should create tested profiles for contexts such as:

- early readers;
- education and training;
- technical demonstrations;
- sport and rapid live commentary;
- drama, comedy and music;
- vertical and short-form video; and
- interactive media and games.

Each profile should state what may vary and which core requirements remain unchanged.

## 12. Technical formats and delivery

### CCS 031 Select the format from the delivery chain

No single file format is correct for every service. Select a documented profile supported end to end by authoring, validation, packaging, distribution and playback.

Common choices include:

| Context | Suitable formats and standards |
| --- | --- |
| Web video | WebVTT is widely supported; TTML or an IMSC profile may be used where the player supports it |
| IP and streaming distribution | EBU-TT-D or an appropriate IMSC/TTML profile |
| Archive and interchange | EBU-TT Part 1 or another documented TTML profile |
| Legacy broadcast exchange | EBU STL where required by the broadcast chain |

EBU Tech 3350 defines EBU-TT Part 1 as an XML format for subtitle archiving and interchange. EBU Tech 3380 defines EBU-TT-D for distributing subtitles over IP networks and aligns its version 1.0.1 features with W3C IMSC 1.0.1. Legacy EBU STL remains relevant to some broadcast systems but should not constrain modern platforms unless interoperability requires it.

### CCS 032 Preserve semantic and technical data

The delivery file **must** preserve:

- correct in and out times using the format's timing semantics;
- language metadata;
- reading order and line breaks;
- speaker and sound roles where the format supports them;
- styling and regions needed for the approved presentation;
- character encoding, normally UTF-8 for modern text formats; and
- a stable link between the caption asset and the exact media version.

Conversion between formats must account for differences such as inclusive and exclusive end times, frame rates, supported characters, regions, styling and metadata. A successful file conversion does not prove that the rendered result is equivalent.

### CCS 033 Validate syntax and rendering

Every final file must pass a validator appropriate to its declared format and profile. It must also be played against the delivered media. Validation cannot detect misspelled names, omitted sounds, misleading speaker labels, poor breaks or visual obstruction.

## 13. Accessible media player requirements

The service fails if a good CCS file cannot be found or used.

The player **must**:

- expose a clear control for turning CCS on and off;
- identify available languages and tracks accurately;
- make the caption control operable by keyboard, touch, pointer, switch access and supported voice control;
- expose the control's name, role, state and options to assistive technologies;
- provide a visible focus indicator and sufficient contrast;
- retain synchronisation while seeking, changing speed or resuming playback;
- avoid obscuring captions with controls and overlays;
- support full-screen and orientation changes; and
- preserve CCS through casting or external-display routes where the platform claims support.

The player **should**:

- remember the viewer's caption preference where this can be done transparently;
- allow text size, font, colour, background and position to be adjusted;
- offer an interactive transcript when useful;
- allow playback speed changes without losing caption synchronisation; and
- expose the caption text to supported screen-reader and braille experiences when the platform permits.

## 14. Quality assurance and acceptance tests

### Test layers

| Layer | Test question | Method |
| --- | --- | --- |
| Availability | Is an appropriate CCS track present for every required asset and language | Catalogue and package inspection |
| File conformance | Does the file satisfy its declared syntax and profile | Automated validation |
| Editorial completeness | Are dialogue, speakers, sounds, music and treatment accurately represented | Human review against final audio and picture |
| Timing | Are cues readable and synchronised without revealing information early | Timed playback review and metric checks |
| Visual presentation | Is the track legible and clear of essential picture information and overlays | Device and viewport testing |
| Player operation | Can viewers find, activate, configure and retain CCS with supported inputs and assistive technologies | Manual accessibility testing |
| Transformation | Does the track remain equivalent after conversion, transcoding, packaging and distribution | End-to-end comparison |
| Audience outcome | Can Deaf and hard-of-hearing viewers follow representative content with reasonable effort | Research and usability testing |

### Minimum acceptance criteria

A CCS asset must not be approved when:

- the track is absent, mislabelled or attached to the wrong media version;
- dialogue or a meaningful sound is omitted;
- a caption materially changes the meaning of the audio;
- a speaker is misidentified;
- timing reveals information before the source or creates a material disconnect;
- captions are clipped, obscured or unreadable in a supported presentation;
- the player control is inaccessible or fails to change the caption state;
- user styling causes loss of content or function; or
- an automatic track has not received the review required by the service policy.

Minor punctuation or styling defects should still be recorded and corrected according to the quality threshold. A high aggregate accuracy score must never hide a small number of serious, discriminatory, defamatory, safety-critical or meaning-changing errors.

## 15. AI-assisted production governance

AI may support transcription, cue generation, line breaking, speaker diarisation, term checking, sound classification, translation, conformance validation and quality triage. Its use must remain accountable.

### Required controls

An AI-assisted workflow **must**:

1. retain the source audio and the exact media version used to create the track;
2. identify which stages were automated and which were reviewed by a person;
3. use an approved glossary for names, brands and specialist terms;
4. flag low-confidence speech, overlapping dialogue, music, sound effects and uncertain speakers;
5. prevent invented words from being silently substituted for inaudible speech;
6. check synchronisation after editorial changes;
7. route sensitive or meaning-changing content for human review;
8. validate the output format; and
9. retain an auditable approval record.

### Prohibited AI behaviour

An AI system must not:

- publish unreviewed automatic captions as compliant prerecorded CCS;
- infer a speaker's identity or personal characteristics from voice alone;
- remove dialect, disfluency or strong language to make speech appear more standard;
- translate a same-language track without a separate instruction and track label;
- summarise speech merely to satisfy a reading-speed metric when accurate editing is possible;
- omit sound information because the speech transcript appears complete;
- rely on colour alone for speaker distinction;
- claim WCAG conformance from file presence or automated validation alone; or
- learn a universal timing rule from one language, genre or platform profile.

### Machine-readable decision record

For each approved asset, an automated system should be able to retain or produce:

```yaml
closed_caption_subtitle_record:
  media_asset_id: "organisation-defined identifier"
  media_version: "approved master version"
  language: "BCP 47 language tag"
  content_mode: "prerecorded or live"
  file_format: "WebVTT, EBU-TT-D, IMSC, EBU-TT, STL or other approved profile"
  creation_method: "human, AI-assisted or live service"
  human_review_status: "required, completed or exception-approved"
  technical_validation: "pass or fail"
  editorial_review: "pass or fail"
  player_test: "pass or fail"
  unresolved_issues: []
  approver: "accountable role or identifier"
  approval_date: "YYYY-MM-DD"
```

## 16. Exceptions and change control

An exception must identify the requirement affected, the content and audience, the reason, the alternative access provided, the owner, the approval date and the remediation or review date. Cost or schedule pressure alone does not demonstrate that an inaccessible outcome is unavoidable.

The guideline owner should review this document when WCAG, EBU formats, browser support, broadcast regulation or audience evidence changes. The following parts should remain configurable rather than silently universalised:

- reading speed by language and audience;
- line width and line count by aspect ratio and platform;
- sound-label punctuation and capitalisation;
- speaker-identification conventions;
- delivery formats and metadata;
- live quality and latency thresholds; and
- age- or genre-specific profiles.

Changes should be tested with Deaf and hard-of-hearing viewers as well as authors, editors, engineers and platform teams.

## 17. Sources

### Primary source

- BBC, [Subtitle Guidelines](https://www.bbc.co.uk/accessibility/forproducts/guides/subtitles/), version 1.2.5, March 2026. The BBC guidance informed the editorial approach to fidelity, editing, line breaks, timing, synchronisation, shot changes, speakers, sound, music, typography, positioning, live subtitling and timed-text delivery. BBC-specific workflows, identifiers and fixed metadata values have not been carried into this organisation-neutral document.

### WCAG and W3C sources

- W3C, [Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/).
- W3C WAI, [Understanding SC 1.2.2 Captions Prerecorded](https://www.w3.org/WAI/WCAG22/Understanding/captions-prerecorded.html).
- W3C WAI, [Understanding SC 1.2.4 Captions Live](https://www.w3.org/WAI/WCAG22/Understanding/captions-live.html).
- W3C WAI, [Captions and Subtitles](https://www.w3.org/WAI/media/av/captions/).
- W3C WAI, [Media Players](https://www.w3.org/WAI/media/av/player/).
- W3C WAI, [Understanding SC 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).
- W3C WAI, [Understanding SC 1.4.3 Contrast Minimum](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

### European Broadcasting Union sources

- European Broadcasting Union, [EBU Tech 3350 EBU-TT Part 1 Subtitle Format Definition](https://tech.ebu.ch/publications/tech3350).
- European Broadcasting Union, [EBU Tech 3380 EBU-TT-D Subtitling Distribution Format](https://tech.ebu.ch/publications/tech3380).
- European Broadcasting Union, [EBU Tech 3264 Specification of the EBU Subtitling Data Exchange Format](https://tech.ebu.ch/publications/tech3264). This is a legacy exchange format and should be used only when the delivery chain requires it.

## Attribution and status

This document is an independent, organisation-agnostic synthesis. It is not an official BBC, W3C or EBU publication and does not imply endorsement by those organisations. WCAG conformance, broadcast compliance and legal duties must be evaluated against the current normative sources and the rules applicable to the service and jurisdiction.
