"""defines the urls for the between app"""

from django.urls import path

from .views import index

app_name = "between_app"

urlpatterns = [
    # page for the whole site
    path("", index, name="index"),
]
