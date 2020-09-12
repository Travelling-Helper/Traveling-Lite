from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

# Robots.txt for crawler engines
def robots(request):
    return render(request, "robots.txt")
def map_robots(request):
    return render(request, "err_404.html")

def gaodeMap(request):
    return render(request, "map.html")
