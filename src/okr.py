from dataclasses import dataclass, field
from typing import List

@dataclass
class KeyResult:
    name: str
    target: float
    current: float = 0.0

    @property
    def progress(self):
        return min(self.current / self.target, 1.0) if self.target else 0

@dataclass
class Objective:
    title: str
    key_results: List[KeyResult] = field(default_factory=list)

    @property
    def progress(self):
        if not self.key_results:
            return 0
        return sum(kr.progress for kr in self.key_results) / len(self.key_results)
