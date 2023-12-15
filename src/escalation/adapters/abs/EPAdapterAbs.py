from abc import ABC, abstractmethod
from typing import List, Any


class EPAdapterAbs(ABC):
    """
    Methods used with the escalation policy service
    """

    @abstractmethod
    def get_target_by_service_and_level(self, service_id, level_id) -> List[Any]:
        """
        Get targets by service and level.

        :param service_id: service id
        :param level_id: level id
        :return: List of all targets
        """
        pass

    @abstractmethod
    def get_levels_by_service(self, service_id) -> List[Any]:
        """
        Get levels by service.

        :param service_id: service id
        :return: List of all Levels
        """
        pass
