"""
URL configuration for mysite project.

This file defines the URL patterns for the project, including:
- Django admin interface
- Blog app URLs
- Sitemap generation for search engines
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog.sitemaps import PostSitemap

# Dictionary of sitemaps for search engines
sitemaps = {
    'posts': PostSitemap,  # Sitemap for blog posts
}

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Blog app URLs
    path('blog/', include('blog.urls', namespace='blog')),

    # Sitemap URL for search engines
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
