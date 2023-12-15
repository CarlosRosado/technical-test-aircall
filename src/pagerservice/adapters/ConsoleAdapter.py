from src.pagerservice.adapters.abs.ConsoleAdapterAbs import ConsoleAdapterAbs
from src.pagerservice.services.abs.PagerServiceAbs import PagerServiceAbs


class ConsoleAdapter(ConsoleAdapterAbs):
    """
    Class for Pager Web Console.
    """

    def __init__(self, pager_service: PagerServiceAbs):
        self.pager_service = pager_service

    def send_ack(self, service_id):
        """
        Function to notify with ACK
        :param service_id: service id
        """
        self.pager_service.notify_ack(service_id)

    def send_healthy_event(self, service_id):
        """
        Function to notify with health event
        :param service_id: service id
        """
        self.pager_service.notify_healthy_event(service_id)
