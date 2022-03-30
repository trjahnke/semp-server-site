from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import RedirectView
from .views import wiki, connection


urlpatterns = [
    re_path(r'^(?P<page_alias>.+?)/connection', connection, name='connection'),
    re_path(r'^(?P<page_alias>.+?)/', wiki, name='wiki'),
    ]

