"""defines the urls for the between app"""

from django.urls import path
from . import views

app_name = 'between_app'

urlpatterns = [
    #page for the topics of blogs
    path('',views.index_View.as_view(),name='index'),
    path('form_list/',views.resultsList.as_view(),name='results_list'),
    path('form_detail/<uuid:pk>/',views.formDetailView.as_view(),name='personal_style_detail'),
    path('results/<uuid:pk>/',views.resultsView.as_view(),name='results'),
    path('profile_test/',views.takeTestView.as_view(),name='profile_test'),
    path('content/',views.contentView.as_view(),name='content'),

#Compnents

    path('components_test/',views.takeComponentstView.as_view(),name='components_test'),

#Traditions
    path('traditions_test/',views.takeTraditionsView.as_view(),name='traditions_test'),


    ]

