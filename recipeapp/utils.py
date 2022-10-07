from .models import Recipe, Tag
from django.db.models import Q


def search_recipes(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print(search_query)

    tags = Tag.objects.filter(name__icontains=search_query)

    recipes = Recipe.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(ingredients__icontains=search_query) |
        Q(method__icontains=search_query) |
        Q(tags__in=tags)
        )
    return recipes, search_query
