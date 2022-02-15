from django.urls import path
from . import views

urlpatterns = [
    path("", views.survey_overview, name="Survey Overview"),
]
