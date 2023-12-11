from typing import List
from src.escalation.entities import Target

class Level:
    def __init__(self):
        self.id = 0
        self.targets: List[Target] = []

    @property
    def get_id(self) -> int:
        return self.id

    @get_id.setter
    def set_id(self, level_id: int):
        self.id = level_id

    @property
    def get_targets(self) -> List[Target]:
        return self.targets

    @get_targets.setter
    def set_targets(self, targets: List[Target]):
        self.targets = targets
