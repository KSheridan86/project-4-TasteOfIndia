from django.shortcuts import render
from .models import Recipe


def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes': recipes
    }
    return render(request, 'recipeapp/recipes.html', context)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    context = {
        'recipe': recipe
    }
    return render(request, 'recipeapp/recipe.html', context)


def landingpage(request):
    return render(request, 'recipeapp/landingpage.html')
