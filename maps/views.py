from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

# Robots.txt for crawler engines
def robots(request):
    return render(request, "robots.txt")
def err_404(request):
    return render(request, "err_404.html")

def gaodeMap(request):
    return render(request, "map.html")
def test(request):

    return render(request, "maps/test.html") #测试

def tested(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        print(request.POST.get('password'))
    return render(request, "maps/tested.html", {
        'location': request.POST.get('location'),
        'username': request.POST.get('username'),
        'password': request.POST.get('password')
    })