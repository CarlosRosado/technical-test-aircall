from enum import Enum

###
# Possible status for a monitored service
# HEALTHY: No alert
# PENDING_ACK: The ack timeout was sent but it was not expired yet
# ACKNOWLEDGED: There was an alert acknowledgment from the console. Someone is checking the alert
###

class MonitoredServiceStatus(Enum):
    HEALTHY = "HEALTHY"
    PENDING_ACK = "PENDING_ACK"
    ACKNOWLEDGED = "ACKNOWLEDGED"
