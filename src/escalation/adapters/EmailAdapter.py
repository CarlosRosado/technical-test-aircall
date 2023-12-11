from abc import ABC, abstractmethod

class EmailAdapter(ABC):

    @abstractmethod
    def send_email(self, email_address, message):
        pass
