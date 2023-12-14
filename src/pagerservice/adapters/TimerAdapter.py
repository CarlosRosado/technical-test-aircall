from src.pagerservice.adapters.abs.TimerAdapterAbs import TimerAdapterAbs
from src.pagerservice.services.abs.PagerServiceAbs import PagerServiceAbs
from typing import Optional


class TimerAdapter(TimerAdapterAbs):
    """
    Class for Timer Service.
    """

    def __init__(self, pager_service: Optional[PagerServiceAbs] = None):
        self.pager_service = pager_service

    def set_ack_timeout(self, service_id, minutes):
        """
        Set the ACK timeout
        :param service_id: service id
        :param minutes: minutes to ack
        :return the OK message
        """
        print("The Ack timeout was sent to the timer service")
        return "The Ack timeout was sent to the timer service"

    def ack_expired(self, service_id):
        """
        Notified to Pager Service that ACK has expired
        :param service_id: service id
        """
        self.get_pager_service().notify_ack_timeout(service_id)

    def get_pager_service(self) -> PagerServiceAbs:
        """
        Get Pager Service Associated
        :return pager service instance
        """
        if not self.pager_service:
            self.pager_service = PagerService()
        return self.pager_service
