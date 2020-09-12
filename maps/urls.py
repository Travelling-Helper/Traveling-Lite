from django.urls import path, include
import maps.views

urlpatterns = [
    path('robots.txt', maps.views.robots),
    path('', maps.views.gaodeMap)
]
