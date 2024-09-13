from django.shortcuts import render


def home_page_view(request):
    """Home page view"""
    return HttpResponse("Hello, Word")
