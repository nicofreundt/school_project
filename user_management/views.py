from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing_page(response):
    return HttpResponse(
        "<h1><a href='login_participant'>Participant Login</a></h1><h1><a href='login_creator'>Survey-Creator Login</a></h1><h1><a href='onboard_creator'>Survey-Creator Onboarding</a></h1>"
    )


def login_participant(response):
    return render(response, "login_participant.html", {})


def login_creator(response):
    return HttpResponse(
        "<h1><a href='login_creator_ldap'>LDAP Login</a></h1><br><h1><a href='login_creator_standard'>Standard Login</a></h1>"
    )


def login_creator_ldap(response):
    return HttpResponse("<h1><LDAP Login></h1>")


def login_creator_standard(response):
    return HttpResponse("<h1>Standard Login></h1>")


def onboard_creator(response):
    return HttpResponse(
        "<h1><a href='creator/sign_up_ldap'>LDAP Sign-Up</a></h1><br><h1><a href='creator/sign_up_test'>Test Sign-Up</a></h1>"
    )


def onboard_creator_ldap(response):
    return HttpResponse("<h1><LDAP Onboarding></h1>")


def onboard_creator_standard(response):
    return HttpResponse("<h1>Standard Onboarding></h1>")
