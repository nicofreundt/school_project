from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("creator/", views.onboardCreator, name="onboardCreator"),
    path("participant/", views.onboardParticipant, name="onboardParticipant"),
]
