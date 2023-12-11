from typing import List
from escalation.adapters import SMSAdapter
from escalation.entities import TargetAbstract

class TargetSMS(TargetAbstract):
    def __init__(self, phone_number, sms_adapter, availability_hours: List[int]):
        super().__init__()
        self.phone_number = phone_number
        self.sms_adapter = sms_adapter
        self.availability_hours = availability_hours

    def send_notification(self, message):
        self.sms_adapter.send_sms(self.phone_number, message)
