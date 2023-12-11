from abc import ABC, abstractmethod

class SMSAdapter(ABC):

    @abstractmethod
    def send_sms(self, phone_number, message):
        pass
