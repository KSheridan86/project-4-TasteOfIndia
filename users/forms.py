from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
            ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control register'})

        # self.fields['username'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['email'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['password1'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['password2'].widget.attrs.update(
        #     {'class': 'form-control register'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'short_intro',
                  'quote', 'bio', 'fav_food', 'social_github',
                  'social_linkedin', 'social_twitter',
                  'social_youtube', 'social_website', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control register'})

        # self.fields['name'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['username'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['email'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['short_intro'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['quote'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['bio'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['fav_food'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['profile_image'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['social_github'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['social_linkedin'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['social_twitter'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['social_youtube'].widget.attrs.update(
        #     {'class': 'form-control register'})
        # self.fields['social_website'].widget.attrs.update(
        #     {'class': 'form-control register'})
