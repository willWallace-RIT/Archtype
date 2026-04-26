from dataclasses import dataclass, field
from typing import Optional, Dict, Any

@dataclass
class DialogueEntry:
    show: str
    character: str
    text: str
    source: str  # canon | fanfiction
    episode: Optional[str] = None

    # computed fields
    score: float = 0.0
    weight: float = 1.0

    metadata: Dict[str, Any] = field(default_factory=dict)
