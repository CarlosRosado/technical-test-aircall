import unittest
from unittest.mock import Mock, patch
from src.escalation.entities import Level, TargetEmail, TargetSMS
from test.pagerservice.FakeFactory import FakeMonitoredService, FakeTarget, FakeLevel, FakeAlert
from src.pagerservice.adapters.impl import AlertingAdapterImpl, ConsoleAdapterImpl, TimerAdapterImpl
from src.pagerservice.adapters import PersistencePagerAdapter
from src.pagerservice.entities import MonitoredService, MonitoredServiceStatus
from src.pagerservice.services.impl import PagerServiceImpl
from src.pagerservice.adapters import TimerAdapter, AlertingAdapter, EscalationService


class PagerServiceTest(unittest.TestCase):

    SERVICE_ID = 1
    FIRST_LEVEL = 1
    TIMEOUT_ACK_MINUTES = 15
    MESSAGE = "TEST MESSAGE 1"

    def setUp(self):
        self.target_sms = Mock(spec=TargetSMS)
        self.target_email = Mock(spec=TargetEmail)
        self.persistence_pager_adapter = Mock(spec=PersistencePagerAdapter)
        self.escalation_service = Mock(spec=EscalationService)
        self.timer_adapter = Mock(spec=TimerAdapter)
        self.pager_service = PagerServiceImpl(self.escalation_service, self.persistence_pager_adapter, self.timer_adapter)
        self.alerting_adapter = AlertingAdapterImpl(self.pager_service)

        self.pager_service.set_current_local_date_time(FakeTarget.CURRENT_TIME_WITHIN_AVAILABILITY_HOURS)

        with patch.object(self.target_email, 'send_notification'):
            with patch.object(self.target_sms, 'send_notification'):
                with patch.object(self.escalation_service, 'get_target_by_service_and_level', return_value=FakeTarget.get_list_target_with_email_and_sms(self.target_email, self.target_sms)):
                    with patch.object(self.escalation_service, 'get_levels_by_service', return_value=FakeLevel.get_list_levels([self.target_email, self.target_sms])):
                        pass

    def test_receive_alert(self):
        monitored_service = FakeMonitoredService.get_monited_service_healthy_status(self.SERVICE_ID)
        self.persistence_pager_adapter.get_monitored_service_by_id.return_value = monitored_service
        self.escalation_service.get_target_by_service_and_level.return_value = FakeTarget.get_list_target_with_email_and_sms(self.target_email, self.target_sms)

        self.alerting_adapter.send_alert_to_pager(FakeAlert.get_fake_alert_service(self.SERVICE_ID, self.MESSAGE))

        self.persistence_pager_adapter.save_monitored_service.assert_called_once_with(MonitoredService(
            id=self.SERVICE_ID,
            status=MonitoredServiceStatus.PENDING_ACK,
            id_level_notified=self.FIRST_LEVEL,
            alert_message=self.MESSAGE
        ))
        self.target_email.send_notification.assert_called_once_with(self.MESSAGE)
        self.target_sms.send_notification.assert_called_once_with(self.MESSAGE)
        self.timer_adapter.set_ack_timeout.assert_called_once_with(self.SERVICE_ID, self.TIMEOUT_ACK_MINUTES)

    # Add other test methods for different scenarios...

if __name__ == '__main__':
    unittest.main()
