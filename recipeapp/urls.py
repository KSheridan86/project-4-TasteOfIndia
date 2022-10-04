from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/<str:pk>/', views.recipe, name='recipe'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
]
