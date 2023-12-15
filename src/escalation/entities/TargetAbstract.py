from typing import List
from abc import ABC, abstractmethod


class TargetAbstract(ABC):
    """
    Abstract class for the target
    """

    def __init__(self):
        self.availability_hours: List[int] = []

    @abstractmethod
    def send_notification(self, message):
        """
        Send notification in the target
        :param message: Message to the target
        """
        pass

    def get_availability_hours(self) -> List[int]:
        """
        Get available hours
        :return list of available hours
        """
        return self.availability_hours

    def set_availability_hours(self, availability_hours: List[int]):
        """
        Set the availability hours in target
        :param availability_hours: list of available hours
        """
        self.availability_hours = availability_hours
