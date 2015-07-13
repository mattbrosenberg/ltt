from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from trancheur.models import Bond, Contract, Trade

from users.forms import UpdateForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, PasswordResetForm
from users.models import User
from trancheur.trancheur import Trancheur
from .helper import QueryTranches
from .models import BondCache

class InvestingApi(View):

    def get(self, request):
        # queries = request.META['QUERY_STRING'].split("+")
        # if queries:
        #     bonds = QueryTranches().get_all_unauctioned_bonds_by_query(queries)
        # else:
        #     bonds = Bond.get_all_unauctioned_bonds()
        # data = format_tranches_for_json(bonds)
        return JsonResponse(BondCache.get_all_unauctioned_bonds_as_json())

class Index(View):

    def get(self, request):
        # namespace the redirect.....
        return redirect("/flex/investing/")

class Investing(View):

    def get(self, request):
        return render(request, "flex/investing.html")

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
