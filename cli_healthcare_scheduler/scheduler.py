from typing import List
from datetime import date, time
from database import Database
from sms import SMS
from diary import Diary
from dataclasses import dataclass

@dataclass
class Appointment:
    id: int
    patient_name: str
    provider_name: str
    date: date
    time: time

class Scheduler:
    def __init__(self, database: Database, sms: SMS):
        self.database = database
        self.sms = sms

    def schedule_appointment(self, patient_name: str, provider_name: str, date: date, time: time) -> Appointment:
        appointment = Appointment(None, patient_name, provider_name, date, time)
        created_appointment = self.database.create_appointment(appointment)
        self.sms.send_confirmation_message(created_appointment)
        return created_appointment

    def reschedule_appointment(self, appointment_id: int, new_date: date, new_time: time) -> Appointment:
        appointment = self.database.get_appointment(appointment_id)
        appointment.date = new_date
        appointment.time = new_time
        updated_appointment = self.database.update_appointment(appointment)
        return updated_appointment

    def cancel_appointment(self, appointment_id: int):
        appointment = self.database.get_appointment(appointment_id)
        self.database.delete_appointment(appointment_id)
        self.sms.send_cancellation_message(appointment)
