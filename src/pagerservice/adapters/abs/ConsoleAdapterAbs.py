from abc import ABC, abstractmethod


class ConsoleAdapterAbs(ABC):
    """
    Abstract Class for Pager Web Console.
    """

    @abstractmethod
    def send_ack(self, service_id):
        """
        Function to notify with ACK
        :param service_id: service id
        """
        pass

    @abstractmethod
    def send_healthy_event(self, service_id):
        """
        Function to notify with health event
        :param service_id: service id
        """
        pass
