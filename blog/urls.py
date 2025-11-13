"""
URL configuration for the blog app.

Defines all routes for blog listing, detail views, sharing, commenting,
searching, tagging, and RSS feeds.
"""

from django.urls import path
from . import views
from .views import PostListView
from .feeds import LatestPostsFeed

# Namespace for blog URLs
app_name = 'blog'

urlpatterns = [
    # List all published posts
    path('', views.post_list, name='post_list'),

    # List posts filtered by tag slug
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),

    # Optional: class-based list view (commented out)
    # path('', PostListView.as_view(), name='post_list'),

    # Detailed view of a single post, using year, month, day, and slug
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),

    # Share a post via email
    path('<int:post_id>/share/', views.post_share, name='post_share'),

    # Submit a comment to a post
    path('<int:post_id>/comment', views.post_comment, name='post_comment'),

    # RSS feed for latest posts
    path('feed/', LatestPostsFeed(), name='post_feed'),

    # Search posts by query
    path('search/', views.post_search, name='post_search'),
]
