from abc import ABC, abstractmethod


class EmailAdapterAbs(ABC):
    """
    Methods that can be used with the Email Service
    """

    @abstractmethod
    def send_email(self, email_address, message):
        """
        Function used to send email (message) to a specific email address.

        Parameters:
        :param email_address: Email address
        :param message: Content to send
        """
        pass
