from enum import Enum


class MonitoredServiceStatus(Enum):
    """
    Enum for Monitored Service Status
    HEALTHY: Healthy, not alarm
    PENDING_ACK: ACK send and pending to timeout
    ACKNOWLEDGED: alert ack from the console
    """
    HEALTHY = "HEALTHY"
    PENDING_ACK = "PENDING_ACK"
    ACKNOWLEDGED = "ACKNOWLEDGED"
