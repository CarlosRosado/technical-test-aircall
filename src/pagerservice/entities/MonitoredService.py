
###
# Entity used to represent the different monitored services available
###

class MonitoredService:
    def __init__(self):
        self.id = 0
        self.status = None
        self.idLevelNotified = None
        self.alertMessage = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def get_id_level_notified(self):
        return self.idLevelNotified

    def set_id_level_notified(self, id_level_notified):
        self.idLevelNotified = id_level_notified

    def get_alert_message(self):
        return self.alertMessage

    def set_alert_message(self, alert_message):
        self.alertMessage = alert_message
