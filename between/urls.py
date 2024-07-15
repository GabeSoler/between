"""
URL configuration for between project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.flatpages import views
from django.contrib.flatpages.sitemaps import FlatPageSitemap
from django.contrib.sitemaps.views import sitemap
from decouple import config


urlpatterns = [
    path(config('ADMIN_URL'), admin.site.urls),
    #path('accounts/',include('accounts.urls')),
    path('accounts/',include('allauth.urls')),
    path('learning/',include('learning_logs.urls')),
    path('pages/',include('pages.urls')),
    path('techniques/',include('techniques_app.urls')),
    path('',include('between_app.urls')),
    
    #flat pages config
    path("articles/", include("django.contrib.flatpages.urls")), #group of flat pages, access by 
    path("about/", views.flatpage, {"url": "/about/"}, name="about"),#To add custom url of flat pages

    #adding a site map
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": {"flatpages": FlatPageSitemap}},
        name="django.contrib.sitemaps.views.sitemap",
    ),

    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)