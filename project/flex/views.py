from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

from django import forms
from users.forms import UpdateForm

from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, PasswordResetForm


from django.contrib.auth.models import User

class Index(View):

    def get(self, request):
        return redirect("/flex/auctions/")

class Auctions(View):

    def get(self, request):
        return render(request, "flex/auctions.html")

class Portfolio(View):

    def get(self, request):
        return render(request, "flex/base.html")

class Account(View):
    form = PasswordChangeForm

    def get(self, request):
        return render(request, "flex/account.html", {'form':self.form(user=request.user)})
