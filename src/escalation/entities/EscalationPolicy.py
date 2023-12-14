from typing import List

from src.escalation.entities.Level import Level


class EscalationPolicy:
    """
    Entity that represents the information that will manage the escalation policy service
    """

    def __init__(self):
        self.levels = []

    def get_levels(self) -> List[Level]:
        """
        Get all levels.
        :return A list of Level objects.
        """
        return self.levels

    def set_levels(self, levels: List[Level]):
        """
        Sets the levels.
        :param levels: list of Level objects.
        """
        self.levels = levels
