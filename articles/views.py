from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)

from django.views.generic.edit import FormMixin
from articles.models import Article, Comment
from .forms import CommentForm
# Create your views here.

class HomeView(ListView):
    model = Article
    template_name = 'articles/home.html'
    context_object_name = 'article_list'


class ArticleDetailView(DetailView):
    model = Article
    slug_field = 'slug'
    template_name = 'articles/detail.html'
    context_object_name = 'blog'



def article_view(request, slug):
    blog = Article.objects.get(slug=slug)
    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(commenter=request.user, article=blog, comment_text=comment_form.data.get('message'))
        return redirect(reverse("articles:detail", kwargs={'slug': blog.slug}))
    
    context = {
        'blog': blog,
        'form': comment_form,
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
