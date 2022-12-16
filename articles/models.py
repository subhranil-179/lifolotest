from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from accounts.models import User
from datetime import datetime

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    keywords = models.CharField(max_length=200, default="")
    description = models.CharField(max_length=600, default="")
    slug = models.SlugField(max_length=300)
    publish_timestamp = models.DateTimeField(auto_now_add=True)
    edited_timestamp = models.DateTimeField(auto_now=True)

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
