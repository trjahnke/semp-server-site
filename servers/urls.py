from django.contrib import admin
from django.urls import path, include
from .views import ServerForm
from django.views.generic import RedirectView

urlpatterns = [
    path('new', ServerForm),
    ]

