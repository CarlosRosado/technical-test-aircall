from datetime import datetime
from src.pagerservice.entities.AlertService import AlertService
from src.pagerservice.entities.MonitoredServiceStatus import MonitoredServiceStatus

from src.pagerservice.adapters.abs.PersistencePagerAdapterAbs import PersistencePagerAdapterAbs
from src.pagerservice.adapters.PersistencePagerAdapter import PersistencePagerAdapter
from src.escalation.services.EscalationService import EscalationService
from src.escalation.services.abs.EscalationServiceAbs import EscalationServiceAbs
from src.pagerservice.services.abs.PagerServiceAbs import PagerServiceAbs
from src.pagerservice.adapters.TimerAdapter import TimerAdapter

from typing import Optional, Any


class PagerService(PagerServiceAbs):
    """
    Class to implement the Pager Service
    """
    ACK_TIMEOUT_MINUTES_VALUE = 15

    def __init__(self, escalation_service: Optional[Any] = None,
                 persistence_pager_adapter: Optional[Any] = None,
                 timer_adapter: Optional[Any] = None):
        self.escalation_service = escalation_service or EscalationServiceAbs()
        self.persistence_pager_adapter = persistence_pager_adapter or PersistencePagerAdapterAbs()
        self.timer_adapter = timer_adapter or TimerAdapter()
        self.current_local_datetime = None

    def notify_alert(self, alert_service: AlertService):
        """
        Function to receive an alert from Alerting Service
        :param alert_service: Service alert
        """
        monitored_service = self._get_monitored_service(alert_service.service_id)
        if self._is_healthy(monitored_service):
            self._send_notification_and_change_status(monitored_service, alert_service.message)
            self._send_timeout_delay(monitored_service.id)

    def notify_ack_timeout(self, service_id):
        """
        Function to receive the ack timeout from the Timer and send notification.
        :param service_id: service id to notify
        """
        monitored_service = self._get_monitored_service(service_id)
        if not self._is_acknowledged(monitored_service) and not self._is_healthy(monitored_service) \
                and not self._is_max_level(service_id, monitored_service.id_level_notified):
            self._send_notification_and_change_status(monitored_service, monitored_service.alert_message)
            self._send_timeout_delay(monitored_service.id)

    def notify_ack(self, service_id):
        """
        Notify with Ack status
        :param service_id: service id to notify
        """
        monitored_service = self._get_monitored_service(service_id)
        monitored_service.status = MonitoredServiceStatus.ACKNOWLEDGED
        self.persistence_pager_adapter.save_monitored_service(monitored_service)

    def notify_healthy_event(self, service_id):
        """
        Notify with healthy event to Console
        :param service_id: service id to notify
        """
        monitored_service = self._get_monitored_service(service_id)
        monitored_service.status = MonitoredServiceStatus.HEALTHY
        monitored_service.id_level_notified = None
        monitored_service.alert_message = None
        self.persistence_pager_adapter.save_monitored_service(monitored_service)

    def _send_timeout_delay(self, service_id):
        """
        Function to send the timeout delay
        :param service_id: service id
        """
        self.timer_adapter.set_ack_timeout(service_id, self.ACK_TIMEOUT_MINUTES_VALUE)

    def _send_notification_and_change_status(self, monitored_service, message):
        """
        Function to send the notification and change the status
        :param monitored_service: monitored service
        :param message: message to send
        """
        level_to_be_notified = self._get_level_id_to_be_notified(monitored_service)
        self._notify_targets(monitored_service, level_to_be_notified, message)

        monitored_service.status = MonitoredServiceStatus.PENDING_ACK
        monitored_service.id_level_notified = level_to_be_notified
        monitored_service.alert_message = message
        self.persistence_pager_adapter.save_monitored_service(monitored_service)

    def _notify_targets(self, monitored_service, level_to_be_notified, message):
        """
        Function to notify to all targets
        :param monitored_service: monitored service
        :param level_to_be_notified: level to be notified
        :param message: message to send
        """
        targets_to_be_notified = self.escalation_service.get_target_by_service_and_level(
            monitored_service.id, level_to_be_notified
        )

        if not targets_to_be_notified:
            raise ValueError(f"The target list to be notified for the serviceId {monitored_service.id} "
                             f"and levelId {level_to_be_notified} is not available.")

        for target in targets_to_be_notified:
            if self._is_available(target):
                target.send_notification(message)

    def _is_available(self, target):
        """
        Function to get if is available
        :param target: target
        :return the target availability
        """
        return target.availability_hours and self.current_local_datetime.hour in target.availability_hours

    def _is_max_level(self, service_id, current_level_notified):
        """
        Function to get if is max level
        :param service_id: service id
        :param current_level_notified: current level to notify
        :return the level or False
        """
        if current_level_notified is None:
            return False

        levels = self.escalation_service.get_levels_by_service(service_id)
        max_level = max(levels, key=lambda level: level.id)
        return current_level_notified >= max_level.id

    def _get_level_id_to_be_notified(self, monitored_service):
        """
        Function to get level if is notified
        :param monitored_service: monitored service
        :return get the level notified
        """
        if monitored_service.id_level_notified is None:
            return 1
        return monitored_service.id_level_notified + 1

    def _is_healthy(self, monitored_service):
        """
        Function to get if is healthy
        :param monitored_service: monitored service
        :return True if is healthy
        """
        return monitored_service.status == MonitoredServiceStatus.HEALTHY

    def _is_acknowledged(self, monitored_service):
        """
        Function to get if is Acknowledged
        :param monitored_service: monitored service
        :return True if is Acknowledged
        """
        return monitored_service.status == MonitoredServiceStatus.ACKNOWLEDGED

    def _get_current_local_datetime(self):
        """
        Function to get the current local datetime
        :return The current local datetime
        """
        if self.current_local_datetime is None:
            self.current_local_datetime = datetime.now()
        return self.current_local_datetime

    def set_current_local_datetime(self, current_local_datetime):
        """
        Function to set the current local datetime
        :param current_local_datetime: The current local datetime
        """
        self.current_local_datetime = current_local_datetime

    def _get_monitored_service(self, service_id):
        """
        Function to get the monitored service
        :param service_id: service id
        :return the monitored service
        """
        monitored_service = self.persistence_pager_adapter.get_monitored_service_by_id(service_id)

        if monitored_service is None:
            raise ValueError(f"Monitored service with id {service_id} not found")

        return monitored_service

    def _get_escalation_service(self):
        """
        Function to get the escalation service
        :return the escalation service
        """
        if self.escalation_service is None:
            self.escalation_service = EscalationService()
        return self.escalation_service

    def _get_persistence_pager_adapter(self):
        """
        Function to get the persistence pager adapter
        :return the service pager adapter
        """
        if self.persistence_pager_adapter is None:
            self.persistence_pager_adapter = PersistencePagerAdapter()
        return self.persistence_pager_adapter

    def _get_timer_adapter(self):
        """
        Function to get the timer adapter
        :return the timer adapter
        """
        if self.timer_adapter is None:
            self.timer_adapter = TimerAdapter()
        return self.timer_adapter
