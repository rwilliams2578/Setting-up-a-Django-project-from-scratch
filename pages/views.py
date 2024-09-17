from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Pass"""

    template_name = "home.html"


class AboutPageView(TemplateView):
    """About Page View"""

    template_name = "about.html"
