def extract_features(text):
    words = text.split()

    return {
        "length": len(words),
        "has_exposition": any(x in text.lower() for x in [
            "as you know", "previously on", "recap"
        ]),
        "dialogue_density": text.count('"') / max(len(text), 1),
        "repetition": len(set(words)) / max(len(words), 1)
    }
