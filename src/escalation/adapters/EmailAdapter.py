from src.escalation.adapters.abs.EmailAdapterAbs import EmailAdapterAbs


class EmailAdapter(EmailAdapterAbs):
    """
    Methods that can be used with the Email Service
    """
    def send_email(self, email_address, message):
        """
        Function used to send email (message) to a specific email address.

        Parameters:
        :param email_address: Email address
        :param message: Content to send
        :return Message for register message
        """
        print("Email sent successfully to: " + email_address)
        return "Email sent successfully to: " + email_address
