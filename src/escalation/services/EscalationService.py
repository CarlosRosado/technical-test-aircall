from typing import List, Any
from src.escalation.adapters.abs.EPAdapterAbs import EPAdapterAbs
from src.escalation.entities import Level, Target
from src.escalation.services.abs.EscalationServiceAbs import EscalationServiceAbs


class EscalationService(EscalationServiceAbs):
    """
    Escalation policy service Class
    """

    def __init__(self, escalation_policy_adapter: EPAdapterAbs):
        self.escalation_policy_adapter = escalation_policy_adapter

    def get_target_by_service_and_level(self, service_id, level_id) -> List[Any]:
        """
        Get the target for the service and level
        :param service_id: service id
        :param level_id: level id
        :return list of targets
        """
        return self.escalation_policy_adapter.get_target_by_service_and_level(service_id, level_id)

    def get_levels_by_service(self, service_id) -> List[Any]:
        """
        Get all levels
        :param service_id: service id
        :return list of levels
        """
        return self.escalation_policy_adapter.get_levels_by_service(service_id)
