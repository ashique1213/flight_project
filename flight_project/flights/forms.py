from django import forms
from .models import Airport, Route

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['code', 'name']

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['source', 'destination', 'position', 'duration']

class SearchNthNodeForm(forms.Form):
    route_id = forms.IntegerField(label="Enter Route ID")
    direction = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')])
    n = forms.IntegerField(min_value=1, label="Enter N (step count)")