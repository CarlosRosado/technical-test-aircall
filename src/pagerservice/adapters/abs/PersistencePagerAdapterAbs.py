from abc import ABC, abstractmethod
from src.pagerservice.entities.MonitoredService import MonitoredService


class PersistencePagerAdapterAbs(ABC):
    """
    Abstract Class to manage the information from the Pager store system.
    """

    @abstractmethod
    def get_monitored_service_by_id(self, service_id) -> MonitoredService:
        """
        Get info for the monitored service
        :param service_id: service id
        :return monitored service
        """
        pass

    @abstractmethod
    def save_monitored_service(self, monitored_service: MonitoredService):
        """
        Save the monitored service
        :param monitored_service: monitored service to save
        """
        pass
