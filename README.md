Archtype
(chatgpt boilerplate)

---

# TV Character ML Framework

A general-purpose machine learning framework for analyzing TV show scripts and fanfiction through:

- Character consistency modeling  
- Dialogue quality scoring  
- Canon vs fanfiction comparison  
- Weighted dataset generation for ML training  

It is designed to work across **any scripted TV universe**, not just one show.

---

## 🧠 Core Idea

This project builds structured representations of characters from two sources:

- **Canon scripts** → ground-truth character behavior  
- **Fanfiction scripts** → user-generated interpretations  

Each line of dialogue is evaluated and assigned a **quality weight** based on how well it matches canonical character behavior and narrative quality standards.

These weights can then be used for:
- Machine learning training datasets  
- LLM fine-tuning  
- Character analysis research  
- Fandom interpretation studies  

---

## 📁 Project Structure

tv-character-ml-framework/ │ ├── data/ │   ├── raw/ │   │   ├── canon/ │   │   ├── fanfiction/ │ ├── processed/ │   ├── dialogues.jsonl │   ├── scored.jsonl │   ├── weighted.jsonl │   └── final_dataset.jsonl │ ├── src/ │   ├── parsing/ │   │   ├── parser.py │   │   ├── schema.py │   │ │   ├── scoring/ │   │   ├── feature_extractor.py │   │   ├── quality_scorer.py │   │   ├── normalize.py │   │ │   ├── modeling/ │   │   ├── embeddings.py │   │ │   ├── pipeline/ │   │   ├── build_dataset.py │ ├── configs/ │   ├── pipeline_config.yaml │ └── README.md

---

## ⚙️ Pipeline Overview

### 1. Data Ingestion
- Parse canon and fanfiction scripts into structured dialogue entries
- Normalize format across all shows

### 2. Canon Character Modeling
- Build embeddings from canon dialogue
- Establish baseline character behavior representations

### 3. Fanfiction Scoring
Each fanfiction line is evaluated using:

- Semantic similarity to canon behavior
- Dialogue quality heuristics
- Exposition / narrative noise detection

### 4. Weight Normalization
Scores are converted into usable training weights:

- Canon content → weight = 1.0  
- Fanfiction → weight ∈ [0, 1]  

### 5. Dataset Fusion
Canon and fanfiction are merged into a unified dataset for downstream ML use.

---

## 🧾 Data Schema

Each dialogue entry follows this structure:

```json
{
  "show": "show_name",
  "character": "CharacterName",
  "text": "Dialogue line here",
  "source": "canon | fanfiction",
  "episode": "optional_episode_id",
  "score": 0.0,
  "weight": 0.0,
  "metadata": {}
}
```

---

🧠 Scoring System

Fanfiction quality is computed using:

1. Character Similarity

Measures how closely a line matches canonical character behavior using embeddings.

2. Dialogue Features

Length penalties (overly verbose exposition)

Recap / meta-explanation detection

Repetition ratio

Dialogue density


3. Final Score

final_score = similarity_score - penalties

This score is then normalized into:

weight ∈ [0, 1]


---

🔗 Use Cases

📊 Research & Analysis

Character drift across fandoms

Interpretation bias in fanfiction communities

Narrative consistency measurement


🤖 Machine Learning

Fine-tuning LLMs on character-consistent datasets

Weighted training data pipelines

Persona-conditioned generation systems


🎮 Creative Tools

Character-aware story generation

Fanfiction quality scoring

Script rewriting assistants



---

🚀 Running the Pipeline

1. Install dependencies

pip install -r requirements.txt

2. Build dataset

python src/pipeline/build_dataset.py


---

🧪 Output

Final dataset is written to:

processed/final_dataset.jsonl

This contains:

Canon + fanfiction merged data

Character scores

Normalized weights

Training-ready structure



---

🔮 Future Extensions

Per-character fine-tuned language models

Multi-character interaction modeling

Episode-level narrative graph generation

Fandom clustering by interpretation style

Temporal drift tracking across fan communities



---

⚠️ Design Philosophy

This system does not treat fanfiction as incorrect.

Instead, it models:

> how interpretation diverges from canon and how strongly it aligns or deviates.



It is designed for analysis, not enforcement.


---

📌 License

MIT
