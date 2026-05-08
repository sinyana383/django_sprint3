"""Views for static pages."""
from django.shortcuts import render


def about(request):
    """Display the about page."""
    return render(request, 'pages/about.html')


def rules(request):
    """Display the rules page."""
    return render(request, 'pages/rules.html')
