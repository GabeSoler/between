"""defines url patterns for accoutns"""

from django.urls import path,include
from django.views.generic.base import TemplateView
from . import views


app_name = 'accounts'

urlpatterns = [
    ## include defoult auth urls/ cancelled by django allauth
    #path('',include('django.contrib.auth.urls')),

    path("profile/", views.profile_view, name='account_profile'), #using allauth system, to integrate a account centre
    path("edit_profile/", views.community_profile_edit_view, name='edit_profile'),
    path("edit_status/", views.user_status_edit_view, name='edit_status'),
    path("delete_account/", views.delete_account_view, name='delete_account'),

]
