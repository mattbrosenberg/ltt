from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput({'class':'form-control'}),
            'password': forms.PasswordInput({'class':'form-control'}),
        }

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput({'class':'form-control'}),
            'password': forms.PasswordInput({'class':'form-control'}),
        }

class UpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        widgets = {
            'username': forms.TextInput({'class':'form-control'}),
            'password': forms.PasswordInput({'class':'form-control'}),
        }

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'type_of',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]