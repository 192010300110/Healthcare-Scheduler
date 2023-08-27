## sms.py
import twilio
from twilio.rest import Client

class SMS:
    def __init__(self, account_sid: str, auth_token: str, from_number: str):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.from_number = from_number

    def send_confirmation_message(self, appointment: Appointment):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"Confirmation message: Your appointment with {appointment.provider_name} on {appointment.date} at {appointment.time} has been scheduled.",
            from_=self.from_number,
            to=appointment.patient_number
        )
        return message

    def send_reminder_message(self, appointment: Appointment):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(
            body=f"Reminder message: You have an appointment with {appointment.provider_name} on {appointment.date} at {appointment.time}.",
            from_=self.from_number,
            to=appointment.patient_number
        )
        return message
