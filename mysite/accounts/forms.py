from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150)
    dob = forms.DateField(help_text='Format: YYYY-DD-MM')
    city = forms.CharField(max_length=150)


    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'email', 'dob', 'city')
