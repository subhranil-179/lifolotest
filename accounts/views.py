from django.shortcuts import render, redirect
from .forms import UserCreationForm, UserUpdateForm, UserProfileUpdateForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.decorators import login_required

# Create your views here.

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserProfileView(LoginRequiredMixin, DetailView):
    model = UserProfile
    template_name = 'registration/profile.html'
    slug = 'slug'
    context_object_name = 'profile'

@login_required
def profile_update_view(request, slug):
    profile = UserProfile.objects.get(slug=slug)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile have been updated successfully')
            return redirect(reverse_lazy('articles:home'))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = UserProfileUpdateForm(instance=request.user.userprofile)
    context = {
        "profile": profile,
        "u_form": u_form,
        "p_form": p_form,
    }
    return render(request, "registration/profile.html", context)
