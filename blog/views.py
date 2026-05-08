"""Views for blog pages."""
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post

POSTS_ON_MAIN_PAGE = 5


def published_posts():
    """Return posts available for public listing."""
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now(),
    )


def index(request):
    """Display the latest published posts."""
    post_list = published_posts()[:POSTS_ON_MAIN_PAGE]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    """Display one published post."""
    post = get_object_or_404(published_posts(), pk=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    """Display published posts from a published category."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = published_posts().filter(category=category)
    context = {'category': category, 'post_list': post_list}
    return render(request, 'blog/category.html', context)
