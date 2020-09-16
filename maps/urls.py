from django.urls import path, include
import maps.views

urlpatterns = [
    path('robots.txt', maps.views.err_404),
    path('map', maps.views.gaodeMap),
    path('test', maps.views.test),
    path('tested', maps.views.tested)
]
