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


class SearchNthNodeForm(forms.Form):
    start_airport = forms.ModelChoiceField(queryset=Airport.objects.all())
    direction = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')])
    n = forms.IntegerField(min_value=1)