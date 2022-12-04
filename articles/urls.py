from django.urls import path
from articles.views import (HomeView,
                            ArticleDetailView,
                            ArticleCreateView,
                            ArticleUpdateView,
                            ArticleDeleteView)
from articles.views import article_view


app_name = 'articles'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/new/', ArticleCreateView.as_view(), name='create'),
    path('post/<slug:slug>/', article_view, name='detail'),
    path('post/<slug:slug>/edit/', ArticleUpdateView.as_view(), name='edit'),
    path('post/<slug:slug>/delete/', ArticleDeleteView.as_view(), name='delete'),
]
