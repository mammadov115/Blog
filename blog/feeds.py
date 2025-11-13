"""
RSS feed configuration for the blog app.

This file defines a custom RSS feed to provide the latest posts
in a format that feed readers can consume.
"""

from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords_html
from django.urls import reverse_lazy
import markdown
from .models import Post

class LatestPostsFeed(Feed):
    """
    RSS feed for the latest blog posts.

    Attributes:
        title (str): Title of the feed.
        link (str): URL of the feed homepage.
        description (str): Short description of the feed.
    
    Methods:
        items(): Returns the latest 5 published posts.
        item_title(item): Returns the title of a post.
        item_description(item): Returns a truncated HTML version of the post body.
        item_pubdate(item): Returns the publication date of the post.
    """
    title = 'My Blog'  # Feed title
    link = reverse_lazy('blog:post_list')  # URL to the main blog page
    description = 'New posts of my blog'  # Feed description

    def items(self):
        """
        Returns a queryset of the latest 5 published posts.
        """
        return Post.published.all()[:5]

    def item_title(self, item):
        """
        Returns the title of a single post for the feed.
        """
        return item.title
    
    def item_description(self, item):
        """
        Returns the body of the post in HTML format, truncated to 30 words.
        Markdown is converted to HTML.
        """
        return truncatewords_html(markdown.markdown(item.body), 30)
    
    def item_pubdate(self, item):
        """
        Returns the publication date of the post.
        """
        return item.publish
