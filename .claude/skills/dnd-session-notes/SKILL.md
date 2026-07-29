---
name: dnd-session-notes
description: Turn a raw D&D session transcript (.txt) into a session-summary note matching the existing Valkara campaign style (Title / Summary / Key Events / Open Questions), saved into English/ with the right filename. Use when the user gives a transcript file path and asks to write up session notes, generate a session summary, or invokes /dnd-session-notes.
---

# D&D Session Notes from Transcript

Turn a raw session transcript into a polished session-summary note for the Valkara campaign, matching the exact structure and tone already established in `Valkara - Ecos de un nuevo mundo/English/`.

## Input

- The user supplies a path to a `.txt` transcript - a raw transcription of the session's audio (speaker turns, in-character and out-of-character chatter mixed together, often messy or phonetic).
- If no file path is given, ask for it. Don't guess a path or invent content.
- The session date drives the output filename. If it isn't obvious from the transcript filename or from in-transcript references (e.g. someone stating the date), ask the user rather than inventing one.

## Before drafting

1. Read the two most recent existing files in `Valkara - Ecos de un nuevo mundo/English/` to recalibrate tone, section rhythm, and prose density - don't rely on memory of the format, it drifts.
2. Read the World DB for canon spelling and continuity: `Valkara - Ecos de un nuevo mundo/World DB/characters.md`, `locations.md`, `factions.md`, and `plot-threads.md`. The raw transcript will have inconsistent or phonetic spellings of names and terms (character names, place names, in-world words like *cenizo* or *báculo*) - normalize everything to the World DB's canon. If the transcript introduces a name or place that isn't in the World DB, keep it as-is and flag it to the user rather than guessing a spelling.
3. Read the full transcript before drafting anything. Identify the chronological run of distinct scenes or beats - these become the numbered Key Events subsections. Do this pass fully before writing, since an early beat's framing sometimes only makes sense in light of how the session ends (see how the Style rules below treat foreshadowing).

## Structure to produce

```
# D&D Session Summary: <Title>

## Summary
<one paragraph>

---

## Key Events

### 1. <Section title>
* **Bold lead-in:** Detail sentence(s).
* **Bold lead-in:** Detail sentence(s).

### 2. <Section title>
* **Bold lead-in:** Detail sentence(s).

### N. <Section title>
* **Bold lead-in:** Detail sentence(s).
    * Optional indented sub-bullet, only for a tight sequence of rapid actions within one beat.

---

## Open Questions
* **Bold lead-in:** Question sentence?
* **Bold lead-in:** Question sentence?
```

## Style rules

- Third person, past tense, narrative recap - not a transcript, and not a dialogue-by-dialogue log.
- **Title:** a short evocative phrase capturing the session's arc (e.g. "The Sparks of Rebellion", "The Gravity Inversion and the Desperate Flight") - never a generic "Session N" label.
- **Summary:** one paragraph, roughly 3-6 sentences, giving the full shape of the session - starting situation, major turns, ending situation or cliffhanger. It should work as a standalone recap for someone who missed the session.
- **Key Events:** 3-5 numbered subsections, each a distinct scene or beat, given a short descriptive heading rather than "Scene 1." Order is strictly chronological, matching how the session actually played out.
- Each bullet starts with a **bolded 2-5 word lead-in** acting as a mini-headline for that beat, then a colon, then 1-3 sentences of detail. Reach for nested sub-bullets only for a rapid back-and-forth combat sequence within a single beat - most bullets should be flat.
- Italicize in-world terms, foreign words, and named abilities/spells/items on first mention in a beat (*cenizo*, *Eldritch Blast*, *The Aurora*). Don't over-bold - reserve bold for the lead-in phrase, not every proper noun.
- Skip real-world meta-discussion (rules lookups, snack breaks, scheduling chatter) unless it materially affected play; if it did, compress it into a half-sentence rather than transcribing it.
- **Open Questions:** 3-5 bullets, each a forward-looking question a player would actually wonder after the session ends - motives, fates, secrets, unresolved threats. Not a GM to-do list. Same bold-lead-in-then-question format as Key Events.
- Use `---` horizontal rules to separate Summary / Key Events / Open Questions.

## Output

- Filename: `dnd_session_<YYYY-MM-DD>_en.md`.
- Save into `Valkara - Ecos de un nuevo mundo/English/`.
- After writing the file, tell the user it's done. Then remind them that `Valkara - Ecos de un nuevo mundo/World DB/README.md` defines an update workflow (timeline, characters, locations, factions, plot-threads) that should run next, and offer to do it - but don't run it unprompted, since it edits five other files.
