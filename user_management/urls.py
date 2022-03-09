from django.urls import path, include
from . import views

# URLs #
urlpatterns = [
    path("", views.landing_page),
    path("accounts/", include("django.contrib.auth.urls")),
]
