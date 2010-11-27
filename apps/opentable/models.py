from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from libraries.geocode.geocode import *
import settings

class Facility(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    address = models.TextField()
    postal_code = models.CharField(_('Postal Code'), max_length=7)
    phone_number = models.CharField(_('Phone Number'), max_length=15, blank=True, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    
    class Meta:
        abstract = True

class Theatre(Facility):
    href = models.CharField(max_length=255, blank=True, null=True)
    def get_recommended_movies(self):
        pass
    def __unicode__(self):
        return self.name
    
class Restaurant(Facility):
    capacity = models.IntegerField() 
    num_reservations = models.IntegerField(default=0)

    def get_closest_theatre(self):
        geo = Geocode()
        closestThreatre = None
        minDiff = None
        for theatre in Theatre.objects.all():
            diff = geo.calculate_distance(self.lat, self.lon, theatre.lat, theatre.lon)
            if not minDiff or diff < minDiff:
                minDiff = diff
                closestTheatre = theatre
        return closestTheatre.name
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
