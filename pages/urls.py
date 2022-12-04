from django.urls import path, include
from pages.views import (AboutPageView,
                         ContactPageView,
                         PrivacyPolicyPageView,
                         BlogView,)

app_name='pages'

urlpatterns = [
    path('', include("articles.urls"), name='home'),
    path('about_us/', AboutPageView.as_view(), name='about_us'),
    path('contact_us/', ContactPageView.as_view(), name='contact_us'),
    path('privacy_policy/', PrivacyPolicyPageView.as_view(), name='privacy_policy'),
    path('blog/', BlogView.as_view(), name='blog'),
]
