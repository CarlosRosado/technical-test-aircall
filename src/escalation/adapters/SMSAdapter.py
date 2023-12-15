from src.escalation.adapters.abs.SMSAdapterAbs import SMSAdapterAbs


class SMSAdapter(SMSAdapterAbs):
    """
    Methods that can be used with the SMS Service
    """

    def send_sms(self, phone_number, message):
        """
        Function used to send sms (message) to a specific phone number.

        Parameters:
        :param phone_number: Phone number
        :param message: Content to send
        :return Message for register message
        """
        print("SMS sent properly to: " + phone_number)
        return "SMS sent properly to: " + phone_number
