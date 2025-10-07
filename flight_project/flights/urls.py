from django.urls import path
from . import views

urlpatterns = [
    path('add-airport/', views.add_airport, name='add_airport'),
    path('add-route/', views.add_route, name='add_route'),
    path('nth-node/', views.find_nth_node, name='nth_node'),


]
