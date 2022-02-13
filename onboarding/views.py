from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(response):
    return HttpResponse(
        "<h1><a href='participant'>Participant Onboarding:</a></h1><br><h1><a href='creator'> Survey-Creator Onboarding:</a></h1>"
    )


def onboardParticipant(response):
    return render(response, "onboardParticipant.html", {})


def onboardCreator(response):
    return HttpResponse(
        "<h1><a href='creator/sign_up_ldap'>LDAP Sign-Up</a></h1><br><h1><a href='creator/sign_up_test'>Test Sign-Up</a></h1>"
    )
