from abc import ABC, abstractmethod

class TimerAdapter(ABC):
    """
    It contains the methods that can be used with the Timer Service
    """

    @abstractmethod
    def set_ack_timeout(self, service_id: int, minutes: int) -> None:
        """
        It will be used to set an ACK timeout in the timer service
        :param service_id: Identifier of the monitored service
        :param minutes: Timeout duration in minutes
        """
        pass

    @abstractmethod
    def ack_expired(self, service_id: int) -> None:
        """
        It will be used to notify the Pager Service that ack timeout is expired
        :param service_id: Identifier of the monitored service
        """
        pass
