"""Application configuration for the blog app."""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Blog app configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    verbose_name = 'Блог'
