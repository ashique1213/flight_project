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
    start_airport = forms.ModelChoiceField(queryset=Airport.objects.all(),label="Select Starting Airport(Node)")
    direction = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')])
    n = forms.IntegerField(min_value=1, label="Enter N (step count)")
   
class ShortestRouteForm(forms.Form):
    source = forms.ModelChoiceField(queryset=Airport.objects.all(),label="Source Airport")
    destination = forms.ModelChoiceField(queryset=Airport.objects.all(),label="Destination Airport")