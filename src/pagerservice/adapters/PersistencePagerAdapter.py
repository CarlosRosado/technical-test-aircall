from abc import ABC, abstractmethod
from typing import Optional

from entities import MonitoredService  # Make sure to import the MonitoredService class from the appropriate module

class PersistencePagerAdapter(ABC):
    """
    It contains the methods to manage the information from the Pager store system
    """

    @abstractmethod
    def get_monitored_service_by_id(self, service_id: int) -> Optional[MonitoredService]:
        """
        It will get the information related to the monitored service
        :param service_id: Identifier for the monitored service
        :return: the monitored service entity retrieved
        """
        pass

    @abstractmethod
    def save_monitored_service(self, monitored_service: MonitoredService) -> None:
        """
        It will store the information related to a monitored service
        :param monitored_service: monitored service entity to be stored
        """
        pass
