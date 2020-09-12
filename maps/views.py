from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Robots.txt for crawler engines
def robots(request):
    return render(request, "robots.txt")

def gaodeMap(request):
    return render(request, "map.html")
