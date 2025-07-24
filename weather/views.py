from django.shortcuts import render, redirect
from weather.models import WeatherQuery
from weather.forms import WeatherForm
from django.conf import settings
import requests
from requests.exceptions import RequestException


def home(request):
    weather_data = None
    form = WeatherForm()

    if request.method == 'POST':
        form = WeatherForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']

            try:
                url = (
                    f"https://api.openweathermap.org/data/2.5/weather?"
                    f"q={city}&appid={settings.OPENWEATHER_API_KEY}&units=metric&lang=en"
                )

                response = requests.get(url)
                response.raise_for_status()

                data = response.json()

                if data.get('cod') == 200:
                    weather_data = {
                        'city': city,
                        'temperature': data['main']['temp'],
                        'description': data['weather'][0]['description']
                    }

                    WeatherQuery.objects.create(**weather_data)

                else:
                    form.add_error('city', data.get('message', 'City not found or API unavailable'))

            except RequestException as e:
                form.add_error(None, f'API request error: {e}')
            except Exception as e:
                form.add_error(None, f'An unexpected error occurred: {e}')

    history = WeatherQuery.objects.order_by('-timestamp')[:10]

    return render(request, 'weather/home.html', {
        'form': form,
        'weather': weather_data,
        'history': history,
    })