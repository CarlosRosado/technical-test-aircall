from abc import ABC, abstractmethod


class Target(ABC):
    """
    Target for monitoring service
    """

    @abstractmethod
    def send_notification(self, message):
        """
        Send notification of the target
        :param message: message in the target
        """
        pass
