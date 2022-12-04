from django.urls import path
from .views import RegisterView, UserProfileView
from django.contrib.auth.views import LoginView, PasswordChangeView
from .forms import LoginForm
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    path('profile/<str:slug>', UserProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(authentication_form=LoginForm), name='login'),
    path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html', success_url=reverse_lazy("articles:home"))),
]
