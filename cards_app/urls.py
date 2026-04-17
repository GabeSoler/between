from django.urls import path
from .views import *

urlpatterns = [
    path('card-list', card_list, name='card_list'),
    path('', select_card_type__view, name='select_card_type'),
]


