import click
from datetime import datetime
from scheduler import Scheduler
from diary import Diary
from database import Database
from sms import SMS

@click.group()
def cli():
    pass

@cli.command()
@click.option("--patient-name", type=str, required=True, help="Name of the patient")
@click.option("--provider-name", type=str, required=True, help="Name of the provider")
@click.option("--date", type=str, required=True, help="Date of the appointment (YYYY-MM-DD)")
@click.option("--time", type=str, required=True, help="Time of the appointment (HH:MM)")
def schedule_appointment(patient_name: str, provider_name: str, date: str, time: str):
    scheduler = Scheduler(Database("appointments.db"), SMS("account_sid", "auth_token", "from_number"))
    appointment = scheduler.schedule_appointment(patient_name, provider_name, date, time)
    click.echo(f"Appointment scheduled: {appointment.id}, {appointment.patient_name}, {appointment.provider_name}, {appointment.date}, {appointment.time}")

@cli.command()
@click.option("--appointment-id", type=int, required=True, help="ID of the appointment to reschedule")
@click.option("--new-date", type=str, required=True, help="New date of the appointment (YYYY-MM-DD)")
@click.option("--new-time", type=str, required=True, help="New time of the appointment (HH:MM)")
def reschedule_appointment(appointment_id: int, new_date: str, new_time: str):
    scheduler = Scheduler(Database("appointments.db"), SMS("account_sid", "auth_token", "from_number"))
    appointment = scheduler.reschedule_appointment(appointment_id, new_date, new_time)
    click.echo(f"Appointment rescheduled: {appointment.id}, {appointment.patient_name}, {appointment.provider_name}, {appointment.date}, {appointment.time}")

@cli.command()
@click.option("--appointment-id", type=int, required=True, help="ID of the appointment to cancel")
def cancel_appointment(appointment_id: int):
    scheduler = Scheduler(Database("appointments.db"), SMS("account_sid", "auth_token", "from_number"))
    scheduler.cancel_appointment(appointment_id)
    click.echo("Appointment cancelled")

@cli.command()
def view_appointments():
    diary = Diary(Database("appointments.db"))
    appointments = diary.view_appointments()
    for appointment in appointments:
        click.echo(f"Appointment: {appointment.id}, {appointment.patient_name}, {appointment.provider_name}, {appointment.date}, {appointment.time}")

if __name__ == "__main__":
    cli()
