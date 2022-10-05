from django.db import models
import uuid
from users.models import Profile
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Recipe(models.Model):
    '''
    Docstrings R us!
    '''
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=200, blank=True)
    ingredients = models.TextField()
    method = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    tags = models.ManyToManyField('Tag', blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

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
