from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from users.forms import UpdateForm
from trancheur.models import Bond, Contract, Trade, MoneyMarket, Residual
from django import forms
import datetime
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User


def format_tranches_for_json(bonds):
    data = []
    for bond in bonds:
        print(bond.maturity)
        print(bond.dated_date)
        print(bond.days_to_auction())
        print(Trancheur(bond).residual_investment())
        print(bond.percent_residuals_funded())
        print(bond.num_available_residuals())
        data.append(
            {
            'maturity' : bond.maturity,
            'dated_date' : bond.dated_date,
            'days_to_auction' : bond.days_to_auction(),
            'residual_investment' : Trancheur(bond).residual_investment(),
            'percent_residuals_funded' : bond.percent_residuals_funded(),
            'num_available_residuals' : bond.num_available_residuals(),
            }
        )
    return {'data': data}


class Index(View):

    def get(self, request):
        return redirect("/flex/investing/")

class Investing(View):

    def get(self, request):
        return render(request, "flex/investing.html")

class AllAvailableTranches(View):

    def get(self, request):
        print('hello')
        bonds = Bond.get_all_unauctioned_bonds()
        print(bonds)
        data = format_tranches_for_json(bonds)
        print(data)
        return JsonResponse(data)

class Portfolio(View):

    def get(self, request):
        return render(request, "flex/portfolio.html")

class Investments(View):

    def get(self, request):
        user = self.request.user
        context_dict = [{'contract':purchase.contract.id, 'price':round(purchase.price * purchase.contract.face, 2), 'maturity': purchase.contract.bond.maturity, 'purchase_date': purchase.time.strftime("%Y-%m-%d %H:%M:%S")} for purchase in user.purchases.all() if purchase.contract.trades.latest().buyer == user]
        return JsonResponse({'investments':context_dict})        

class Trades(View):

    def get(self, request):
        investor_purchases = request.user.purchases.all()
        investor_purchases = [{'id':purchase.contract.id, 'proceeds':round(purchase.price * purchase.contract.face, 2), 'time':purchase.time.strftime("%Y-%m-%d %H:%M:%S"), 'buyer':purchase.buyer.username, 'seller':purchase.seller.username} for purchase in investor_purchases]
        return JsonResponse({'investor_purchases':investor_purchases})

class Account(View):
    form = PasswordChangeForm

    def get(self, request):
        return render(request, "flex/account.html", {'form':self.form(user=request.user)})
