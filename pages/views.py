from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class AboutPageView(TemplateView):
    template_name = 'pages/about_us.html'
class ContactPageView(TemplateView):
    template_name = 'pages/contact_us.html'
class PrivacyPolicyPageView(TemplateView):
    template_name = 'pages/privacy_policy.html'
class BlogView(TemplateView):
    template_name = 'pages/blog.html'
