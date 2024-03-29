from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as AbstractUserManager

# Create your models here.

class UserManager(AbstractUserManager):
    pass

class User(AbstractUser):
    objects = UserManager()

    def __str__(self):
        return self.username


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='images/profile_pics/default.jpg', upload_to='images/profile_pics')
    bio = models.CharField(max_length=699, default="")
    slug = models.SlugField(default="")

    def __str__(self):
        return f"{self.user.username} Profile"



    def save(self, *args, **kwargs):
        self.slug = self.user.username
        super().save(*args, **kwargs)
