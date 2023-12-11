from pagerservice.adapters import ConsoleAdapter
from pagerservice.services import PagerService

class ConsoleAdapterImpl(ConsoleAdapter):
    def __init__(self, pager_service):
        self.pager_service = pager_service

    def send_ack(self, service_id):
        self.pager_service.notify_ack(service_id)

    def send_healthy_event(self, service_id):
        self.pager_service.notify_healthy_event(service_id)
