"""Defines URL patterns for tools."""

from django.urls import path

from . import views

app_name = 'tools'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),

    #client-session app
    path('session_home/', views.session_home, name='session_home'),
    path('client/', views.clients, name='client'),
    path('session/', views.sessions, name='session'),
    path('add_client/', views.add_client, name='add_client'),
    path('add_session/', views.add_session, name='add_session'),
    path('client_list/', views.clients, name='client_list'),
    path('session_list/', views.sessions, name='session_list'),
    path('edit_client/', views.session_home, name='edit_client'),
    path('edit_session/', views.session_home, name='edit_session'),

]