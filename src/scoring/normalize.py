import numpy as np

def normalize(entries):
    scores = np.array([e.score for e in entries])

    min_s, max_s = scores.min(), scores.max()

    for e in entries:
        e.weight = (e.score - min_s) / (max_s - min_s + 1e-8)

    return entries
