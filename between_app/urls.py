"""defines the urls for the between app"""

from django.urls import path
from . import views

app_name = 'between_app'

urlpatterns = [
    #page for the topics of blogs
    path('',views.index_View.as_view(),name='index'),
    path('form_detail/<int:pk>/',views.formDetailView.as_view(),name='formDetail'),
    path('results/<int:pk>/',views.resultsView.as_view(),name='results'),

    ]

