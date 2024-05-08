from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    #page for the topics of blogs
    path('',views.homeView.as_view(),name='index'),

]