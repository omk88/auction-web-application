from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=120, help_text='Required. Enter a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date', 'password1', 'password2')

class ProfileForm(UserCreationForm):
    email = forms.EmailField(max_length=120, help_text='Required. Enter a valid email address.')
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'email', 'birth_date', 'password1', 'password2')
