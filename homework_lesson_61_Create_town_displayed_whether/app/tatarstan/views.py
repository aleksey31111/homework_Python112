import requests
from django.shortcuts import render

def tatarstan(request):
    app_id = '177f6d3726fc411f8bb183205222408'
    city = 'Нижнекамск'
    url = f"http://api.weatherapi.com/v1/current.json?key={ app_id }&q={ city }&aqi=no"
    nizhnekamsk_weather = requests.get(url).json()
    # print(nizhnekamsk_weather)
    nizhnekamsk_info = {
        'name': nizhnekamsk_weather['location']['name'],
        'temp': nizhnekamsk_weather['current']['temp_c'],

        'icon': nizhnekamsk_weather['current']['condition']['icon']
    }
    context = {'info': nizhnekamsk_info}
    return render(request, 'tatarstan/tatarstan.html', context)
