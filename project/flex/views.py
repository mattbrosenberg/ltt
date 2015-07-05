from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from users.forms import UpdateForm
from trancheur.models import Bond, Contract, Trade, MoneyMarket, Residual
from users.models import User
from django import forms
import datetime

class Index(View):

    def get(self, request):
        return redirect("/flex/investing/")


class Investing(View):
    def get(self, request):
        return render(request, "flex/investing.html")

class All_deals(View):
    def get(self, request):
        today = datetime.datetime.today()
        bonds = Bond.objects.filter(auction_date__gte = today)
        for bond in bonds:
            funded = 0
            residuals = Residual.objects.filter(bond = bond)
            for contract in residuals:
                if contract.trades.count == 0:
                    funded += 1
            percentage_funded = funded / residuals.count()                    

class Portfolio(View):
    def get(self, request):
        return render(request, "flex/portfolio.html")

class Trades(View):
    def get(self, request):
        user = User.objects.get(id=request.session['user_id'])
        user_purchases = user.purchases.all()
        user_purchases = [{'id':purchase.contract.id, 'proceeds':round(purchase.price * purchase.contract.face, 2), 'time':purchase.time, 'buyer':purchase.buyer.name, 'seller':purchase.seller.name} for purchase in user_purchases]
        return JsonResponse({'user_purchases':user_purchases})

class Account(View):
    def get(self, request):
        user = User.objects.get(id=request.session['user_id'])
        data = {'name':user.name, 'email':user.email}
        form = UpdateForm(initial=data)
        return render(request, "flex/account.html", {'form':form})
