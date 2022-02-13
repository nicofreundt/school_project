from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def signIn(response):
    return HttpResponse("<h1>Username:</h1><br><h1>Password:</h1>")
