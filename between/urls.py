from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.flatpages import views
from django.contrib.sitemaps.views import sitemap
from decouple import config
from .sitemaps import StaticViewSitemap
from django.views.generic.base import TemplateView

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path(config('ADMIN_URL'), admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('accounts/',include('accounts.urls')),

    path('learning/',include('learning_logs.urls')),
    path('techniques/',include('techniques_app.urls')),
    path('diver/',include('dive_app.urls')),
    path('',include('between_app.urls')),
    
    #flat pages config
    path("articles/", include("django.contrib.flatpages.urls")), #group of flat pages, access by 
    path("about/", views.flatpage, {"url": "/about/"}, name="about"),#To add custom url of flat pages

    path("__reload__/", include("django_browser_reload.urls")), # for dj reload app
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')), #robots txt

    #adding a site map
    path("sitemap.xml/",
         sitemap,
        {"sitemaps":sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
        ),

    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#debug toolbar

if not settings.TESTING or settings.DEBUG:
    from debug_toolbar.toolbar import debug_toolbar_urls
    urlpatterns = [
        *urlpatterns,
    ] + debug_toolbar_urls()
