"""
Models for the blog app.

This file defines the database models for blog posts and comments, 
including custom managers and tagging support.
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from django.utils.translation import gettext_lazy as _

class PublishedManager(models.Manager):
    """
    Custom manager to return only published posts.
    Overrides the default queryset to filter posts with status 'PUBLISHED'.
    """
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    """
    Model representing a blog post.

    Fields:
        title (CharField): The post's title.
        slug (SlugField): Unique URL-friendly identifier for the post.
        author (ForeignKey): User who authored the post.
        body (TextField): Content of the post.
        publish (DateTimeField): Publication date and time.
        created (DateTimeField): Creation timestamp.
        updated (DateTimeField): Last update timestamp.
        status (CharField): Publication status (Draft or Published).
        tags (TaggableManager): Tags associated with the post.

    Managers:
        objects: Default manager.
        published: Custom manager returning only published posts.
    """
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)

    # Managers
    objects = models.Manager()       # Default manager
    published = PublishedManager()   # Custom manager to fetch only published posts

    # Tag support
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):
        """String representation of the Post."""
        return self.title

    def get_absolute_url(self):
        """
        Returns the canonical URL for a post, including year, month, day, and slug.
        Useful for detail views.
        """
        return reverse('blog:post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])

class Comment(models.Model):
    """
    Model representing a comment on a blog post.

    Fields:
        post (ForeignKey): Associated blog post.
        name (CharField): Commenter's name.
        email (EmailField): Commenter's email.
        body (TextField): Comment content.
        created (DateTimeField): Timestamp when the comment was created.
        updated (DateTimeField): Timestamp when the comment was last updated.
        active (BooleanField): Whether the comment is publicly visible.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']
        indexes = [models.Index(fields=['created'])]

    def __str__(self) -> str:
        """String representation of the Comment."""
        return f"Comment by {self.name} on {self.post}"
