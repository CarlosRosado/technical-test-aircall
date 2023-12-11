from typing import List
from escalation.entities import Level

class EscalationPolicy:
    def __init__(self):
        self.levels: List[Level] = []

    @property
    def get_levels(self) -> List[Level]:
        return self.levels

    @get_levels.setter
    def set_levels(self, levels: List[Level]):
        self.levels = levels
