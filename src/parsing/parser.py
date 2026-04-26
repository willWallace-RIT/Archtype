import json
import re
from schema import DialogueEntry

def parse_script(file_path, show, source, episode=None):
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    entries = []

    for line in text.split("\n"):
        match = re.match(r"(\w+): (.+)", line)
        if match:
            entries.append(
                DialogueEntry(
                    show=show,
                    character=match.group(1),
                    text=match.group(2),
                    source=source,
                    episode=episode
                )
            )

    return entries


def save_jsonl(entries, path):
    with open(path, "w") as f:
        for e in entries:
            f.write(json.dumps(e.__dict__) + "\n")
