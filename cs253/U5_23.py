
from collections import namedtuple

# make a basic Point class
Point = namedtuple('Point', ["lat", "lon"])
points = [Point(1,2),
          Point(3,4),
          Point(5,6)]

# implement the function gmaps_img(points) that returns the google maps image
# for a map with the points passed in. A example valid response looks like
# this:
#
# http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&markers=1,2&marker=3,4
#
# Note that you should be able to get the first and second part of an individual Point p with
# p.lat and p.lon, respectively, based on the above code. For example, points[0].lat would 
# return 1, while points[2].lon would return 6.

GMAPS_URL = "http://maps.googleapis.com/maps/api/staticmap?size=380x263&sensor=false&"

def gmaps_img(points):
    result = ''
    for point in points:
        result += '&markers=' + str(point.lat) + ',' + str(point.lon)
    result = GMAPS_URL + result[1:]
    return result


def gmaps_img2(points):
    markers = '&'.join('markers=%s,%s' % (p.lat , p.lon) for p in points)
    return GMAPS_URL + markers

print gmaps_img(points)
    ###Your code here

print gmaps_img2(points)
