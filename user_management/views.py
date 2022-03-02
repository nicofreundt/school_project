from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(response):
    return render(response, 'home.html')
