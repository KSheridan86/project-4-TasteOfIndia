from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Docstrings R us!!
    """
    list_filter = ('name', 'username', 'fav_food')
    list_display = ('name', 'username', 'fav_food')
    search_fields = ('name', 'username', 'fav_food')
