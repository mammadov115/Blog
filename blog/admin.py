"""
Django admin configuration for the blog app.

This file registers the Post and Comment models with the admin site
and customizes their admin interface to improve usability.
"""

from django.contrib import admin
from .models import Post, Comment

# Register the Post model with custom admin options
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Admin interface for the Post model.

    Customizations include:
    - Displaying key fields in the list view
    - Filtering posts by status, creation, publish date, and author
    - Searching posts by title and body
    - Prepopulating the slug field from the title
    - Using raw ID fields for author to optimize performance
    - Hierarchical date navigation and ordering
    """
    list_display = ('title', 'slug', 'author', 'publish', 'status')  # Columns to display
    list_filter = ('status', 'created', 'publish', 'author')          # Sidebar filters
    search_fields = ('title', 'body')                                 # Searchable fields
    prepopulated_fields = {'slug': ('title',)}                        # Auto-generate slug
    raw_id_fields = ('author',)                                       # Optimized foreign key selection
    date_hierarchy = 'publish'                                        # Date-based drilldown
    ordering = ('status', 'publish')                                   # Default ordering

# Register the Comment model with custom admin options
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin interface for the Comment model.

    Customizations include:
    - Displaying key comment fields in the list view
    - Filtering comments by active status and creation/update dates
    - Searching comments by name, email, and body
    """
    list_display = ['name', 'email', 'post', 'created', 'active']    # Columns to display
    list_filter = ['active', 'created', 'updated']                   # Sidebar filters
    search_fields = ['name', 'email', 'body']                        # Searchable fields
