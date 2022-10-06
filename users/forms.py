from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
            ]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control register'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control register'})
        self.fields['password1'].widget.attrs.update(
            {'class': 'form-control register'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control register'})
