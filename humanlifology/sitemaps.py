from django.contrib.sitemaps import Sitemap
from articles.models import Article
from django.urls import reverse

class ArticleSitemap(Sitemap):
    changefreq = "weekly"
    priority = "0.9"
    protocol = "https"

    def items(self):
        return Article.objects.all().order_by("publish_timestamp")

    def lastmod(self, obj):
        return obj.edited_timestamp


class StaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = "1.0"
    protocol = "https"

    def items(self):
        return ['pages:home', 'pages:about_us', 'pages:contact_us', 'pages:privacy_policy', 'pages:disclaimer', 'accounts:register', 'accounts:login']

    def location(self, item):
        return reverse(item)
