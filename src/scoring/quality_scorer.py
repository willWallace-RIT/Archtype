import numpy as np
from sentence_transformers import SentenceTransformer
from feature_extractor import extract_features

model = SentenceTransformer("all-MiniLM-L6-v2")


def cosine(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


class QualityScorer:

    def __init__(self, canon_embeddings_by_character):
        self.canon_embeddings = canon_embeddings_by_character

    def score(self, entry):
        emb = model.encode(entry.text)

        canon_emb = self.canon_embeddings.get(entry.character)

        if canon_emb is None:
            return 0.3  # unknown character baseline

        similarity = cosine(emb, canon_emb)

        features = extract_features(entry.text)

        penalty = 0.0
        if features["has_exposition"]:
            penalty += 0.15
        if features["length"] > 40:
            penalty += 0.1

        return float(similarity - penalty)
