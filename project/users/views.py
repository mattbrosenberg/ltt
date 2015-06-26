from django.shortcuts import render, redirect
from django.views.generic import View
from users.models import User
from users.forms import LoginForm, RegisterForm
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
import bcrypt

# Create your views here.

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
            if checked_user != None:
                print(entered_password, checked_user.password)
                if checked_user.check_hash(entered_password, checked_user.password):
                    request.session['user_id'] = checked_user.id
                    print(request.session['user_id'])
                    return redirect('/welcome')
                else:
                    return render(request, "users/index.html", {'error':"Invalid password", 'login_form':self.login_form, 'register_form':self.register_form})

        except ObjectDoesNotExist:
            return render(request, "users/index.html", {'error':"Invalid login information", 'login_form':self.login_form, 'register_form':self.register_form})

class RegisterView(View):
    register_form = RegisterForm()
    login_form = LoginForm()

    def post(self, request):
        encrypted = User()
        submitted_form = RegisterForm(request.POST)
        entered_email = request.POST['email']
        try:
            if User.objects.get(email=entered_email):
                return render(request, "users/index.html", {'error':"Email is already in the database.  Please enter another email.", 'register_form':self.register_form, 'login_form':self.login_form})
        except:
            if submitted_form.is_valid():
                entered_type = submitted_form.cleaned_data.get('type_of')
                entered_name = submitted_form.cleaned_data.get('name')
                entered_password = submitted_form.cleaned_data.get('password')
                password = encrypted.create_hash(entered_password)
                print(entered_name, entered_password)
                User(type_of=entered_type, name=entered_name, email=entered_email, password=password).save()
                registered_user = User.objects.get(email=entered_email)
                request.session['user_id'] = registered_user.id
                print(request.session['user_id'])

                return redirect('/welcome')
            else:
                return render(request, 'users/index.html', {'error':'Invalid input - Please populate all fields on the form.', 'register_form':self.register_form, 'login_form':self.login_form})

class WelcomeView(View):

    def get(self, request):
        current_session_id = request.session.get('user_id')
        print('Session id:')
        print(current_session_id)
        request.session.set_expiry(180)
        if current_session_id:
            user = User.objects.get(id=current_session_id)
            if user.type_of == 'money-market':
                return render(request, 'users/mm_welcome.html', {
                'user':user})
            else:
                return render(request, 'users/res_welcome.html', {
                'user':user})
        else:
            return redirect('/')

class LogoutView(View):

    def get(self, request):
        request.session.flush()
        return redirect('/')
