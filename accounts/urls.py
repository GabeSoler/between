"""defines url patterns for accoutns"""

from django.urls import path,include
from .views import SignupPageView

app_name = 'accounts'

urlpatterns = [
    #include defoult auth urls
    path('',include('django.contrib.auth.urls')),
    #registration page
    path('signup/',SignupPageView.as_view(),name='signup'),
]
