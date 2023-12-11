from abc import ABC, abstractmethod
from typing import List
from escalation.entities import Level, Target

class EscalationPolicyAdapter(ABC):

    @abstractmethod
    def get_target_by_service_and_level(self, service_id, level_id) -> List[Target]:
        pass

    @abstractmethod
    def get_levels_by_service(self, service_id) -> List[Level]:
        pass
