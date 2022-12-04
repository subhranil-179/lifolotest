from django.shortcuts import render
from .forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from .models import UserProfile

# Create your views here.

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserProfileView(DetailView):
    model = UserProfile
    template_name = 'registration/profile.html'
    slug = 'slug'
    context_object_name = 'profile'
