from django.shortcuts import redirect
from django.urls import path
from . import views

urlpatterns = [
    path("", lambda request: redirect("survey_overview", permanent=True)),
    path("overview/", views.survey_overview, name="survey_overview"),
    path("create/", views.survey_create.as_view(), name="survey_create"),
    path("delete/<survey>/", views.survey_delete, name="survey_delete"),
    path("edit/<survey>/", views.survey_edit.as_view(), name="survey_edit"),
    path(
        "edit/<survey>/create/question/",
        views.question_create.as_view(),
        name="question_create",
    ),
    path(
        "edit/<survey>/edit/question/<question>/",
        views.question_edit.as_view(),
        name="question_edit",
    ),
]
