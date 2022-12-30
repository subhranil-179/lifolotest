from django.shortcuts import render
from articles.models import Article
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank

# Create your views here.

def search(request):
    q = None
    if request.method == 'GET':
        q = request.GET.get('q')
        vector = SearchVector('title', 'description', 'content')
        vector = SearchVector('title', weight='A') + SearchVector('description', weight='B') + SearchVector('content', weight='D')
        query = SearchQuery(q)
        results = Article.objects.annotate(rank=SearchRank(vector, query, cover_density=True)).filter(rank__gte=0.001).order_by('-rank')
        print(results)
    context = {"article_list": results}
    if q == None:
        context = {}
    print(context)
    return render(request, "search/search.html", context)
