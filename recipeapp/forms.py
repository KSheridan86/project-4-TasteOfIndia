from django.forms import ModelForm
from django import forms
from .models import Recipe, Tag


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description',
                  'ingredients', 'method', 'featured_image', 'tags']

        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control register',
             'placeholder': 'Add title here...'})
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control register',
             'placeholder': 'Please give a short description...'})
        self.fields['ingredients'].widget.attrs.update(
            {'class': 'form-control register',
             'placeholder': 'Please add each ingredient on a new line...'})
        self.fields['method'].widget.attrs.update(
            {'class': 'form-control register',
             'placeholder': 'Please add each step on a new line...'})
        self.fields['featured_image'].widget.attrs.update(
            {'class': 'form-control register'})
