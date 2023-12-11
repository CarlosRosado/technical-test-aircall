from abc import ABC, abstractmethod
from pagerservice.entities import AlertService

class AlertingAdapter(ABC):
    """
    It contains the methods allowed to be used with the alerting service.
    """

    @abstractmethod
    def send_alert_to_pager(self, alert_service: AlertService):
        """
        Notify the pager about a new alert.

        :param alert_service: Alert information
        """
        pass
