from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class FAQPage(generic.TemplateView):
    template_name = "faq.html"
