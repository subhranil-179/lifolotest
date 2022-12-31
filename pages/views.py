from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import ContactForm
from django.core.mail import send_mail
from django.urls import reverse
from articles.models import Article, Category

# Create your views here.
class AboutPageView(TemplateView):
    template_name = 'pages/about_us.html'
class PrivacyPolicyPageView(TemplateView):
    template_name = 'pages/privacy_policy.html'
class DisclaimerPageView(TemplateView):
    template_name = 'pages/disclaimer.html'
class TACPageView(TemplateView):
    template_name = 'pages/tac.html'
class BlogView(TemplateView):
    template_name = 'pages/blog.html'

# Temproraliy not required
class ContactPageView(TemplateView):
    template_name = 'pages/contact_us.html'


def contact_us(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            name = contact_form.cleaned_data.get('name')
            email = contact_form.cleaned_data.get('email')
            subject = contact_form.cleaned_data.get('subject')
            message = contact_form.cleaned_data.get('message')
            send_mail(subject, message, email, ['lifology.site@gmail.com'])
            return redirect(reverse('pages:contact_us'))
    return render(request, "pages/contact_us.html", {'form': contact_form})

def home_page(request):
    featured_articles = Article.objects.filter(featured=True)
    categories = Category.objects.all()
    # print(dir(categories[0].keywords.all())
    context = {
            "featured_articles": featured_articles,
            "categories": categories,
    }
    return render(request, "pages/home.html", context)
