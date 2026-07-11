from decouple import config
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic.base import TemplateView

from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = (
    [
        path(config("ADMIN_URL"), admin.site.urls),
        path("accounts/", include("allauth.urls")),
        path("", include("base.urls")),
        path("accounts/", include("accounts.urls")),
        path("learning/", include("learning_logs.urls")),
        path("techniques/", include("techniques_app.urls")),
        path("diver/", include("dive_app.urls")),
        path("profiles/", include("between_app.urls")),
        path("cards/", include("cards_app.urls")),
        path("companion", include("companion_app.urls")),
        path("__reload__/", include("django_browser_reload.urls")),  # for dj reload app
        path(
            "robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")
        ),  # robots txt
        # adding a site map
        path(
            "sitemap.xml/",
            sitemap,
            {"sitemaps": sitemaps},
            name="django.contrib.sitemaps.views.sitemap",
        ),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
