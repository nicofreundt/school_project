from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path("", lambda request: redirect("survey_overview", permanent=True)),
    path("overview/", views.survey_overview, name="survey_overview"),
    path("create/", views.survey_create.as_view(), name="survey_create"),
    path('edit/<str:survey>/', views.survey_edit.as_view(), name="survey_edit"),
]
