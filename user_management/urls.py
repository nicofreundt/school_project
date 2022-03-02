from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing_page),
    path('accounts/', include('django.contrib.auth.urls')),
]
