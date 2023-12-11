from pagerservice.adapters import TimerAdapter
from pagerservice.services import PagerService
from pagerservice.services.impl import PagerServiceImpl
from typing import Optional


class TimerAdapterImpl(TimerAdapter):
    def __init__(self, pager_service: Optional[PagerService] = None):
        self.pager_service = pager_service or PagerServiceImpl()

    def set_ack_timeout(self, service_id: int, minutes: int):
        print("The Ack timeout was sent to the timer service")

    def ack_expired(self, service_id: int):
        self.get_pager_service().notify_ack_timeout(service_id)

    def get_pager_service(self) -> PagerService:
        if not self.pager_service:
            self.pager_service = PagerServiceImpl()
        return self.pager_service
