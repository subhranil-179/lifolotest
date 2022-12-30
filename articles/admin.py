from django.contrib import admin
from .models import Article, Comment, Images, Category

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Images)
admin.site.register(Category)
