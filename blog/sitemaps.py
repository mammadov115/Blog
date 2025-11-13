"""
Sitemap definition for the blog app.

This file defines a sitemap class that allows search engines
to efficiently crawl published blog posts.
"""

from django.contrib.sitemaps import Sitemap
from .models import Post

class PostSitemap(Sitemap):
    """
    Sitemap for published blog posts.

    Attributes:
        changefreq (str): How frequently the page is likely to change.
        priority (float): Priority of the page relative to other pages.
    """
    changefreq = 'weekly'  # Indicates posts are updated roughly weekly
    priority = 0.9          # High priority for blog posts

    def items(self):
        """
        Returns the queryset of objects to include in the sitemap.
        Here we only include published posts.
        """
        return Post.published.all()

    def lastmod(self, obj):
        """
        Returns the last modified timestamp for a given object.
        Search engines can use this to identify recently updated posts.
        """
        return obj.updated
