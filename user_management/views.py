from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.
def landing_page(response):
    """Check if user is authenticated and redirect accordingly"""
    if(response.user.is_authenticated):
        return redirect('survey_overview'); # To Survey overview
    else:
        return redirect('login'); # To login
