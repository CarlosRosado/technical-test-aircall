from pagerservice.adapters import PersistencePagerAdapter
from pagerservice.entities import MonitoredService


class PersistencePagerAdapterImpl(PersistencePagerAdapter):
    def get_monitored_service_by_id(self, service_id: int) -> MonitoredService:
        return None

    def save_monitored_service(self, monitored_service: MonitoredService):
        print("Monitored Service saved")
