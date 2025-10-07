from django.shortcuts import render
from .models import Airport, Route
from .forms import AirportForm, RouteForm,SearchNthNodeForm,ShortestRouteForm

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
    form = SearchNthNodeForm(request.GET or None)
    result = None
    if form.is_valid():
        start_airport = form.cleaned_data['start_airport']
        direction = form.cleaned_data['direction']
        n = form.cleaned_data['n']

        # Get all routes in order
        routes = list(Route.objects.order_by('position'))
        # Find the route that starts from this airport
        current_index = next((i for i, r in enumerate(routes) if r.source == start_airport), None)

        if current_index is not None:
            target_index = current_index - n if direction == 'left' else current_index + n
            if 0 <= target_index < len(routes):
                result = routes[target_index]
            else:
                result = "No route found in that direction."
        else:
            result = "Starting airport(node) not found in any route."

    return render(request, 'nth_node.html', {'form': form, 'result': result})


# Find Longest Route (based on duration)
def longest_route_view(request):
    longest = Route.objects.order_by('-duration').first()
    return render(request, 'longest_route.html', {'longest': longest})

# Find Shortest Route between Two Airports
def shortest_route_view(request):
    form = ShortestRouteForm(request.GET or None)
    result = None

    if form.is_valid():
        src = form.cleaned_data['source']
        dest = form.cleaned_data['destination']
        route = Route.objects.filter(source=src, destination=dest).order_by('duration').first()
        result = route if route else "No route found between given airports."

    return render(request, 'shortest_route.html', {'form': form, 'result': result})