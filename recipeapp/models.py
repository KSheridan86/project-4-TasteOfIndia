from django.db import models
import uuid
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    '''
    Docstrings R us!
    '''
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(
        'Profile', null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)
    ingredients = models.TextField()
    method = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    tags = models.ManyToManyField('Tag', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)

    class Meta:
        """
        Docstrings R us!!
        """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)

    def number_of_likes(self):
        """
        Docstrings R us!
        """
        return self.likes.count()


class Tag(models.Model):
    '''
    Docstrings R us!
    '''
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Profile(models.Model):
    """
    Docstrings R us!!
    """
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=80, blank=True, null=True)
    username = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
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
