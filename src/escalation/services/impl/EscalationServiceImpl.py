from typing import List
from escalation.adapters import EscalationPolicyAdapter
from escalation.entities import Level, Target
from escalation.services import EscalationService

class EscalationServiceImpl(EscalationService):
    def __init__(self, escalation_policy_adapter: EscalationPolicyAdapter):
        self.escalation_policy_adapter = escalation_policy_adapter

    def get_target_by_service_and_level(self, service_id: int, level_id: int) -> List[Target]:
        return self.escalation_policy_adapter.get_target_by_service_and_level(service_id, level_id)

    def get_levels_by_service(self, service_id: int) -> List[Level]:
        return self.escalation_policy_adapter.get_levels_by_service(service_id)
