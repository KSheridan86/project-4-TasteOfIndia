from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('name', 'username')
    list_display = ('name', 'username')
    search_fields = ('name', 'username')
