from abc import ABC, abstractmethod

class Target(ABC):

    @abstractmethod
    def send_notification(self, message):
        pass
