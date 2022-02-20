from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path("", lambda request: redirect("overview/", permanent=True)),
    path("overview/", views.survey_overview, name="Survey Overview"),
    path("create/", views.create_survey.as_view(), name="Create Survey"),
]
