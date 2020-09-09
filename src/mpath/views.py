"""
@author Yuqi Hu
@date Sep. 9th 2020
@version 0.0
"""

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Robots.txt for crawler engines
def robots(request):
    return render(request, "robots.txt")
