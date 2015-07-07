from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from users.forms import UpdateForm
from trancheur.models import Bond, Contract, Trade, MoneyMarket, Residual
from django import forms
import datetime
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User

class Index(View):
    def get(self, request):
        return redirect("/flex/investing/")

class Investing(View):
    def get(self, request):
        return render(request, "flex/investing.html")

class AllDeals(View):
    def get(self, request):
        bonds = Bond.get_all_available_bonds()
        data = {'percent_residuals_funded':bond.percent_residuals_funded() for bond in bonds}
        # print(data)
        return JsonResponse({'data':data})

class Portfolio(View):
    def get(self, request):
        return render(request, "flex/portfolio.html")

class Trades(View):
    def get(self, request):
        investor_purchases = request.user.purchases.all()
        print(investor_purchases)
        investor_purchases = [{'id':purchase.contract.id, 'proceeds':round(purchase.price * purchase.contract.face, 2), 'time':purchase.time.strftime("%Y-%m-%d %H:%M:%S"), 'buyer':purchase.buyer.username, 'seller':purchase.seller.username} for purchase in investor_purchases]
        return JsonResponse({'investor_purchases':investor_purchases})

class Account(View):
    form = PasswordChangeForm

    def get(self, request):
        return render(request, "flex/account.html", {'form':self.form(user=request.user)})
