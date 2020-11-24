from django.urls import path, include
import maps.views

urlpatterns = [
    path('robots.txt', maps.views.err_404),
    path('search', maps.views.test),
    path('result', maps.views.tested),
    path('test', maps.views.tested),
    path('tested', maps.views.tested)
]
