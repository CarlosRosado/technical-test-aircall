from typing import List
from src.escalation.adapters.abs.SMSAdapterAbs import SMSAdapterAbs
from src.escalation.entities.TargetAbstract import TargetAbstract  # Assuming TargetAbstract is in the same package or module


class TargetSMS(TargetAbstract):
    """
    Entity used to represent the target SMS
    """

    def __init__(self, phone_number, sms_adapter: SMSAdapterAbs, availability_hours: List[int]):
        super().__init__()
        self.phone_number = phone_number
        self.sms_adapter = sms_adapter
        self.availability_hours = availability_hours

    def send_notification(self, message):
        """
        Send notification SMS.
        :param message: message sms
        """
        return self.sms_adapter.send_sms(self.phone_number, message)
