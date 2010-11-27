from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
import settings

class Facility(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    address = models.TextField()
    postal_code = models.CharField(_('Postal Code'), max_length=7)
    phone_number = models.CharField(_('Phone Number'), max_length=15)
    lat = models.IntegerField()
    lon = models.IntegerField()
    
    class Meta:
        abstract = True

class Theatre(Facility):
    def __unicode__(self):
        return self.name

class Restaurant(Facility):
    capacity = models.IntegerField() 
    num_reservations = models.IntegerField(default=0)

    def __unicode__(self):
        return self.name


class Reservation(models.Model):
    name = models.CharField(_('Reservation Name'), max_length=255, editable=False)
    user = models.ForeignKey(User, editable=False)
    restaurant = models.ForeignKey(Restaurant)
    num_people = models.IntegerField(default=2)
    reservation_time = models.DateTimeField()
    reminder_time = models.DateTimeField(_('Notification Period'))
    notified = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
