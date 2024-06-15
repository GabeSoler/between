from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    #page for the topics of blogs
    path('',views.indexView.as_view(),name='index'),
    path('creation/',views.creationView.as_view(),name='creation'),
    path('profiles/',views.ProfilesView.as_view(),name='profiles'),
    path('components/',views.ComponentsView.as_view(),name='components'),
    path('intro/',views.introView.as_view(),name='intro'),
    path('history/',views.HistoryView.as_view(),name='history'),


]