from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")


def build_canon_embeddings(entries):
    by_char = {}

    for e in entries:
        by_char.setdefault(e.character, []).append(e.text)

    embeddings = {}

    for char, texts in by_char.items():
        embs = model.encode(texts)
        embeddings[char] = np.mean(embs, axis=0)

    return embeddings
