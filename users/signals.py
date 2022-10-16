from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.username
        )


@receiver(post_save, sender=Profile)
def edit_profile(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    if created is False:
        user.name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=Profile)
def delete_profile(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except Exception:
        pass
