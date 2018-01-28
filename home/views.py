from django.shortcuts import render, HttpResponse
from jinja2 import Environment


# Create your views here.
def home (request):
    return render(request, 'home/home.html')

#return HttpResponse("Ana Sayfa.")
