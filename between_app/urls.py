"""defines the urls for the between app"""

from django.urls import path
from . import views

app_name = 'between_app'

urlpatterns = [
    #page for the whole site
    path('', views.IndexView.as_view(), name='index'),

 #home for all the tests
    path('tests/',views.test_home,name='test_home'),
   
# therapeutic positions

    path('tests/style_detail/<uuid:pk>/',views.style_detail,name='style_detail'),
    path('tests/style_list/',views.positions_list_view,name='profiles_list'),
    path('tests/profile_test/',views.take_profile_test,name='profile_test'),
    path('tests/profile_test_client/',views.take_profile_test_client,name='profile_test_client'),
    path('tests/content_1/',views.positions_content_view,name='content_1'),
    path('tests/results/<uuid:pk>/',views.ps_results,name='results'),

#Compnents

    path('tests/components_test/',views.take_components,name='components_test'),
    path('tests/components_list/',views.components_list,name='components_list'),
    path('tests/components_detail/<uuid:pk>/',views.components_detail,name='components_detail'),

#Traditions
    path('tests/traditions_test/',views.big_trad_test,name='traditions_test'),
    path('tests/traditions_list/',views.big_trad_list,name='traditions_list'),
    path('tests/traditions_detail/<uuid:pk>/',views.big_trad_detail,name='traditions_detail'),

    
#content
    path('content/',views.positions_content_view,name='content'),
    path('tests/results/<uuid:pk>/',views.ps_results,name='results'),



]