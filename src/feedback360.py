from dataclasses import dataclass
from typing import List

@dataclass
class Feedback:
    reviewer: str
    category: str  # leadership, communication, teamwork, delivery
    score: int  # 1-5
    comment: str = ""

def aggregate(feedbacks: List[Feedback]):
    by_cat = {}
    for f in feedbacks:
        by_cat.setdefault(f.category, []).append(f.score)
    return {cat: round(sum(s)/len(s), 2) for cat, s in by_cat.items()}
