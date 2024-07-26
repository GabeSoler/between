"""defines url patterns for accoutns"""

from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views


app_name = 'accounts'

urlpatterns = [
    ## include defoult auth urls/ cancelled by django allauth
    #path('',include('django.contrib.auth.urls')),

    path("profile/", views.profile_view, name='account_profile'), #using allauth system, to integrate a account centre
                                                                        #i need to add link in the manage.py file and extend it too
    path("edit_profile/", views.community_profile_edit_view, name='account_profile'),
    path("edit_status/", views.user_status_edit_view, name='account_profile'),
]
