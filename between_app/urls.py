"""defines the urls for the between app"""

from django.urls import path
from . import views

app_name = 'between_app'

urlpatterns = [
    #page for the whole site
    path('',views.index_View.as_view(),name='index'),

 #home for all the tests
    path('test_home/',views.test_home,name='test_home'),
   

# therapeutic positions

    path('form_detail/<uuid:pk>/',views.formDetailView.as_view(),name='personal_style_detail'),
    #path('results/<uuid:pk>/',views.resultsView.as_view(),name='results'),
    path('profile_test/',views.takeTestView.as_view(),name='profile_test'),
    path('content/',views.contentView.as_view(),name='content'),

#Compnents

    path('components_test/',views.takeComponentstView.as_view(),name='components_test'),

#Traditions
    path('traditions_test/',views.takeTraditionsView.as_view(),name='traditions_test'),

    
#content
    path('content_1/',views.contentView.as_view(),name='content_1'),

    path('results_email/<uuid:pk>/',views.ps_results,name='results'),


]