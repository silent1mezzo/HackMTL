import math
# a bunch of python geocode utilites

class Geocode(object):

    def __init__(self):
        pass

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        '''
        a = lat1 in radians, b = lat2 in radians, C = (lon2 - lon1) in radians
        reference: Spherical Law Of Cosines
        ''' 
        if lat1 == lat2 and lon1 == lon2:
            return 0

        delta = lon2 - lon1
        a = math.radians(lat1)
        b = math.radians(lat2)
        C = math.radians(delta)
        x = math.sin(a) * math.sin(b) + math.cos(a) * math.cos(b) * math.cos(C)
        distance = math.acos(x) # radians
        distance = math.degrees(distance) # in degrees
        distance = distance * 60 # 60 nautial miles / lat degree
        distance = distance * 1.852 # conversion to km 
        return distance
