from .models import Profile
from django.db.models import Q


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
