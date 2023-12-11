from escalation.adapters import SMSAdapter

class SMSAdapterImpl(SMSAdapter):
    def send_sms(self, phone_number, message):
        print(f"SMS sent properly to: {phone_number}")
