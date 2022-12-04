from django.db.models.signals import post_save
from .models import User, UserProfile
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_userprofile(sender, instance, created, **kwargs):
    instance.userprofile.save()
