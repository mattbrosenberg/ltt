from django import forms
from django.forms import ModelForm
from users.models import User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['type_of', 'name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
