from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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


@login_required(login_url='sign_in')
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


@login_required(login_url='sign_in')
def update_recipe(request, pk):
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)
    form = RecipeForm(instance=recipe)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes')

    context = {
        'form': form
    }
    return render(request, 'recipeapp/recipe_form.html', context)


@login_required(login_url='sign_in')
def delete_recipe(request, pk):
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipes')
    context = {
        'object': recipe
    }
    return render(request, 'recipeapp/delete_object.html', context)


def landingpage(request):
    return render(request, 'landingpage.html')
