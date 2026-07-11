"""defines the urls for the between app"""

from django.contrib.flatpages import views
from django.urls import include, path

from .views import index

app_name = "between_app"

urlpatterns = [
    # page for the whole site
    path("", index, name="index"),
    # flat pages config
    path("articles/", include("django.contrib.flatpages.urls")),  # group of flat pages, access by
    path("about/", views.flatpage, {"url": "/about/"}, name="about"),  # To add custom url of flat pages
    path(
        "data-policy/", views.flatpage, {"url": "/data-policy/"}, name="data_policy"
    ),  # To add custom url of flat pages
]
