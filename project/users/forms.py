from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User


# class LoginForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password',)
#         widgets = {
#             'username': forms.TextInput({'class':'form-control'}),
#             'password': forms.PasswordInput({'class':'form-control'}),
#         }

# class RegisterForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password',)
#         widgets = {
#             'username': forms.TextInput({'class':'form-control'}),
#             'password': forms.PasswordInput({'class':'form-control'}),
#         }

class UpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
        widgets = {
            'username': forms.TextInput({'class':'form-control'}),
            'email': forms.TextInput({'class':'form-control'}),
            'password': forms.PasswordInput({'class':'form-control'}),
        }