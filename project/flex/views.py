from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from users.forms import UpdateForm

from users.models import User
from django import forms

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

    def get(self, request):
        user = User.objects.get(id=request.session['user_id'])
        data = {'name':user.name, 'email':user.email}
        form = UpdateForm(initial=data)
        return render(request, "flex/account.html", {'form':form})
