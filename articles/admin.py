from django.contrib import admin
from .models import Article, Comment, Images, Keyword, Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Images)
admin.site.register(Keyword)
admin.site.register(Category)
