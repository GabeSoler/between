from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "weekly"

    def items(self):
        return ["between_app:index", 
                "between_app:test_home", 
                "dive_app:index",
                "learning_logs:index",
                "techniques_app:index",
                ]

    def location(self, item):
        return reverse(item)