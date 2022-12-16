from django import forms
from .models import Item
from users.models import CustomUser

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'starting_price', 'description', 'item_image', 'end_date', 'end_time']

        title = forms.CharField(max_length=100)
        starting_price = forms.DecimalField(max_digits=10, decimal_places=2)
        description = forms.CharField(max_length=600)
        item_image = forms.ImageField()
        end_date = forms.DateField()
        end_time = forms.TimeField()

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'dob', 'profile_picture']

        email = forms.EmailField()
        dob = forms.DateField()  
        item_image = forms.ImageField()

