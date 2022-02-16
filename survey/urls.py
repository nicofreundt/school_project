from django.urls import path
from . import views

urlpatterns = [
    path("", views.survey_overview, name="Survey Overview"),
    path("create/", views.create_survey.as_view(), name="Create Survey"),
    path("create/", views.survey_overview, name="Create Survey"),
]
