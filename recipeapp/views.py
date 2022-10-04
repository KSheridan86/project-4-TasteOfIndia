from django.shortcuts import render


def recipes(request):
    return render(request, 'recipeapp/recipes.html')


def recipe(request):
    return render(request, 'recipeapp/recipe.html')


def landingpage(request):
    return render(request, 'recipeapp/landingpage.html')
