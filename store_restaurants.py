from libraries.yellowapi.yellowExtendedAPI import *
import json
from libraries.yellowapi.settings import *
from libraries.geocode.geocode import *
from decimal import *

from opentable.models import *
ypAPI = YellowExtendedAPI(api_key=api_key)

def storeRestaurantList(what="", where="H5A 1E4", uid=1, maxDistance=25.0):
    
    restaurants = json.loads(ypAPI.find_restaurant(what=what, where=where, uid=uid, maxDistance=maxDistance))
    count = 1
    for r in restaurants:
        print '%s. %s %s %s %s' % (count, r['name'], r['address']['street'], r['address']['city'], r['address']['pcode'])
        count+=1

        restaurant = Restaurant(capacity=100, 
                                num_reservations=0, 
                                name=r['name'], 
                                address=r['address']['street'], 
                                postal_code=r['address']['pcode'],
                                lat = Decimal(r['geoCode']['latitude']),
                                lon = Decimal(r['geoCode']['longitude']), 
                                )
        restaurant.save()

    # insert code to insert into db.
    return restaurants

if __name__ == "__main__":
    restaurants = storeRestarauntList()
    
