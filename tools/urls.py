"""Defines URL patterns for tools."""

from django.urls import path

from . import views

app_name = 'tools'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]