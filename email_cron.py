from opentable.models import *
from datetime import datetime
from time import sleep

def notify_users():
    reservations = Reservation.objects.filter(notified=False, reminder_time__lt=datetime.now()) 
    for reservation in reservations:
        reservation.notify_user()

if __name__ == "__main__":
    while(True):
        notify_users()
        sleep(30)
