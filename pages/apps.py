"""Application configuration for static pages."""
from django.apps import AppConfig


class PagesConfig(AppConfig):
    """Pages app configuration."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
