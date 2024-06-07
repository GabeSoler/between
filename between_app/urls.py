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

    path('style_detail/<uuid:pk>/',views.style_detail,name='style_detail'),
    path('style_list/',views.PositionListView.as_view(),name='profiles_list'),
    path('profile_test/',views.takeTestView.as_view(),name='profile_test'),
    path('content/',views.contentView.as_view(),name='content'),
    path('results_email/<uuid:pk>/',views.ps_results,name='results'),

#Compnents

    path('components_test/',views.take_components,name='components_test'),
    path('components_list/',views.components_list,name='components_list'),
    path('components_detail/<uuid:pk>/',views.components_detail,name='components_detail'),

#Traditions
    path('traditions_test/',views.big_trad_test,name='traditions_test'),
    path('traditions_list/',views.big_trad_list,name='traditions_list'),
    path('traditions_detail/<uuid:pk>/',views.big_trad_detail,name='traditions_detail'),

    
#content
    path('content_1/',views.contentView.as_view(),name='content_1'),

    path('results_email/<uuid:pk>/',views.ps_results,name='results'),


]