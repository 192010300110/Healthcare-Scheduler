"""
Rewritten code with improvements:
- Added type hints to function parameters and return values.
- Used context managers for database connection to ensure proper handling of resources.
- Simplified the code by using list comprehension to create Appointment objects.
- Renamed the `db_file` parameter to `db_path` for clarity.
"""

import sqlite3
from typing import List

class Appointment:
    def __init__(self, id: int, patient_name: str, provider_name: str, date: str, time: str):
        self.id = id
        self.patient_name = patient_name
        self.provider_name = provider_name
        self.date = date
        self.time = time

class Database:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def create_appointment(self, appointment: Appointment) -> Appointment:
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO appointments (patient_name, provider_name, date, time) VALUES (?, ?, ?, ?)",
                      (appointment.patient_name, appointment.provider_name, appointment.date, appointment.time))
            appointment_id = c.lastrowid
            conn.commit()
        return Appointment(appointment_id, appointment.patient_name, appointment.provider_name, appointment.date, appointment.time)

    def update_appointment(self, appointment: Appointment) -> Appointment:
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("UPDATE appointments SET patient_name = ?, provider_name = ?, date = ?, time = ? WHERE id = ?",
                      (appointment.patient_name, appointment.provider_name, appointment.date, appointment.time, appointment.id))
            conn.commit()
        return appointment

    def delete_appointment(self, appointment_id: int):
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
            conn.commit()

    def get_appointments(self) -> List[Appointment]:
        with sqlite3.connect(self.db_path) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM appointments")
            rows = c.fetchall()
        appointments = [Appointment(row[0], row[1], row[2], row[3], row[4]) for row in rows]
        return appointments
