from django.contrib import admin
from .models import Article, Comment, Images

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Images)
