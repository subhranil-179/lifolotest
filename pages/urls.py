from django.urls import path
from pages.views import (AboutPageView,
                         ContactPageView,
                         PrivacyPolicyPageView,
                         DisclaimerPageView,
                         TACPageView,
                         BlogView,
                         home_page,
                         contact_us, )

app_name='pages'

urlpatterns = [
    path('', home_page, name='home'),
    path('about_us/', AboutPageView.as_view(), name='about_us'),
    path('contact_us/', contact_us, name='contact_us'),
    path('privacy_policy/', PrivacyPolicyPageView.as_view(), name='privacy_policy'),
    path('disclaimer/', DisclaimerPageView.as_view(), name='disclaimer'),
    path('terms-and-conditions/', TACPageView.as_view(), name='tac'),
    path('blog/', BlogView.as_view(), name='blog'),
]
