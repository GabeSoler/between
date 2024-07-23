"""defines url patterns for accoutns"""

from django.urls import path,include
from .views import settings_view,community_profile_view

app_name = 'accounts'

urlpatterns = [
    ## include defoult auth urls/ cancelled by django allauth
    #path('',include('django.contrib.auth.urls')),

    path('settings/',settings_view,name='settings'),
    path('profile/',community_profile_view,name='account_profile'),
]
