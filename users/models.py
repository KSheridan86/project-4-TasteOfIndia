from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    """
    Docstrings R us!!
    """
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    profile_image = CloudinaryField(
        'image', default='placeholder', blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    quote = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    fav_food = models.CharField(max_length=80, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Docstrings R us!!
        """
        ordering = ['username']

    def __str__(self):
        return str(self.username)
