from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class Index(View):

    def get(self, request):
        return HttpResponse("Welcome to the flex dashboard. <a href='/clients/logout/'>Log Out</a>")