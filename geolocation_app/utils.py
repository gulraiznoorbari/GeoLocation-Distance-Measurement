from django.contrib.gis.geoip2 import GeoIP2

# Helper functions for "geolocation_app/views.py"

def get_geo(ip):
    g = GeoIP2()
    country = g.country(ip)
    city = g.city(ip)
    latitude, logitude = g.lat_lon(ip)
    return country, city, latitude, logitude

def get_center_coordinates(latA, longA, latB=None, longB=None):
    coordinate = (latA, longA)
    if latB:
        coordinate = [(latA+latB)/2, (longA+longB)/2]
    return coordinate
      
def get_zoom(distance):
    if distance <= 500:
        return 8
    elif distance > 500 and distance <= 5000:
        return 4
    else:
        return 2

def get_ip_address(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
