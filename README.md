<div align="center">
<h1>Geo-Location Distance Measurement</h1>
<h4>Geo-Location Distance Measurement App made with Folium(Leaflet.js) and Django.</h4>
<img src="demo.png">    
<br>
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25.gif" border="0" alt="Made with Django." title="Made with Django." /></a>
</div>

## Functionalities
- [x] Calculate and visualize the distance between the current location and the destination.

## Installation steps

Clone the Repo and install the requirements

```
git clone https://github.com/gulraiznoorbari/Geolocation-Distance-Measurement.git
cd Geolocation-Distance-Measurement
pip install -r requirements.txt
```
### Get Geodatabases from Maxmindb
 - [Get from Here](https://www.maxmind.com/en/accounts/549107/geoip/downloads)
 - Paste them to geoip folder 
 - run the application

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Integrate into an Existing Application

### Add into installed Apps
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'measurements',
]
```

## Author
You can get in touch with me on my LinkedIn Profile:

#### Gulraiz Noor Bari
[![LinkedIn Link](https://img.shields.io/badge/Connect-gulraiznoorbari-blue.svg?logo=linkedin&longCache=true&style=social&label=Connect
)](https://www.linkedin.com/in/gulraiznoorbari)
<br>
[![Twitter Link](https://img.shields.io/badge/Follow-gulraiznoorbari-blue.svg?logo=twitter&longCache=true&style=social&label=Follow
)](https://twitter.com/gulraiznoorbari)

You can also follow my GitHub Profile to stay updated about my latest projects: [![GitHub Follow](https://img.shields.io/badge/Connect-gulraiznoorbari-blue.svg?logo=Github&longCache=true&style=social&label=Follow)](https://github.com/gulraiznoorbari)

If you liked the repo then kindly support it by giving it a star ⭐!

## Contributions Welcome
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](#)

If you find any bug in the code or have any improvements in mind then feel free to generate a pull request.


