from .models import Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def profile_pagination(request, profiles, results):
    page = request.GET.get('page')
    paginator = Paginator(profiles, results)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)

    left_index = (int(page) - 1)
    if left_index < 1:
        left_index = 1
    right_index = (int(page) + 2)
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    return custom_range, profiles


def search_profiles(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        print(search_query)
    profiles = Profile.objects.filter(
        Q(name__icontains=search_query) |
        Q(quote__icontains=search_query)
        )
    return profiles, search_query
