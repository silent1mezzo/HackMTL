"""
Cineti Python API Library

Requires Python 2.3+
Version 0.1
"""
import urllib2
import urllib
import itertools
import re
import json

from datetime import date, datetime, time

class CinetiAPI(object):

    URL = "http://api.cineti.ca"

    def __init__(self, api_key=None, format='json'):
        self.format = format
        self.url = "http://api.cineti.ca" 
    def get_all_theaters(self):
        """
            returns list of "name" / "href" pairs.

            eg {"name": "AMC Forum 22", "href": "http://api.cineti.ca/theater/amc"}
        """
        url = self._build_url(method='theaters')
        return self._perform_request(url)

    def get_all_movies(self):
        url = self._build_url(method='movies')
        return self._perform_request(url)

    def get_movies_at_theater(self, theater_url):
        url = "%s.%s" % (theater_url, self.format)
        return self._perform_request(url)

    def get_recommended_movies_at_theater(self, theater_url, startTime="00:00:00", limit=3):
        """ 
        given a start time (24hr clock), and theatre, this will return a subset of movie recommendations 
        limit of 3 to prevent decision paralysis? or more? dunno
        """ 

        if len(startTime) == 5:
            startTime = "%s:00" % startTime

        # for the purposes of this we'll assume we're using json
        results = self.get_movies_at_theater(theater_url)
        
        movies = json.loads(results)
        recommended = []
        for movie in movies.get('movies', []):
            for time in movie['times']:
                if time >= startTime:
                    movie['closestTime'] = time
                    recommended.append(movie)
                    break
        
        # sort by times
        movies = sorted(recommended, key=lambda k: k['times'])
        # limit
        return json.dumps(movies[0:limit])
        

    def _build_url(self, method, **kwargs):
        params = ["%s=%s" % (k,urllib.quote(str(v))) for (k,v) in itertools.ifilter(
            lambda (k,v): v is not None, kwargs.iteritems())]
        
        if params:
            params = "?%s" % ("&".join(params))
        url = "%s/%s.%s%s" % (self.url, method, self.format, "&".join(params))
        return url

    def _perform_request(self, url):
        resp = None
        try:
            resp = urllib2.urlopen(url)
            body = resp.read()
        except urllib2.HTTPError, err:
            if err.code == 400:
                msg = err.read()
                err.msg += "\n" + msg
            raise(err)
        finally:
            if resp:
                resp.close()
        return body
