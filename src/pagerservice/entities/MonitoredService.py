
class MonitoredService:
    """
    Class for Monitoring Service
    """

    def __init__(self, id, status, id_level_notified, alert_message):
        self.id = id
        self.status = status
        self.id_level_notified = id_level_notified
        self.alert_message = alert_message

    @property
    def get_id(self):
        """
        Function to get service id
        :return service id
        """
        return self.id

    @get_id.setter
    def set_id(self, id):
        """
        Function to set service id
        :param id: service id
        """
        self.id = id

    @property
    def get_status(self):
        """
        Function to get the status
        :return status
        """
        return self.status

    @get_status.setter
    def set_status(self, status):
        """
        Function to set the status
        :param status: status to set
        """
        self.status = status

    @property
    def get_id_level_notified(self):
        """
        Function to get id of level
        :return level id
        """
        return self.id_level_notified

    @get_id_level_notified.setter
    def set_id_level_notified(self, id_level_notified):
        """
        Function to set id of level
        :param id_level_notified: id of level
        """
        self.id_level_notified = id_level_notified

    @property
    def get_alert_message(self):
        """
        Function to set id of level
        :return id_level_notified: id of level
        """
        return self.alert_message

    @get_alert_message.setter
    def set_alert_message(self, alert_message):
        """
        Function to set the alert
        :param alert_message: alert message
        """
        self.alert_message = alert_message
