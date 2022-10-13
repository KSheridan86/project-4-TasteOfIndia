from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Recipe, Tag
from .forms import RecipeForm, CommentForm
from .utils import search_recipes, recipe_pagination


def recipes(request):
    recipes, search_query = search_recipes(request)
    custom_range, recipes = recipe_pagination(request, recipes, 6)
    context = {
        'recipes': recipes,
        'search_query': search_query,
        'custom_range': custom_range
    }
    return render(request, 'recipeapp/recipes.html', context)


def recipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.recipe = recipe
        comment.owner = request.user.profile
        comment.save()
        messages.success(request, 'Comment Saved!')
        return redirect('recipe', pk=recipe.id)

    context = {
        'recipe': recipe,
        'form': form
    }
    return render(request, 'recipeapp/recipe.html', context)


@login_required(login_url='sign_in')
def create_recipe(request):
    profile = request.user.profile
    form = RecipeForm()

    if request.method == 'POST':
        user_tags = request.POST.get('tag_string').replace(
            ',', ' ').replace('-', ' ').split()
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.owner = profile
            recipe.save()
            for tag in user_tags:
                tag, created_on = Tag.objects.get_or_create(name=tag)
                recipe.tags.add(tag)
            return redirect('user_profile', pk=profile.id)
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
        old_tags = recipe.tags.all()
        print(old_tags)
        old_tags.delete()
        refresh = recipe.tags.all()
        print(refresh)

        user_tags = request.POST.get('tag_string').replace(
            ',', ' ').replace('-', ' ').split()
        for i in range(len(user_tags)):
            user_tags[i] = user_tags[i].capitalize()

        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            recipe = form.save()
            for tag in user_tags:
                tag, created_on = Tag.objects.get_or_create(name=tag)
                recipe.tags.add(tag)
            return redirect('user_profile', pk=profile.id)

    context = {
        'form': form,
        'recipe': recipe
    }
    return render(request, 'recipeapp/recipe_form.html', context)


@login_required(login_url='sign_in')
def delete_recipe(request, pk):
    page = 'delete-recipe'
    profile = request.user.profile
    recipe = profile.recipe_set.get(id=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('user_profile', pk=profile.id)
    context = {
        'object': recipe,
        'page': page
    }
    return render(request, 'recipeapp/delete_object.html', context)


def landingpage(request):
    return render(request, 'landingpage.html')
