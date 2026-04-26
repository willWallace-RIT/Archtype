from parsing.parser import parse_script, save_jsonl
from scoring.quality_scorer import QualityScorer
from scoring.normalize import normalize
from modeling.embeddings import build_canon_embeddings
import json


def build(canon_data, fan_data):

    canon_entries = []
    fan_entries = []

    # parse canon
    for show, path in canon_data:
        canon_entries += parse_script(path, show, "canon")

    # parse fanfiction
    for show, path in fan_data:
        fan_entries += parse_script(path, show, "fanfiction")

    canon_embeddings = build_canon_embeddings(canon_entries)

    scorer = QualityScorer(canon_embeddings)

    all_entries = canon_entries + fan_entries

    for e in all_entries:
        if e.source == "canon":
            e.score = 1.0
        else:
            e.score = scorer.score(e)

    all_entries = normalize(all_entries)

    with open("processed/final_dataset.jsonl", "w") as f:
        for e in all_entries:
            f.write(json.dumps(e.__dict__) + "\n")
