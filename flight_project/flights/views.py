from django.shortcuts import render
from .models import Airport, Route
from .forms import AirportForm

# Add Airport
def add_airport(request):
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AirportForm()
    airports = Airport.objects.all()
    return render(request, 'add_airport.html', {'form': form, 'airports': airports})
