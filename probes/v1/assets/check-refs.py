#!/usr/bin/env python3
"""Check internal cross-references in a Markdown document set.

Usage: python3 check-refs.py [directory]

Scans every .md file in the directory except MANIFEST.md. For each
[text](target) link whose target is a local .md file (optionally with a
#anchor), it verifies:
  1. the target file exists;
  2. if an anchor is present, a heading in the target file slugifies to
     that anchor (GitHub style: lowercase, spaces to hyphens, drop
     punctuation);
  3. if the link text has the form "Doc N", the target file is doc-NN.md
     (catches references left pointing at the wrong file after a
     renumbering).

Prints one line per broken reference, then a summary line:
  PASS: all references resolve (N links checked)
  FAIL: K broken reference(s) of N links checked
Exit code 0 on PASS, 1 on FAIL. Standard library only.
"""

import os
import re
import sys

LINK_RE = re.compile(r"(?<!!)\[([^\]]*)\]\(([^)\s]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+(.*?)\s*#*\s*$")
DOC_TEXT_RE = re.compile(r"^Doc\s+(\d+)\b")
DOC_FILE_RE = re.compile(r"^doc-(\d+)\.md$")


def slugify(heading):
    text = heading.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)
    return text.replace(" ", "-")


def anchors_of(path):
    anchors = set()
    with open(path, encoding="utf-8") as handle:
        for line in handle:
            match = HEADING_RE.match(line.rstrip("\n"))
            if match:
                anchors.add(slugify(match.group(1)))
    return anchors


def main(argv):
    root = argv[1] if len(argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    files = sorted(
        name
        for name in os.listdir(root)
        if name.endswith(".md") and name != "MANIFEST.md"
    )
    anchor_cache = {}
    checked = 0
    broken = []

    for name in files:
        source_path = os.path.join(root, name)
        with open(source_path, encoding="utf-8") as handle:
            content = handle.read()
        for text, target in LINK_RE.findall(content):
            if "://" in target or target.startswith("mailto:") or target.startswith("#"):
                continue
            file_part, _, anchor = target.partition("#")
            if not file_part.endswith(".md"):
                continue
            checked += 1
            target_path = os.path.join(root, file_part)
            if not os.path.isfile(target_path):
                broken.append((name, text, target, "target file does not exist"))
                continue
            doc_match = DOC_TEXT_RE.match(text)
            file_match = DOC_FILE_RE.match(os.path.basename(file_part))
            if doc_match and file_match and int(doc_match.group(1)) != int(file_match.group(1)):
                broken.append(
                    (
                        name,
                        text,
                        target,
                        "link text says Doc %s but target is %s"
                        % (doc_match.group(1), os.path.basename(file_part)),
                    )
                )
                continue
            if anchor:
                if file_part not in anchor_cache:
                    anchor_cache[file_part] = anchors_of(target_path)
                if anchor not in anchor_cache[file_part]:
                    broken.append((name, text, target, "anchor not found in target file"))

    for name, text, target, reason in broken:
        print("%s: [%s](%s) - %s" % (name, text, target, reason))
    if broken:
        print("FAIL: %d broken reference(s) of %d links checked" % (len(broken), checked))
        return 1
    print("PASS: all references resolve (%d links checked)" % checked)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
