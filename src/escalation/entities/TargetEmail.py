from typing import List
from escalation.adapters import EmailAdapter
from escalation.entities import TargetAbstract

class TargetEmail(TargetAbstract):
    def __init__(self, email_address, email_adapter, availability_hours: List[int]):
        super().__init__()
        self.email_address = email_address
        self.email_adapter = email_adapter
        self.availability_hours = availability_hours

    def send_notification(self, message):
        self.email_adapter.send_email(self.email_address, message)
