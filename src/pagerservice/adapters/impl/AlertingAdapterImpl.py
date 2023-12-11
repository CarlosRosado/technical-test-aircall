from pagerservice.adapters import AlertingAdapter
from pagerservice.entities import AlertService
from pagerservice.services import PagerService
from pagerservice.services.impl import PagerServiceImpl

class AlertingAdapterImpl(AlertingAdapter):
    def __init__(self, pager_service=None):
        self.pager_service = pager_service

    def send_alert_to_pager(self, alert_service):
        self.get_pager_service().notify_alert(alert_service)

    def get_pager_service(self):
        if self.pager_service is None:
            self.pager_service = PagerServiceImpl()
        return self.pager_service
