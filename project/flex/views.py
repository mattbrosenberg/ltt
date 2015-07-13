from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from users.forms import UpdateForm
from trancheur.models import Bond, Contract, Trade, MoneyMarket, Residual
from django import forms
import datetime
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, PasswordResetForm
from django.contrib.auth.models import User
from trancheur.trancheur import Trancheur
from cashflow.cashflow_calculator import CashflowCreator

def format_tranches_for_json(bonds):
    data = []
    for bond in bonds:
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

class InvestingApi(View):

    def get(self, request):
        bonds = Bond.get_all_unauctioned_bonds()
        queries = request.META['QUERY_STRING'].split("+")
        query_options = {
            'least_percent_funded':{'key': lambda bond: bond.percent_residuals_funded(), 'reverse': False},
            'most_percent_funded':{'key': lambda bond: bond.percent_residuals_funded(), 'reverse': True},
            'least_days':{'key': lambda bond: bond.days_to_auction(), 'reverse': False},
            'most_days':{'key': lambda bond: bond.days_to_auction(), 'reverse': True},
        }
        for query in queries:
            bonds = sorted(bonds, **query_options[query])
        data = format_tranches_for_json(bonds)
        return JsonResponse(data)

class AllAvailableTranchesByMostFunded(View):

    def get(self, request):
        bonds = Bond.get_all_unauctioned_bonds_by_most_funded()
        data = format_tranches_for_json(bonds)
        return JsonResponse(data)

class AllAvailableTranchesByLeastFunded(View):

    def get(self, request):
        bonds = Bond.get_all_unauctioned_bonds_by_least_funded()
        data = format_tranches_for_json(bonds)
        return JsonResponse(data)

class Portfolio(View):

    def get(self, request):
        return render(request, "flex/portfolio.html")

class Investments(View):

    def get(self, request):
        user = self.request.user
        context_dict = [{'contract':purchase.contract.id, 'price':round(purchase.price * purchase.contract.face, 2), 'maturity': purchase.contract.bond.maturity, 'purchase_date': purchase.time.strftime("%Y-%m-%d %H:%M:%S")} for purchase in user.purchases.all() if purchase.contract.trades.latest().buyer == user]
        return JsonResponse({'investments':context_dict})    

class Contract(View):

    def average_return(self,list_of_cashflows,contract):
        annualized_returns = [(1 + i['amount'] / contract.face) ** 2 - 1  for i in list_of_cashflows]
        average_return = sum(annualized_returns)/len(annualized_returns)
        return round(average_return*100,3)  

    def get(self, request) :
        contract = Residual.objects.get(id = request.GET['contract'])
        cashflows = CashflowCreator(contract.bond).residual_cashflows()
        cashflows_since_purchase = [cashflow for cashflow in cashflows if cashflow['date'] > contract.trades.latest().time.date()]
        total = (sum(item['amount'] for item in cashflows_since_purchase))
        return JsonResponse({'data':{'cashflows':cashflows_since_purchase,'total':total, 'average_return': self.average_return(cashflows_since_purchase,contract)}})   

class Trades(View):

    def get(self, request):
        investor_purchases = request.user.purchases.all()
        investor_purchases = [{'id':purchase.contract.id, 'proceeds':round(purchase.price * purchase.contract.face, 2), 'time':purchase.time.strftime("%Y-%m-%d %H:%M:%S"), 'buyer':purchase.buyer.username, 'seller':purchase.seller.username} for purchase in investor_purchases]
        return JsonResponse({'investor_purchases':investor_purchases})

class Account(View):
    form = PasswordChangeForm

    def get(self, request):
        return render(request, "flex/account.html", {'form':self.form(user=request.user)})
