from django.urls import path
from . import views

urlpatterns = [
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('register/', views.register, name='register'),
    path('', views.profiles, name='profiles'),
    path('user_profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('edit_account/', views.edit_account, name='edit_account'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('inbox/', views.inbox, name='inbox'),
    path('view_message/<str:pk>/', views.view_message, name='view_message'),
]
