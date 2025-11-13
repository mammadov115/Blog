"""
Forms for the blog app.

This file contains Django forms used for:
1. Sharing posts via email.
2. Submitting comments.
3. Searching posts.
"""

from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    """
    Form for sharing a blog post via email.

    Fields:
        name (CharField): Name of the person sending the email.
        email (EmailField): Sender's email address.
        to (EmailField): Recipient's email address.
        comments (CharField): Optional message from the sender.
    """
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=False, 
        widget=forms.Textarea,
        help_text="Optional message to include in the email"
    )

class CommentForm(forms.ModelForm):
    """
    Form for submitting a comment on a blog post.

    This uses the Comment model and includes the fields:
        - name
        - email
        - body (comment text)
    """
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class SearchForm(forms.Form):
    """
    Form for searching blog posts by query.

    Fields:
        query (CharField): The search term entered by the user.
    """
    query = forms.CharField(
        max_length=255,
        help_text="Enter keywords to search blog posts"
    )
