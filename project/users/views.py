from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import User
from users.forms import LoginForm, RegisterForm
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import bcrypt

class IndexView(View):
    template = 'users/index.html'
    login_form = LoginForm()
    register_form = RegisterForm()

    def get(self, request):
        return render(request, self.template, {'login_form':self.login_form, 'register_form':self.register_form})

class LoginView(View):
    login_form = LoginForm()
    register_form = RegisterForm()

    def post(self, request):
        entered_email = request.POST['email']
        entered_password = request.POST['password']
        try:
            checked_user = User.objects.get(email=entered_email)
            if checked_user.check_hash(entered_password, checked_user.password):
                request.session['user_id'] = checked_user.id
                return redirect('/flex/')
            else:
                return render(request, "users/index.html", {'error':"Invalid password", 'login_form':self.login_form, 'register_form':self.register_form})
        except ObjectDoesNotExist:
            return render(request, "users/index.html", {'error':"Invalid login information", 'login_form':self.login_form, 'register_form':self.register_form})

class RegisterView(View):
    register_form = RegisterForm()
    login_form = LoginForm()

    def post(self, request):
        form = RegisterForm(request.POST)
        try:
            User.objects.get(email=request.POST['email'])
            return render(request, "users/index.html", {'error':"Email is already in the database.  Please enter another email.", 'register_form':self.register_form, 'login_form':self.login_form})
        except:
            if form.is_valid():
                user = User(
                    type_of=form.cleaned_data.get('type_of'),
                    name=form.cleaned_data.get('name'),
                    email=form.cleaned_data.get('email'),
                    password=User.create_hash(form.cleaned_data.get('password'))
                )
                user.save()
                request.session['user_id'] = user.id
                return redirect('/flex/')
            else:
                return render(request, 'users/index.html', {'error':'Invalid input - Please populate all fields on the form.', 'register_form':self.register_form, 'login_form':self.login_form})

class WelcomeView(View):

    def get(self, request):
        current_session_id = request.session.get('user_id')
        if current_session_id:
            user = User.objects.get(id=current_session_id)
            if user.type_of == 'money-market':
                return render(request, 'users/mm_welcome.html', {'user':user})
            else:
                return render(request, 'users/res_welcome.html', {'user':user})
        else:
            return redirect('/')

class LogoutView(View):

    def get(self, request):
        request.session.flush()
        return redirect('/')
