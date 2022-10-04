from django.contrib import admin
from .models import Recipe, Profile, Tag


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('name', 'username', 'fav_food')
    list_display = ('name', 'username', 'fav_food')
    search_fields = ('name', 'username', 'fav_food')


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('created_on', 'title', 'owner')
    list_display = ('title', 'owner', 'created_on')
    search_fields = ('title', 'owner')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',)
