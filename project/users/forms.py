from django import forms
from django.forms import ModelForm
from users.models import User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'password': forms.PasswordInput({'class':'form-control'}),
            'email': forms.TextInput({'class':'form-control'}),
            'name': forms.TextInput({'class':'form-control'}),
        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['type_of', 'name', 'email', 'password']
        widgets = {
            'type_of': forms.TextInput({'class':'form-control'}),
            'password': forms.PasswordInput({'class':'form-control'}),
            'email': forms.TextInput({'class':'form-control'}),
            'name': forms.TextInput({'class':'form-control'}),
        }

class UpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput({'class':'form-control'}),
            'email': forms.TextInput({'class':'form-control'}),
            'name': forms.TextInput({'class':'form-control'}),
        }
