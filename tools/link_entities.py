#!/usr/bin/env python3
"""Add Obsidian wikilinks to campaign names across the notes.

Entities come from the ### headings of World DB/characters.md, locations.md
and factions.md. Each mention is linked as [[file#Heading|text]], so no files
need restructuring. The script is idempotent: existing links are left alone.

Rules
- Only the first mention per scope is linked: per session note, per ### entry
  in the World DB files, and per bullet in plot-threads.md.
- An entry never links to itself.
- Headings, code, and existing links/URLs are never touched.
- Matching is case-sensitive, to avoid linking common words.

Usage:  python tools/link_entities.py [--dry-run]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CAMPAIGN = ROOT / "Valkara - Ecos de un nuevo mundo"
DB = CAMPAIGN / "World DB"
DB_FILES = ["characters", "locations", "factions"]

# Headings that are not worth linking (unnamed or generic).
SKIP_HEADINGS = {
    "Erios's family (mother, sister, father)",
    "The mysterious rescuer",
    "The old man",
    "The Bielar leader",
    "The roadside stranger (unnamed)",
    "The aquamarine-robed weaver (unnamed)",
    "The three lunching *tejedores*",
    "The old janitor (unnamed)",
    "The sewers",
}

# Extra mention forms for a heading (matched case-sensitively).
EXTRA_ALIASES = {
    "Sergeant Holt": ["Holt"],
    "The Tejedora (the Weaver)": ["Tejedora"],
    "The Aurora": ["Aurora"],
    "The Kingdom of Doria": ["Doria"],
    "The Crown / Royal Guard": ["Royal Guard"],
    "The Aeonics": ["Aeonic"],
    "The Weavers": ["tejedores"],
    "The Ashen (*cenizos*)": [],
}


def plain(heading: str) -> str:
    """Heading text as Obsidian shows it (emphasis markers stripped)."""
    return heading.replace("*", "").strip()


def base_name(heading: str) -> str:
    """'The Witch's Arm (*El Brazo de Bruja*)' -> "The Witch's Arm"."""
    return re.sub(r"\s*\(.*\)\s*$", "", plain(heading)).strip()


def mention_forms(heading: str) -> list[str]:
    name = base_name(heading)
    forms = [name]
    if name.startswith("The "):
        forms.append("the " + name[4:])
    if "/" in name:  # "The Crown / Royal Guard"
        first = name.split("/")[0].strip()
        forms = [first] + ([f"the {first[4:]}"] if first.startswith("The ") else [])
    forms += EXTRA_ALIASES.get(heading, [])
    return forms


def load_entities():
    entities = []  # (form, file, heading_plain)
    for stem in DB_FILES:
        for line in (DB / f"{stem}.md").read_text(encoding="utf-8").splitlines():
            m = re.match(r"^###\s+(.*\S)\s*$", line)
            if not m or m.group(1) in SKIP_HEADINGS:
                continue
            heading = m.group(1)
            for form in mention_forms(heading):
                entities.append((form, stem, plain(heading)))
    entities.sort(key=lambda e: -len(e[0]))  # longest match wins
    return entities


PROTECTED = re.compile(r"\[\[.*?\]\]|\[[^\]]*\]\([^)]*\)|`[^`]*`|https?://\S+")


def link_line(line, entities_re, lookup, seen, own_heading):
    out, pos = [], 0
    for prot in list(PROTECTED.finditer(line)) + [None]:
        end = prot.start() if prot else len(line)
        segment = line[pos:end]
        last = 0
        for m in entities_re.finditer(segment):
            stem, heading = lookup[m.group(0)]
            key = (stem, heading)
            if key in seen or heading == own_heading:
                continue
            seen.add(key)
            out.append(segment[last:m.start()])
            out.append(f"[[{stem}#{heading}|{m.group(0)}]]")
            last = m.end()
        out.append(segment[last:])
        if prot:
            wl = re.match(r"\[\[([^#|\]]+)#([^|\]]+)", prot.group(0))
            if wl:  # an existing entity link counts as this scope's mention
                seen.add((wl.group(1), wl.group(2)))
            out.append(prot.group(0))
            pos = prot.end()
    return "".join(out)


def process(path: Path, entities_re, lookup, scope: str):
    text = path.read_bytes().decode("utf-8")  # keep CRLF as-is
    lines = text.split("\n")
    seen, own, in_fm = set(), None, False
    for i, line in enumerate(lines):
        if i == 0 and line.strip() == "---":
            in_fm = True
            continue
        if in_fm:
            in_fm = line.strip() != "---"
            continue
        if line.startswith("#"):
            if scope == "entry" and line.startswith("###"):
                seen, own = set(), plain(line.lstrip("#"))
            continue
        if scope == "line":
            seen = set()
        lines[i] = link_line(line, entities_re, lookup, seen, own)
    new = "\n".join(lines)
    if new != text:
        path.write_bytes(new.encode("utf-8"))
    return new != text


def main():
    dry = "--dry-run" in sys.argv
    entities = load_entities()
    lookup = {}
    for form, stem, heading in entities:
        lookup.setdefault(form, (stem, heading))
    pattern = "|".join(re.escape(f) for f in lookup)
    entities_re = re.compile(rf"(?<![\w\[|#])(?:{pattern})(?!\w)")
    targets = [(p, "file") for p in sorted((CAMPAIGN / "Current").glob("*.md"))]
    targets += [(DB / f"{s}.md", "entry") for s in DB_FILES + ["timeline"]]
    targets += [(DB / "plot-threads.md", "line")]  # one bullet per question
    for path, scope in targets:
        if dry:
            before = path.read_bytes()
            changed = process(path, entities_re, lookup, scope)
            path.write_bytes(before)
        else:
            changed = process(path, entities_re, lookup, scope)
        print(("would change " if dry else "changed ") + path.name if changed else f"unchanged {path.name}")


if __name__ == "__main__":
    main()
