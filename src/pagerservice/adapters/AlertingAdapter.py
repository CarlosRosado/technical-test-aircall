from src.pagerservice.adapters.abs.AlertingAdapterAbs import AlertingAdapterAbs
from src.pagerservice.entities.AlertService import AlertService
from src.pagerservice.services.abs.PagerServiceAbs import PagerServiceAbs
from src.pagerservice.services.PagerService import PagerService
from typing import Optional


class AlertingAdapter(AlertingAdapterAbs):
    """
    Class for Alerting service
    """

    def __init__(self, pager_service: Optional[PagerServiceAbs] = None):
        self.pager_service = pager_service

    def send_alert_to_pager(self, alert_service: AlertService):
        """
        Function to notify with alert to the pager service
        :param alert_service: Alert info
        """
        self.get_pager_service().notify_alert(alert_service)

    def get_pager_service(self) -> PagerServiceAbs:
        """
        Get the pager service function
        :return the pager service
        """
        if not self.pager_service:
            self.pager_service = PagerService()
        return self.pager_service
