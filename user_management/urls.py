from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home_page, name="Home"),
    path('accounts/', include('django.contrib.auth.urls'))
]
