## diary.py
from typing import List
from database import Database
from dataclasses import dataclass

@dataclass
class Appointment:
    id: int
    patient_name: str
    provider_name: str
    date: str
    time: str

class Diary:
    def __init__(self, database: Database):
        self.database = database

    def view_appointments(self) -> List[Appointment]:
        return self.database.get_appointments()
