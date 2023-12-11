from abc import ABC, abstractmethod

class ConsoleAdapter(ABC):
    """
    It contains the methods that can be used with Pager Web Console
    """

    @abstractmethod
    def send_ack(self, service_id: int) -> None:
        """
        It will be used to notify the ACK from the Aircall engineer
        :param service_id: Monitored Service Id that has to be updated
        """
        pass

    @abstractmethod
    def send_healthy_event(self, service_id: int) -> None:
        """
        It will be used to notify a Healthy event from the Aircall engineer
        :param service_id: Monitored Service Id that has to be updated
        """
        pass
