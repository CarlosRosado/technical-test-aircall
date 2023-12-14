from abc import ABC, abstractmethod


class TimerAdapterAbs(ABC):
    """
    Abstract Class for Timer Service.
    """

    @abstractmethod
    def set_ack_timeout(self, service_id, minutes):
        """
        Set the ACK timeout
        :param service_id: service id
        :param minutes: minutes to ack
        """
        pass

    @abstractmethod
    def ack_expired(self, service_id):
        """
        Notified to Pager Service that ACK has expired
        :param service_id: service id
        """
        pass
