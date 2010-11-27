from libraries.yellowapi.yellowExtendedAPI import *
import json
from libraries.yellowapi.settings import *
from libraries.geocode.geocode import *
from decimal import *

from opentable.models import *
ypAPI = YellowExtendedAPI(api_key=api_key)

def storeTheatresList(what="", theatres=[], where="montreal", uid=1):
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
        
        theatre = Theatre(name=listing['name'],
                            address = listing['address']['street'],
                            postal_code = listing['address']['pcode'],
                            lat = Decimal(listing['geoCode']['latitude']),
                            lon = Decimal(listing['geoCode']['longitude']))

        theatre.save()


if __name__ == "__main__":
    theatres = ["AMC Forum 22", "Banque Scotia", "Cinema Beaubien", "Cinema du Parc", "Quartier Latin"]
    theatreList = storeTheatresList(theatres=theatres)
    
