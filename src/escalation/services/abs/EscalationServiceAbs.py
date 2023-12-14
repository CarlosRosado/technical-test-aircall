from typing import List,Any


class EscalationServiceAbs:
    """
    Escalation policy service Abstract Class
    """

    def get_target_by_service_and_level(self, service_id, level_id) -> List[Any]:
        """
        Get the target for the service and level
        :param service_id: service id
        :param level_id: level id
        :return list of targets
        """
        pass

    def get_levels_by_service(self, service_id) -> List[Any]:
        """
        Get all levels
        :param service_id: service id
        :return list of levels
        """
        pass
