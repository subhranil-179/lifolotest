from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import F
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from articles.models import Article, Comment, Category
from .forms import CommentForm
# Create your views here.

"""

class ArticleDetailView(DetailView):
    model = Article
    slug_field = 'slug'
    template_name = 'articles/detail.html'
    context_object_name = 'blog'
"""


def article_view(request, slug):
    blog = get_object_or_404(Article, slug=slug)
    blog.views = F('views') + 1
    blog.save(update_fields=['views'])

    popular_articles = Article.objects.order_by('-views')[:5]

    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(commenter=request.user, article=blog, comment_text=comment_form.data.get('message'))
        return redirect(reverse("articles:detail", kwargs={'slug': blog.slug}))
    
    context = {
        'blog': blog,
        'form': comment_form,
        'popular_articles': popular_articles,
    }
    return render(request, "articles/detail.html", context)


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/create.html'
    fields = ['title', 'content']


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'articles/update.html'
    fields = ['title', 'content']


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'articles/delete.html'
    success_url = reverse_lazy('article:home')



def fix(request):
    blog = Article.objects.get(slug="10-best-stress-relieving-activities")
    return render(request, "articles/fix.html", {"blog": blog})
    # return redirect(reverse("articles:detail", kwargs={"slug": "10-best-stress-relieving-activities"}))

def category_view(request, category):
    keywords = Category.objects.get(category=category).keywords.all()
    context = {"category": category,
        "keywords": keywords
    }
    return render(request, "articles/category.html", context)

def article_home_view(request):
    featured_articles = Article.objects.filter(featured=True)
    popular_article_list = Article.objects.order_by("-views")[:5]
    latest_article_list = Article.objects.order_by("-publish_timestamp")[:5]
    categories = Category.objects.all()
    # print(dir(categories[0].keywords.all())
    context = {
            "featured_articles": featured_articles,
            "categories": categories,
            "popular_article_list": popular_article_list,
            "latest_article_list": latest_article_list,
    }
    return render(request, "articles/home.html", context)


def popular_view(request):
    article_list = Article.objects.all().order_by('-views')
    context = {"article_list": article_list,
        "section": "Popular",
    }
    return render(request, "articles/article_.html", context)


def latest_view(request):
    article_list = Article.objects.all().order_by('-publish_timestamp')
    context = {"article_list": article_list,
        "section": "Latest",
    }
    return render(request, "articles/article_.html", context)
