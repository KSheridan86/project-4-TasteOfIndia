from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm


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


def create_recipe(request):
    profile = request.user.profile
    form = RecipeForm()

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            return redirect('recipes')
    context = {
        'form': form
    }
    return render(request, 'recipeapp/recipe_form.html', context)


def landingpage(request):
    return render(request, 'recipeapp/landingpage.html')
