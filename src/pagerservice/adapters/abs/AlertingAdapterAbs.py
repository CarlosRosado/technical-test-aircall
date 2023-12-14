from abc import ABC, abstractmethod
from src.pagerservice.entities.AlertService import AlertService


class AlertingAdapterAbs(ABC):
    """
    Abstract Class for Alerting service
    """

    @abstractmethod
    def send_alert_to_pager(self, alert_service: AlertService):
        """
        Function to notify with alert to the pager service
        :param alert_service: Alert info
        """
        pass
