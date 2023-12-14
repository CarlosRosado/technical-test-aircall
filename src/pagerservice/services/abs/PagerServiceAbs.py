from abc import ABC, abstractmethod


class PagerServiceAbs(ABC):
    """
    Abstract Class to implement the Pager Service
    """

    @abstractmethod
    def notify_alert(self, alert_service):
        """
        Function to receive an alert from Alerting Service
        :param alert_service: Service alert
        """
        pass

    @abstractmethod
    def notify_ack_timeout(self, service_id):
        """
        Function to receive the ack timeout from the Timer and send notification.
        :param service_id: service id to notify
        """
        pass

    @abstractmethod
    def notify_ack(self, service_id):
        """
        Notify with Ack status
        :param service_id: service id to notify
        """
        pass

    @abstractmethod
    def notify_healthy_event(self, service_id):
        """
        Notify with healthy event to Console
        :param service_id: service id to notify
        """
        pass
