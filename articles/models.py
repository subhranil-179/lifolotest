from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import User
from datetime import datetime
from django.contrib.postgres.indexes import GinIndex

# Create your models here.
KEYWORD_CHOICES = (
    ("S", "short"),
    ("L", "long"),
)

class Keyword(models.Model):
    keyword = models.CharField(max_length=200)
    keyword_type = models.CharField(max_length=1, choices=KEYWORD_CHOICES, default="S")

    def __str__(self):
        return str(self.keyword)


class Article(models.Model):
    # SEO
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600, default="")
    meta_title = models.CharField(max_length=200, default="")
    keywords = models.ManyToManyField(Keyword, related_name="article_keywords")
    slug = models.SlugField(max_length=300)
    canonical = models.URLField(max_length=300, default="", blank=True, null=True)

    # Schema (SEO)

    schema1 = models.TextField(blank=True, null=True)
    schema2 = models.TextField(blank=True, null=True)
    schema3 = models.TextField(blank=True, null=True)

    # Content
    content = models.TextField()

    #Time
    publish_timestamp = models.DateTimeField(auto_now_add=True)
    edited_timestamp = models.DateTimeField(auto_now=True)

    # Feed
    views = models.BigIntegerField(default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        indexes = [
            GinIndex(name='LifologyGinIndex', fields=['title', 'description', 'content'])
        ]

    def get_absolute_url(self):
        return reverse('articles:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == "":
            slug = slugify(str(self.title))
            count = self.__class__.objects.filter(
                    slug__startswith=slug).count()

            self.slug = slug

            if count > 0:
                self.slug = slug + "-" + str(count+1)

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

class Comment(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment_text = models.CharField(max_length=500)

    def __str__(self):
        return str(self.comment_text)

class Images(models.Model):
    article = models.ForeignKey(Article, default=None, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=f'images/articles/{datetime.now().strftime("%Y")}/{datetime.now().strftime("%m")}/{datetime.now().strftime("%d")}')

    def __str__(self):
        return str(self.image)

class Category(models.Model):
    category = models.CharField(max_length=200)
    keywords = models.ManyToManyField(Keyword, related_name="section_keywords")

    def __str__(self):
        return str(self.category)
