from django.shortcuts import render
from geopy.geocoders import Photon
from geopy.distance import geodesic
from .forms import MeasurementForm
from .utils import get_geo, get_center_coordinates, get_zoom, get_ip_address
import folium

def calculate_distance_view(request):

    # Initializing Values:
    distance = None
    destination = None

    form = MeasurementForm(request.POST or None)
    geolocator = Photon(user_agent='geolocation_app')

    # Uncomment the following lines if you are hosting this app on a proper URL:
    # ip = get_ip_address(request)
    # print(ip)
    ip = '119.160.120.83'
    country, city, latitude, longitude = get_geo(ip)
    location = geolocator.geocode(city, timeout=10, exactly_one=True)

    # Current Location Co-ordinates:
    location_latitude = latitude
    location_longitude = longitude
    pointA = (location_latitude, location_longitude)

    # Initial Folium Map:
    map = folium.Map(location=get_center_coordinates(location_latitude, location_longitude), zoom_start=8)

    # Location Marker:
    folium.Marker([location_latitude, location_longitude], tooltip="Click here for more", popup=city['city'], icon=folium.Icon(color='blue')).add_to(map) 

    if form.is_valid():
        instance = form.save(commit=False)
        get_destination = form.cleaned_data.get('destination')
        destination = geolocator.geocode(get_destination, timeout=10, exactly_one=True)

        # Destination Co-ordinates:
        d_latitude = destination.latitude
        d_longitude = destination.longitude
        pointB = (d_latitude, d_longitude)

        # Distance Calculation:
        distance = round(geodesic(pointA, pointB).km, 2)

        # Folium Map Modification:
        map = folium.Map(location=get_center_coordinates(location_latitude, location_longitude, d_latitude, d_longitude), zoom_start=get_zoom(distance))

        # Location Marker:
        folium.Marker([location_latitude, location_longitude], tooltip="Click here for more", popup=city["city"], icon=folium.Icon(color='blue')).add_to(map)
        
        # Destination Marker:
        folium.Marker([d_latitude, d_longitude], tooltip="Click here for more", popup=destination, icon=folium.Icon(color='red', icon='cloud')).add_to(map)

        # Draw a line betweem Location and Destination Markers:
        line = folium.PolyLine(locations=[pointA, pointB], weight=1, color='blue')
        map.add_child(line)

        instance.location = location
        instance.distance = distance
        instance.save()

    map = map._repr_html_()

    context = {
        'distance': distance,
        'destination': destination,
        'form': form,
        'map': map,
    }

    return render(request,'home.html',context)
