import requests

from django.conf import settings
from django.shortcuts import render


def geo_home(request):
    response = requests.get(f'http://api.ipstack.com/check?access_key={settings.IP_STACK}')
    geodata = response.json()
    return render(request, 'geo_home.html', {
        'ip': geodata['ip'],
        'country': geodata['country_name'],
        'latitude': geodata['latitude'],
        'longitude': geodata['longitude'],
        'google_api_key': settings.GOOGLE_MAPS_API_KEY,
    })
