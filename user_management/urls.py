from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing_page, name="Landing Page"),
    path("login_participant/", views.login_participant, name="Participant Login"),
    path("login_creator/", views.login_creator, name="Creator Login"),
    path("onboard_creator/", views.onboard_creator, name="Creator Onboarding"),
]
