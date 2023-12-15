from typing import List
from src.escalation.adapters.abs.EmailAdapterAbs import EmailAdapterAbs
from src.escalation.entities.TargetAbstract import TargetAbstract  # Assuming TargetAbstract is in the same package or module


class TargetEmail(TargetAbstract):
    """
    Entity used to represent the target Email
    """

    def __init__(self, email_address, email_adapter: EmailAdapterAbs, availability_hours: List[int]):
        super().__init__()
        self.email_address = email_address
        self.email_adapter = email_adapter
        self.availability_hours = availability_hours

    def send_notification(self, message):
        """
        Send notification email
        :param message: message email
        """
        return self.email_adapter.send_email(self.email_address, message)
