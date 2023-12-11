from datetime import datetime
from pagerservice.entities import AlertService, MonitoredService, MonitoredServiceStatus
from pagerservice.adapters import PersistencePagerAdapter, TimerAdapter
from escalation.entities import Level
from escalation.entities.target import TargetAbstract
from escalation.services import EscalationService, EscalationServiceImpl
from pagerservice.adapters.impl import PersistencePagerAdapterImpl, TimerAdapterImpl
from typing import List
from itertools import chain
from functools import partial

class PagerServiceImpl:
    ACK_TIMEOUT_MINUTES_VALUE = 15

    def __init__(self, escalation_service=None, persistence_pager_adapter=None, timer_adapter=None):
        self.escalation_service = escalation_service or EscalationServiceImpl()
        self.persistence_pager_adapter = persistence_pager_adapter or PersistencePagerAdapterImpl()
        self.timer_adapter = timer_adapter or TimerAdapterImpl()
        self.current_local_date_time = None

    ####
    # @param alertService Service alert to be processed
    # @inheritDoc
    ####
    def notify_alert(self, alert_service: AlertService):
        monitored_service = self._get_monitored_service(alert_service.service_id)
        if self._is_healthy(monitored_service):
            self._send_notification_and_change_status(monitored_service, alert_service.message)
            self._send_timeout_delay(monitored_service.id)

    ####
    # @param serviceId Service alert id to be notified the timeout ack
    # @inheritDoc
    ####
    def notify_ack_timeout(self, service_id: int):
        monitored_service = self._get_monitored_service(service_id)
        if not self._is_acknowledged(monitored_service) and not self._is_healthy(monitored_service) \
                and not self._is_max_level(service_id, monitored_service.id_level_notified):
            self._send_notification_and_change_status(monitored_service, monitored_service.alert_message)
            self._send_timeout_delay(monitored_service.id)

    ####
    # @param serviceId Service alert id which will be marked as acknowledged
    # @inheritDoc
    ####
    def notify_ack(self, service_id: int):
        monitored_service = self._get_monitored_service(service_id)
        monitored_service.status = MonitoredServiceStatus.ACKNOWLEDGED
        self.persistence_pager_adapter.save_monitored_service(monitored_service)

    ####
    # @param serviceId Service alert id which will be marked as healthy
    # @inheritDoc
    ####
    def notify_healthy_event(self, service_id: int):
        monitored_service = self._get_monitored_service(service_id)
        monitored_service.status = MonitoredServiceStatus.HEALTHY
        monitored_service.id_level_notified = None
        monitored_service.alert_message = None
        self.persistence_pager_adapter.save_monitored_service(monitored_service)

    ####
    # It will user send to the time the Ack Timeout.
    #
    # @param serviceId Service alert id for which will be set the ack timeout
    ####
    def _send_timeout_delay(self, service_id: int):
        self.timer_adapter.set_ack_timeout(service_id, self.ACK_TIMEOUT_MINUTES_VALUE)

    ####
    # It will send the notification to the next level targets.
    # Also, it will set the right status {@link pagerservice.entities.MonitoredServiceStatus PENDING_ACK} with the alert message
    #
    # @param monitoredService Monitored service which has the alert
    # @param message          Alert message to be sent to the targets
    ####
    def _send_notification_and_change_status(self, monitored_service: MonitoredService, message: str):
        level_to_be_notified = self._get_level_id_to_be_notified(monitored_service)
        self._notify_targets(monitored_service, level_to_be_notified, message)

        monitored_service.status = MonitoredServiceStatus.PENDING_ACK
        monitored_service.id_level_notified = level_to_be_notified
        monitored_service.alert_message = message
        self.persistence_pager_adapter.save_monitored_service(monitored_service)

    ####
    # It will send the notification for each target.
    #
    # @param monitoredService  Monitored Service which has the alert
    # @param levelToBeNotified Target level which should receive the notifications
    # @param message           Alert message that has to be sent to the targets
    # @throws IllegalArgumentException if no target is retrieved for the level specified
    ####
    def _notify_targets(self, monitored_service: MonitoredService, level_to_be_notified: int, message: str):
        targets_to_be_notified = self.escalation_service.get_target_by_service_and_level(monitored_service.id, level_to_be_notified)

        if not targets_to_be_notified:
            raise ValueError(f"The target list to be notified for the serviceId {monitored_service.id} "
                             f"and levelId {level_to_be_notified} is not available.")

        for target in targets_to_be_notified:
            if self._is_available(target):
                target.send_notification(message)

    def _is_available(self, target: TargetAbstract):
        return any(hour == self._get_current_local_date_time().hour for hour in target.availailability_hours)

    ####
    # It will check if the current monitored service level is the maximum level available for the service passed
    #
    # @param serviceId            Service id for which will be calculated the maximum level
    # @param currentLevelNotified Last level that was notified for the service passed
    # @return True is current level is the maximum or False if not or the current level notified is null
    ####
    def _is_max_level(self, service_id: int, current_level_notified: int):
        if current_level_notified is None:
            return False

        levels = self.escalation_service.get_levels_by_service(service_id)
        max_level = max(levels, key=lambda x: x.id)
        return current_level_notified >= max_level.id

    ####
    # It will calculate the next level to be notified
    #
    # @param monitoredService Monitored Service which has the alert
    # @return It will sum one to the current notified level. If the current one is null it will initialize the level
    ####
    def _get_level_id_to_be_notified(self, monitored_service: MonitoredService):
        if monitored_service.id_level_notified is None:
            return 1
        return monitored_service.id_level_notified + 1

    def _is_healthy(self, monitored_service: MonitoredService):
        return monitored_service.status == MonitoredServiceStatus.HEALTHY

    def _is_acknowledged(self, monitored_service: MonitoredService):
        return monitored_service.status == MonitoredServiceStatus.ACKNOWLEDGED

    def _get_current_local_date_time(self):
        if self.current_local_date_time is None:
            self.current_local_date_time = datetime.now()
        return self.current_local_date_time

    def set_current_local_date_time(self, current_local_date_time):
        self.current_local_date_time = current_local_date_time

    def _get_monitored_service(self, service_id):
        monitored_service = self.persistence_pager_adapter.get_monitored_service_by_id(service_id)

        if monitored_service is None:
            raise ValueError(f"Monitored service with id {service_id} not found")

        return monitored_service

    def _get_escalation_service(self):
        if self.escalation_service is None:
            self.escalation_service = EscalationServiceImpl()
        return self.escalation_service

    def _get_persistence_pager_adapter(self):
        if self.persistence_pager_adapter is None:
            self.persistence_pager_adapter = PersistencePagerAdapterImpl()
        return self.persistence_pager_adapter

    def _get_timer_adapter(self):
        if self.timer_adapter is None:
            self.timer_adapter = TimerAdapterImpl()
        return self.timer_adapter
