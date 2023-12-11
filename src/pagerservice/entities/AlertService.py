###
# Entity that will be used by the alert service to notify the alerts
###

class AlertService:
    def __init__(self):
        self.service_id = 0
        self.message = ""

    @property
    def service_id(self):
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        self._service_id = service_id

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message
