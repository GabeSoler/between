# urls.py
from django.urls import path

from . import views

app_name = "stones_app"

urlpatterns = [
    path("", views.sandbox, name="sandbox"),
]
