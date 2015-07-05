from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import User
from users.forms import LoginForm, RegisterForm, UpdateForm
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import bcrypt

from django.contrib.auth import authenticate, login, logout

class Login(View):
    template = 'users/login.html'
    login_form = LoginForm()

    def get(self, request):
        return render(request, self.template, {'login_form':self.login_form})

    def post(self, request):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/flex/')
            else:
                return render(request, self.template, {'login_error':"Account no longer active.", 'login_form':self.login_form})
        else:
            return render(request, self.template, {'login_error':"Invalid login information.", 'login_form':self.login_form})

class Register(View):
    template = 'users/register.html'
    register_form = RegisterForm()

    def get(self, request):
        return render(request, self.template, {'register_form':self.register_form})

    def post(self, request):
        form = RegisterForm(request.POST)
        try:
            User.objects.get(username=request.POST['username'])
            return render(request, self.template, {'registration_error': "Username already taken.", 'register_form': self.register_form})
        except:
            if form.is_valid():
                user = User(
                    type_of='investor',
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password'],
                )
                user.save()
                login(request, user)
                return redirect('/flex/')
            else:
                return render(request, self.template, {'registration_error':'Invalid input - Please populate all fields on the form.', 'register_form':self.register_form})

class Update(View):

    def post(self, request):
        user = User.objects.get(id=request.session['user_id'])
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/flex/account/')
        else:
            return redirect('/flex/account/')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect('/')
