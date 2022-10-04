from django.urls import path
from . import views

urlpatterns = [
    path('', views.landingpage, name='landingpage'),
    path('recipes/', views.recipes, name='recipes'),
    path('recipe/', views.recipe, name='recipe'),
]
