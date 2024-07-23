"""defines url patterns for accoutns"""

from django.urls import path,include
from .views import settings_view,community_profile_view
from django.views.generic.base import TemplateView

app_name = 'accounts'

urlpatterns = [
    ## include defoult auth urls/ cancelled by django allauth
    #path('',include('django.contrib.auth.urls')),

    path('settings/',settings_view,name='settings'),
    #path('profile/',community_profile_view,name='account_profile'),
    path("profile/", TemplateView.as_view(template_name="profile.html")), #using allauth system, to integrate a account centre
                                                                        #i need to add link in the manage.py file and extend it too

]
