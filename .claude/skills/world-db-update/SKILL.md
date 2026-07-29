---
name: world-db-update
description: Update the Valkara campaign's World DB (timeline, characters, locations, factions, plot-threads) from a new English session note, per the workflow in World DB/README.md. Use after a new dnd_session_*_en.md file is added, or when asked to update the World DB / campaign database / lore files.
---

# World DB Update

Apply one new session's events to the five living-reference files in `Valkara - Ecos de un nuevo mundo/World DB/`, keeping them accurate and internally consistent without rewriting what's already there.

## Input

- The user will point to a session note, or just say "update the World DB" after a new one was added. If it's ambiguous which session note to use, list the files in `Valkara - Ecos de un nuevo mundo/Current/` and pick the most recent by the date in the filename (`dnd_session_<YYYY-MM-DD>_en.md`) - confirm with the user if more than one plausible candidate exists.
- If the session note doesn't exist yet, don't fabricate one - point the user to the `dnd-session-notes` skill first (or ask for the transcript).

## Before editing anything

1. Read the target session note in full.
2. Read all five World DB files in full - `characters.md`, `locations.md`, `factions.md`, `timeline.md`, `plot-threads.md` - before writing anything. Every edit needs to sit consistently next to what's already there; you cannot know what's a duplicate or a contradiction without reading the current state first.

## File-by-file process

**timeline.md** - Append one new dated entry (`### Session - <YYYY-MM-DD>: <Title>`), 2-4 sentences. This is a summary of the session note's summary, not a beat-by-beat recap - match the terse density of the existing entries, not the session note's own length.

**characters.md** -
- For each PC who did something notable, append 1-2 sentences to their *existing* entry. Don't rewrite the entry from scratch and don't repeat what it already says - add only what's new.
- For each NPC that's new or newly significant, add a new entry under `## NPCs` in the same terse style as existing ones (one paragraph, present-tense facts, no scene-by-scene narration).
- Mark deaths, exiles, or other major status flips in bold, matching the file's existing convention (e.g. `**Died**`, `**Killed**`, `**Formally exiled**`).

**locations.md** / **factions.md** - Add new entries for new places or groups the session introduced. Append a short update sentence to any existing entry whose status changed (destroyed, occupied, revealed purpose, etc.) rather than editing its original description away.

**plot-threads.md** -
- For every question currently in *Active*, check whether this session answered it.
  - Fully answered: move it to *Resolved*, using the file's existing dated format: `(raised YYYY-MM-DD, resolved YYYY-MM-DD)`. Keep the original question text in the line itself (don't replace it with only the answer) and append the resolution after a `**Resolved:**` marker, e.g. `- **Title** (raised ..., resolved ...) - <original question> **Resolved:** <one-line answer>`. A reader who only has the Resolved section should still be able to tell what was being asked.
  - Partially addressed: keep it in *Active*, but append a short clause noting what's now known.
  - Untouched: leave it exactly as it is.
- Add any newly raised questions to *Active*, tagged `(raised YYYY-MM-DD)`.
- Never delete a resolved question - it stays in the *Resolved* archive permanently, per the file's own rule.

## Judgment calls

- If the session note states something as inferred or likely rather than certain (e.g. "almost certainly the same person as X, though never stated outright"), carry that same hedge into the World DB. Don't launder an inference into a flat fact just because it's convenient for a cleaner entry.
- Prefer surgical edits (Edit, not Write) so unrelated existing content survives untouched. The only files that should ever be fully rewritten are ones you're creating for the first time.

## Output

After all five files are updated, give the user a short per-file summary of what changed (a few bullets, not a full diff) so they can sanity-check it before treating it as canon - don't just say "done."
