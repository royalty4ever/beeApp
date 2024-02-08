from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.forms.widgets import PasswordInput, TextInput


# - Register/Create a user

class CreateUserForm(UserCreationForm):
    
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']

# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# ----------------- create a form for createing new record-------

class CreateRecordForm(forms.ModelForm):

    class Meta:
        
        model = Record
        fields = ['surname', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'state_of_origin', 'dob', 'qualification']

# ----------------- Update a record-------

class UpdateRecordForm(forms.ModelForm):

    class Meta:
        
        model = Record
        fields = ['surname', 'first_name', 'last_name', 'email', 'address', 'phone_number', 'state_of_origin', 'dob', 'qualification']