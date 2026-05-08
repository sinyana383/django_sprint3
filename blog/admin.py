"""Admin configuration for the blog app."""
from django.contrib import admin

from .models import Category, Location, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Category admin settings."""

    list_display = ('title', 'slug', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('title',)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Location admin settings."""

    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin settings."""

    list_display = (
        'title', 'author', 'category', 'location', 'pub_date',
        'is_published',
    )
    list_editable = ('is_published',)
    list_filter = ('category', 'location', 'is_published')
    search_fields = ('title', 'text')
