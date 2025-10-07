from django import forms
from .models import Airport, Route

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'position']


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['source', 'destination', 'duration']