from django.contrib import admin
from .models import Recipe, Tag, Comment


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'title')
    list_display = ('title', 'created_on')
    search_fields = ('title',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_filter = ('created_on', 'body', 'recipe')
    list_display = ('body', 'recipe', 'created_on')
    search_fields = ('body', 'recipe', 'owner')
