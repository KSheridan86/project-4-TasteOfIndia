from .models import Recipe, Tag
from users.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def recipe_pagination(request, recipes, results):
    page = request.GET.get('page')
    paginator = Paginator(recipes, results)
    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        recipes = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        recipes = paginator.page(page)

    left_index = (int(page) - 1)
    if left_index < 1:
        left_index = 1
    right_index = (int(page) + 2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, recipes


def search_recipes(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print(search_query)

    tags = Tag.objects.filter(name__icontains=search_query)
    profiles = Profile.objects.filter(name__icontains=search_query)

    recipes = Recipe.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(description__icontains=search_query) |
        Q(ingredients__icontains=search_query) |
        Q(method__icontains=search_query) |
        Q(owner__in=profiles) |
        Q(tags__in=tags)
        )
    return recipes, search_query
