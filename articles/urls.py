from django.urls import path
from articles.views import (ArticleCreateView,
                            ArticleUpdateView,
                            ArticleDeleteView)
from articles.views import article_view, fix, category_view, article_home_view, popular_view, latest_view


app_name = 'articles'
urlpatterns = [
    path('index/', article_home_view, name='home'),
    path('popular/', popular_view, name='popular'),
    path('latest/', latest_view, name='latest'),
    path('post/master-the-art-of-stress-relieving-with-these-10-activities-scientifically-proven/', fix, name='fix'),
    path('category/<str:category>/', category_view, name='category'),
    path('<slug:slug>/', article_view, name='detail')
    # path('post/new/', ArticleCreateView.as_view(), name='create'),
    # path('post/<slug:slug>/edit/', ArticleUpdateView.as_view(), name='edit'),
    # path('post/<slug:slug>/delete/', ArticleDeleteView.as_view(), name='delete'),
]
