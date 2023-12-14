from datetime import datetime
import unittest

from src.escalation.adapters.EmailAdapter import EmailAdapter
from src.escalation.adapters.SMSAdapter import SMSAdapter
from src.escalation.entities.Level import Level
from src.escalation.entities.TargetEmail import TargetEmail
from src.escalation.entities.TargetSMS import TargetSMS
from src.escalation.services.abs.EscalationServiceAbs import EscalationServiceAbs
from src.pagerservice.adapters.AlertingAdapter import AlertingAdapter
from src.pagerservice.adapters.PersistencePagerAdapter import PersistencePagerAdapter
from src.pagerservice.adapters.TimerAdapter import TimerAdapter
from src.pagerservice.entities.AlertService import AlertService
from src.pagerservice.entities.MonitoredService import MonitoredService
from src.pagerservice.entities.MonitoredServiceStatus import MonitoredServiceStatus
from src.pagerservice.services.PagerService import PagerService


class PagerServiceTest(unittest.TestCase):
    SERVICE_ID = 1
    FIRST_LEVEL = 1
    TIMEOUT_ACK_MINUTES = 15
    MESSAGE = "TEST MESSAGE 1"
    AVAILABILITY_HOURS = [12, 17, 20]
    CURRENT_TIME_OUT_OF_AVAILABILITY_HOURS = datetime(2021, 1, 1, 11, 0, 0)
    CURRENT_TIME_WITHIN_AVAILABILITY_HOURS = datetime(2021, 1, 1, 12, 0, 0)

    def setUp(self):
        self.sms_adapter = SMSAdapter()
        self.target_sms = TargetSMS(phone_number='658947898', sms_adapter=self.sms_adapter, availability_hours=self.AVAILABILITY_HOURS)
        self.email_adapter = EmailAdapter()
        self.target_email = TargetEmail(email_address="manuel@gmail.com", email_adapter=self.email_adapter,
                                   availability_hours=self.AVAILABILITY_HOURS)
        self.persistence_pager_adapter = PersistencePagerAdapter()
        self.escalation_service = EscalationServiceAbs()
        self.timer_adapter = TimerAdapter()
        self.pager_service = PagerService(self.escalation_service, self.persistence_pager_adapter, self.timer_adapter)

        self.alerting_adapter = AlertingAdapter(self.pager_service)

        self.CURRENT_TIME_WITHIN_AVAILABILITY_HOURS = datetime.now()

        self.target_email.send_notification(self.MESSAGE)
        self.target_sms.send_notification(self.MESSAGE)
        self.e_service = self.escalation_service.get_target_by_service_and_level(service_id=self.SERVICE_ID, level_id=self.FIRST_LEVEL)

        self.level = Level()
        self.level.id = self.FIRST_LEVEL
        self.level.targets = [self.target_email, self.target_sms]

        self.lev = self.escalation_service.get_levels_by_service(service_id=self.SERVICE_ID)

    def test_receive_alert(self):
        monitored_service = MonitoredService(id=self.SERVICE_ID, status=MonitoredServiceStatus.HEALTHY,
                                             id_level_notified=None, alert_message="")

        test_monitored = self.persistence_pager_adapter.get_monitored_service_by_id(self.SERVICE_ID)

        fake_target = [self.target_email, self.target_sms]
        t_service_level = self.escalation_service.get_target_by_service_and_level(self.SERVICE_ID, self.FIRST_LEVEL)

        alert_service = AlertService(service_id=self.SERVICE_ID, message=self.MESSAGE)

        monitored_service2 = MonitoredService(id=self.SERVICE_ID, status=MonitoredServiceStatus.PENDING_ACK,
                                              id_level_notified=self.FIRST_LEVEL, alert_message=self.MESSAGE)

        self.persistence_pager_adapter.save_monitored_service(monitored_service2)

        self.assertEqual(self.target_email.send_notification(self.MESSAGE), 'Email sent successfully to: manuel@gmail.com')
        self.assertEqual(self.target_sms.send_notification(self.MESSAGE), 'SMS sent properly to: 658947898')
        self.assertEqual(self.timer_adapter.set_ack_timeout(self.SERVICE_ID, self.TIMEOUT_ACK_MINUTES), "The Ack timeout was sent to the timer service")

    def test_receive_alert_but_target_no_availability(self):

        self.pager_service.set_current_local_datetime(self.CURRENT_TIME_OUT_OF_AVAILABILITY_HOURS)

        monitored_service = MonitoredService(id=self.SERVICE_ID, status=MonitoredServiceStatus.HEALTHY,
                                             id_level_notified=1, alert_message=self.MESSAGE)

        m_ser2 = self.persistence_pager_adapter.get_monitored_service_by_id(service_id=self.SERVICE_ID)

        t_l = self.escalation_service.get_target_by_service_and_level(service_id=self.SERVICE_ID, level_id=self.FIRST_LEVEL)

        alert_service = AlertService(service_id=self.SERVICE_ID, message=self.MESSAGE)

        self.persistence_pager_adapter.save_monitored_service(monitored_service)

        self.assertEqual(self.SERVICE_ID, monitored_service.id)
        self.assertEqual(MonitoredServiceStatus.HEALTHY, monitored_service.status)

        self.assertEqual(self.FIRST_LEVEL, monitored_service.id_level_notified)

        self.assertEqual(self.MESSAGE, monitored_service.alert_message)

    def test_receive_ack_timeout(self):

        monitored_service = MonitoredService(id=self.SERVICE_ID, status=MonitoredServiceStatus.PENDING_ACK,
                                             id_level_notified=1, alert_message=self.MESSAGE)

        level_to_be_notified = monitored_service.id_level_notified + 1

        self.persistence_pager_adapter.save_monitored_service(monitored_service)

        get_ser_id = self.persistence_pager_adapter.get_monitored_service_by_id(service_id=self.SERVICE_ID)

        l_t_s = self.escalation_service.get_target_by_service_and_level(service_id=self.SERVICE_ID, level_id=self.FIRST_LEVEL)

        self.assertEqual(self.SERVICE_ID, monitored_service.id)
        self.assertEqual(MonitoredServiceStatus.PENDING_ACK, monitored_service.status)

        self.assertEqual(self.FIRST_LEVEL, monitored_service.id_level_notified)

        self.assertEqual(self.MESSAGE, monitored_service.alert_message)


if __name__ == '__main__':
    unittest.main()
