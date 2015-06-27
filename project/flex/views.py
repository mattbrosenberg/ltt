from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse

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
        return render(request, "flex/base.html")
