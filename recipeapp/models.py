from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField
from users.models import Profile


class Recipe(models.Model):
    '''
    Recipe model, used to add recipes to the database
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
        Helper function to organize recipes by newest first
        """
        ordering = ['-created_on']

    def __str__(self):
        return str(self.title)


class Tag(models.Model):
    '''
    Add warning tags to recipes, eg..Spicy, Vegetarian...
    '''
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.name)


class Comment(models.Model):
    """
    Leave comments on recipes
    """
    owner = models.ForeignKey(
        Profile, null=True, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        """
        Order comments by oldest first
        """
        ordering = ['created_on']

    def __str__(self):
        return str(self.owner)
