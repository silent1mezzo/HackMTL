from libraries.yellowapi.yellowExtendedAPI import *
import json
from libraries.yellowapi.settings import *
from libraries.geocode.geocode import *
from decimal import *

from opentable.models import *
ypAPI = YellowExtendedAPI(api_key=api_key)

def grabRestaurantList(what="", where="H5A 1E4", uid=1, maxDistance=25.0):
    
    restaurants = json.loads(ypAPI.find_restaurant(what=what, where=where, uid=uid, maxDistance=maxDistance))
    count = 1
    for r in restaurants:
        print '%s. %s %s %s %s' % (count, r['name'], r['address']['street'], r['address']['city'], r['address']['pcode'])
        count+=1

        restaurant = Restaurant(capacity=100, num_reservations=0, name=r['name'], address=r['address']['street'], postal_code=r['address']['pcode'])
        restaurant.save()

    # insert code to insert into db.
    return restaurants

def grabTheatresList(what="", theatres=[], where="montreal", uid=1):
    theatreListing = []
    for theatre in theatres:
        print '--'
        print theatre
        theatreInfo = json.loads(ypAPI.find_business(what=theatre, where=where, uid=uid))

        listing = theatreInfo.get('listings', None)[0]
        print listing['name']
        print listing['address']['street']
        print listing['address']['city']
        print listing['address']['pcode']
        print listing['geoCode']['latitude']
        print listing['geoCode']['longitude']
        theatreListing.append(listing)
        
        ## insert code to insert into db.


    return theatreListing
def grabDistances(restaurants, theatres):

    geoCodeObj = Geocode()
    
    for restaurant in restaurants:
        print restaurant['name']
        lat1 = Decimal(restaurant['geoCode']['latitude'])
        lon1 = Decimal(restaurant['geoCode']['longitude'])
        print lat1, lon1
        grabClosestTheatre(lat1, lon1, theatres)

def grabClosestTheatre(lat1, lon1, theatres):         
    
    geoCodeObj = Geocode()
    
    closestTheatre = None
    minDiff = None
    for theatre in theatres:
        lat2 = Decimal(theatre['geoCode']['latitude'])
        lon2 = Decimal(theatre['geoCode']['longitude'])
        print lat2, lon2 

        diff = geoCodeObj.calculate_distance(lat1, lon1, lat2, lon2)
        print 'this is the diff: ', diff
        if not minDiff or diff < minDiff:
            minDiff = diff
            closestTheatre = theatre 
    
    print '%s is closest.' % theatre['name']                    

if __name__ == "__main__":
    #theatres = ["AMC Forum 22", "Banque Scotia", "Cinema Beaubien", "Cinema du Parc", "Quartier Latin"]
    #theatreList = grabTheatresList(theatres=theatres)
    restaurants = grabRestaurantList()
    #print theatreList
    #distances = grabDistances(restaurants, theatreList)
    
