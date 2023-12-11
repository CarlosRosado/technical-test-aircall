from src.escalation.entities import Level, Target, TargetEmail, TargetSMS
from src.pagerservice.entities import AlertService, MonitoredService, MonitoredServiceStatus
from datetime import datetime
from typing import List

class FakeFactory:

    class FakeMonitoredService:

        @staticmethod
        def get_monitored_service_healthy_status(service_id):
            monitored_service = MonitoredService()
            monitored_service.id = service_id
            monitored_service.status = MonitoredServiceStatus.HEALTHY
            return monitored_service

        @staticmethod
        def get_monitored_service_unhealthy_status(service_id, message):
            monitored_service = MonitoredService()
            monitored_service.id = service_id
            monitored_service.status = MonitoredServiceStatus.PENDING_ACK
            monitored_service.id_level_notified = 1
            monitored_service.alert_message = message
            return monitored_service

        @staticmethod
        def get_monitored_service_unhealthy_status_with_level_notified(service_id, message, level_notified):
            monitored_service = MonitoredService()
            monitored_service.id = service_id
            monitored_service.status = MonitoredServiceStatus.PENDING_ACK
            monitored_service.id_level_notified = level_notified
            monitored_service.alert_message = message
            return monitored_service

        @staticmethod
        def get_monitored_service_unhealthy_status_with_ack():
            monitored_service = MonitoredService()
            monitored_service.id = 1
            monitored_service.status = MonitoredServiceStatus.ACKNOWLEDGED
            monitored_service.id_level_notified = 2
            return monitored_service

    class FakeTarget:

        AVAILABILITY_HOURS = [12, 17, 20]
        CURRENT_TIME_OUT_OF_AVAILABILITY_HOURS = datetime(2021, 1, 1, 11, 0, 0)
        CURRENT_TIME_WITHIN_AVAILABILITY_HOURS = datetime(2021, 1, 1, 12, 0, 0)

        @staticmethod
        def get_list_target_with_email_and_sms(target_email, target_sms):
            return [target_email, target_sms]

    class FakeLevel:

        @staticmethod
        def get_list_levels(targets):
            result = []
            result.append(FakeFactory.FakeLevel.get_level(1, targets))
            result.append(FakeFactory.FakeLevel.get_level(2, targets))
            result.append(FakeFactory.FakeLevel.get_level(3, targets))
            return result

        @staticmethod
        def get_level(level_id, targets):
            level = Level()
            level.id = level_id
            level.targets = targets
            return level

    class FakeAlert:

        @staticmethod
        def get_fake_alert_service(service_id, message):
            alert_service = AlertService()
            alert_service.service_id = service_id
            alert_service.message = message
            return alert_service