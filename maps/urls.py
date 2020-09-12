from django.urls import path, include
import maps.views

urlpatterns = [
    path('robots.txt', maps.views.map_robots),
    path('map', maps.views.gaodeMap)
]
