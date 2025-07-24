from django import forms

class WeatherForm(forms.Form):
    city = forms.CharField(label="Choose the city", max_length=100)