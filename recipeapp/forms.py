from django.forms import ModelForm
from django import forms
from .models import Recipe, Tag, Comment


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
             'placeholder': 'Please add each Ingredient on a new line...'})
        self.fields['method'].widget.attrs.update(
            {'class': 'form-control register',
             'placeholder': 'Please add each Step on a new line...'})
        self.fields['featured_image'].widget.attrs.update(
            {'class': 'form-control register'})


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': 'Enter your comment here . . . '
        }

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control register'})
