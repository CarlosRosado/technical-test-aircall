from abc import ABC, abstractmethod


class SMSAdapterAbs(ABC):
    """
    Methods that can be used with the SMS Service
    """

    @abstractmethod
    def send_sms(self, phone_number, message):
        """
        Function used to send sms (message) to a specific phone number.

        Parameters:
        :param phone_number: Phone number
        :param message: Content to send
        """
        pass
