from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from libraries.geocode.geocode import *
import settings
from libraries.cineti.cineti import *
from libraries.cakemail import CakeRelay
from django.template.loader import render_to_string
from django.template import Context, Template
import json


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
    href = models.URLField(max_length=255, blank=True, null=True, verify_exists=False)
    def get_recommended_movies(self, start_time, limit):
        # returns a list of (movie_name, start_time) 
        cineti = CinetiAPI()
        resp = cineti.get_recommended_movies_at_theater(self.href, start_time=start_time, limit=limit)
        movieList= []
        if resp: 
            movies = json.loads(resp)
            for movie in movies:
                movieList.append((movie['title'], movie['closestTime']))

        return movieList

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
        return closestTheatre

    @models.permalink
    def get_absolute_url(self):
        return ('restaurant', (), {'restaurant_id': self.id})

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

    def notify_user(self):
        theatre = self.restaurant.get_closest_theatre() 
        movies = theatre.get_recommended_movies(start_time = (self.reservation_time + timedelta(hours=1.5)).strftime("%H:%s"), limit=3)
        movieText = u"" 
        counter = 1
        movie_stuff = {}
        for movie in movies: 
            movie_stuff['movie_name%s' % counter] = movie[0]
            movie_stuff['movie_time%s' % counter] = movie[1] 
            counter += 1
        template = Template('{{ movie_name1}} @ {{ movie_time1 }}<br />{{ movie_name2}} @ {{ movie_time2 }}<br />{{ movie_name3}} @ {{ movie_time3 }}<br />')
        movieText = template.render(Context(movie_stuff))

        dict = Context({
                    'name': self.user.first_name,
                    'restaurant': self.restaurant.name,
                    'date': self.reservation_time.strftime("%A %B %d %Y at %H:%m"),
                    'theatre_name': theatre.name,
                    'movies': movieText, 
                })
        # to define:
        params = {
            'user_key': settings.CAKEMAIL_USER_KEY,
            'email': self.user.email,
            'html_message': render_to_string('email_template.html', dict),
            'subject': 'Your reservation at %s for: %s' % (self.restaurant.name, self.reservation_time.strftime("%A %B %d %Y at %H:%m")),
            'sender_name': 'Ceviche Notifier',
            'sender_email': 'admin@ceviche.com',
        }
        CakeRelay.Send(params)
        self.notified = True
        self.save()
    def __unicode__(self):
        return '%s-%s' % (self.user.last_name, self.reservation_time)
