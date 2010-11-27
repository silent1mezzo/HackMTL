from yellowapi import *
import json
import random

class YellowExtendedAPI(YellowAPI):
    def __init__(self, api_key, test_mode=True, format='JSON', handlers=[]):
        super(YellowExtendedAPI, self).__init__(api_key, test_mode, format, handlers)

    def find_restaurant(self, what, where, uid, page=None, page_len=None,
        sflag=None, lang=None, maxDistance=float(20.0), limit=20):

        what = "restaurant " + what
        resultsDict = json.loads(self.find_business(what,where,uid,page,page_len, sflag, lang))
        listings = resultsDict.get('listings')
        if not listings:
            return []

        results = []
        for listing in listings:
            if self._is_blacklisted(listing):
                continue
            if not listing.get('distance') or not listing['address'].get('pcode'):
                continue
            results.append(listing)
            if len(results) == 20:
                break
        return json.dumps(results)

    def _is_blacklisted(self, listing):
        filters = ['McDonalds', 'Burger King', 'Tim Hortons']
        for filter in filters:
            if listing.get('name').startswith(filter):
                return True

        return False
