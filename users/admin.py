from django.contrib import admin
from .models import Profile, Message


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('name', 'username')
    list_display = ('name', 'username')
    search_fields = ('name', 'username')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('sender', 'recipient', 'body')
    list_display = ('sender', 'recipient', 'body')
    search_fields = ('sender', 'recipient', 'body')
