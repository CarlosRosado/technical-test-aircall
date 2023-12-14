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
from src.pagerservice.entities.MonitoredServiceStatus import MonitoredServiceStatus
from src.pagerservice.entities.MonitoredService import MonitoredService
from src.pagerservice.services.PagerService import PagerService
from datetime import datetime

SERVICE_ID = 1
FIRST_LEVEL = 1
TIMEOUT_ACK_MINUTES = 15
MESSAGE = "TEST MESSAGE 1"
AVAILABILITY_HOURS = [12, 17, 20]
CURRENT_TIME_OUT_OF_AVAILABILITY_HOURS = datetime(2021, 1, 1, 11, 0, 0)
CURRENT_TIME_WITHIN_AVAILABILITY_HOURS = datetime(2021, 1, 1, 12, 0, 0)


if __name__ == '__main__':
    sms_adapter = SMSAdapter()
    target_sms = TargetSMS(phone_number='658947898', sms_adapter=sms_adapter, availability_hours=AVAILABILITY_HOURS)
    email_adapter = EmailAdapter()
    target_email = TargetEmail(email_address="manuel@gmail.com", email_adapter=email_adapter, availability_hours=AVAILABILITY_HOURS)
    persistence_pager_adapter = PersistencePagerAdapter()
    escalation_service = EscalationServiceAbs()
    timer_adapter = TimerAdapter()
    pager_service = PagerService(escalation_service, persistence_pager_adapter, timer_adapter)

    alerting_adapter = AlertingAdapter(pager_service)

    CURRENT_TIME_WITHIN_AVAILABILITY_HOURS = datetime.now()

    target_email.send_notification(MESSAGE)
    target_sms.send_notification(MESSAGE)
    e_service = escalation_service.get_target_by_service_and_level(service_id=SERVICE_ID, level_id=FIRST_LEVEL)

    level = Level()
    level.id = FIRST_LEVEL
    level.targets = [target_email, target_sms]

    lev = escalation_service.get_levels_by_service(service_id=SERVICE_ID)

    #####################
    # Recieve alert
    #####################

    monitored_service = MonitoredService(id=SERVICE_ID, status=MonitoredServiceStatus.HEALTHY, id_level_notified=None, alert_message="")

    test_monitored = persistence_pager_adapter.get_monitored_service_by_id(SERVICE_ID)

    fake_target = [target_email, target_sms]
    t_service_level = escalation_service.get_target_by_service_and_level(SERVICE_ID, FIRST_LEVEL)

    alert_service = AlertService(service_id=SERVICE_ID, message=MESSAGE)

    monitored_service2 = MonitoredService(id=SERVICE_ID, status=MonitoredServiceStatus.PENDING_ACK, id_level_notified=FIRST_LEVEL, alert_message=MESSAGE)

    persistence_pager_adapter.save_monitored_service(monitored_service2)

    t1 = target_email.send_notification(MESSAGE)

    target_sms.send_notification(MESSAGE)
    timer_adapter.set_ack_timeout(SERVICE_ID, TIMEOUT_ACK_MINUTES)

    #####################
    # Recieve alert without availability
    #####################

    pager_service.set_current_local_datetime(CURRENT_TIME_OUT_OF_AVAILABILITY_HOURS)

    monitored_service = MonitoredService(id=SERVICE_ID, status=MonitoredServiceStatus.HEALTHY, id_level_notified=None, alert_message="")

    m_ser2 = persistence_pager_adapter.get_monitored_service_by_id(service_id=SERVICE_ID)

    t_l = escalation_service.get_target_by_service_and_level(service_id=SERVICE_ID, level_id=FIRST_LEVEL)

    alert_service = AlertService(service_id=SERVICE_ID, message=MESSAGE)

    persistence_pager_adapter.save_monitored_service(monitored_service)

    #####################
    # Recieve ack timeout
    #####################

    monitored_service = MonitoredService(id= SERVICE_ID, status=MonitoredServiceStatus.PENDING_ACK, id_level_notified=1, alert_message=MESSAGE)

    level_to_be_notified = monitored_service.id_level_notified + 1

    persistence_pager_adapter.save_monitored_service(monitored_service)

    get_ser_id = persistence_pager_adapter.get_monitored_service_by_id(service_id=SERVICE_ID)

    l_t_s = escalation_service.get_target_by_service_and_level(service_id=SERVICE_ID, level_id=FIRST_LEVEL)

    argument_persistence_adapter = persistence_pager_adapter.save_monitored_service(monitored_service)



