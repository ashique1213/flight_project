from django.shortcuts import render
from .models import Airport, Route
from .forms import AirportForm, RouteForm,SearchNthNodeForm

# Add Airport
def add_airport(request):
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AirportForm()
    airports = Airport.objects.all()
    return render(request, 'add_airport.html', {'form': form, 'airports': airports})


# Add Route
def add_route(request):
    form = RouteForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RouteForm()
    routes = Route.objects.all()
    return render(request, 'add_route.html', {'form': form, 'routes': routes})

# Find Nth Left or Right Node
def find_nth_node(request):
    result = None
    form = SearchNthNodeForm(request.POST or None)
    if form.is_valid():
        start = form.cleaned_data['start_airport']
        direction = form.cleaned_data['direction']
        n = form.cleaned_data['n']

        if direction == 'right':
            for i in range(n):
                route = Route.objects.filter(source=start).first()
                if not route:
                    result = "No further route found."
                    break
                start = route.destination
            else:
                result = f"{n}th Right Node: {start.code}"
        else:
            for i in range(n):
                route = Route.objects.filter(destination=start).first()
                if not route:
                    result = "No further route found."
                    break
                start = route.source
            else:
                result = f"{n}th Left Node: {start.code}"

    return render(request, 'nth_node.html', {'form': form, 'result': result})
