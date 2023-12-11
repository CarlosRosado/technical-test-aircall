from typing import List
from escalation.entities import Target

class TargetAbstract(Target):
    def __init__(self):
        self.availability_hours: List[int] = []

    @property
    def get_availability_hours(self) -> List[int]:
        return self.availability_hours

    @get_availability_hours.setter
    def set_availability_hours(self, availability_hours: List[int]):
        self.availability_hours = availability_hours

    def send_notification(self, message):
        # Implement the abstract method
        pass
