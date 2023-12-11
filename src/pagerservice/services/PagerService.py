from abc import ABC, abstractmethod
from pagerservice.entities import AlertService

###
# Service with the logic to manage the Pager Service
###
class PagerService(ABC):

    ###
    # It will receive an alert from Alerting Service and it will notify
    # to the right target only if the monitored service was healthy.
    # @param alertService Service alert to be processed
    ###
    @abstractmethod
    def notify_alert(self, alert_service: AlertService):
        pass

    ###
    # It will receive the acknowledgment timeout from the Timer. If needed (no healthy and not acknowledged) it will notify the next target level.
    # If the notification was already sent to the last level, nothing will be done.
    # @param serviceId Service alert id to be notified the timeout ack
    ###
    @abstractmethod
    def notify_ack_timeout(self, service_id: int):
        pass

    ###
    # It will process the acknowledgement from the console. It will be hold on the acknowledged status.
    # @param serviceId Service alert id which will be marked as acknowledged
    ###
    @abstractmethod
    def notify_ack(self, service_id: int):
        pass

    ###
    # It will process an healthy event from the console.
    # @param serviceId Service alert id which will be marked as healthy
    ###
    @abstractmethod
    def notify_healthy_event(self, service_id: int):
        pass