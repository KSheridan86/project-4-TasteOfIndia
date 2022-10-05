from django.contrib import admin
from .models import Recipe, Tag


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('created_on', 'title')
    list_display = ('title', 'created_on')
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',)
