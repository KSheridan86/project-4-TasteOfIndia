from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('', views.profiles, name='profiles'),
    path('user_profile/<str:pk>/', views.user_profile, name='user_profile'),
]