class AlertService:
    """
    Class for Alert Service
    """

    def __init__(self, service_id, message):
        self.service_id = service_id
        self.message = message

    @property
    def get_service_id(self):
        """
        Function to get service id
        :return service id
        """
        return self.service_id

    @property
    def set_service_id(self, service_id):
        """
        Function to set service id
        :param service_id: service id
        """
        self.service_id = service_id

    @property
    def get_message(self):
        """
        Function to get the message
        :return the message
        """
        return self.message

    @property
    def set_message(self, message):
        """
        Function to set the message
        :param message: the message to set
        """
        self.message = message
