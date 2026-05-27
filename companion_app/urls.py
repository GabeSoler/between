from django.urls import path

from . import views

app_name = 'companion_app'

urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    path('path', views.index, name='path'),
    path('therapy-needs', views.index, name='therapy_needs'),
    path('therapy-search', views.index, name='therapy_search'),
    path('therapy-connection', views.index, name='therapy_connection'),
    path('therapy-process', views.index, name='therapy_process'),
    path('cards-journal', views.index, name='cards_journal'),
    path('sessions-journal', views.index, name='sessions_journal'),
    ]
