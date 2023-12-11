from escalation.adapters import EmailAdapter

class EmailAdapterImpl(EmailAdapter):
    def send_email(self, email_address, message):
        print(f"Email sent successfully to: {email_address}")
