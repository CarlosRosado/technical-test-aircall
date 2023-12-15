from typing import List
from src.escalation.entities.Target import Target


class Level:
    """
    Levels for monitoring service
    """

    def __init__(self):
        self.id = 0
        self.targets = []

    def get_id(self) -> int:
        """
        Get if of Level
        :return id of level
        """
        return self.id

    def set_id(self, level_id: int):
        """
        Set id of Level
        :param level_id: id of the level
        """
        self.id = level_id

    def get_targets(self) -> List[Target]:
        """
        Get all target level
        :return list of target level
        """
        return self.targets

    def set_targets(self, targets: List[Target]):
        """
        Set target in level
        :param targets: list of targets
        """
        self.targets = targets

