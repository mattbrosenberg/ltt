from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse, JsonResponse
from trancheur.models import Bond, Contract, Trade, Residual, BondPrice
from users.forms import UpdateForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm, PasswordResetForm
from users.models import User
from trancheur.trancheur import Trancheur
from cashflow.cashflow_calculator import CashflowCreator
from .helper import QueryTranches
from .models import BondCache
from .services.trader import Trader

class InvestingApi(View):

    def get(self, request):
        queries = request.META['QUERY_STRING'].split("+")
        if queries[0]:
            data = BondCache.get_all_unauctioned_bonds_by_query_as_json(queries)
        else:
            data = BondCache.get_all_unauctioned_bonds_as_json()
        return JsonResponse(data)

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

class Activity(View):

    def get(self, request):
        transactions = request.user.transactions.all()
        context_dict = [{'date':transaction.time.strftime("%Y-%m-%d %H:%M:%S"), 'category': transaction.category, 'description':transaction.description, 'amount': transaction.amount} for transaction in transactions]    
        balance = User.objects.get(username = request.user.username).get_balance()
        print (balance)
        return JsonResponse({'transactions':context_dict, 'balance': balance})

class Investments(View):

    def current_value(self, contract):
        return (round((float(contract.bond.prices.latest().price * contract.bond.face) - Trancheur(contract.bond).money_market_investment()) / Trancheur(contract.bond).number_of_residual_contracts(),2))

    def change_in_value(self, purchase):
        p1 = float(purchase.price * purchase.contract.face)
        p2 = self.current_value(purchase.contract)
        return ((p2-p1)/p1 * 100)

    def get(self, request):
        user = self.request.user
        context_dict = [{'contract':purchase.contract.id, 'price':round(purchase.price * purchase.contract.face, 2), 'current_value': self.current_value(purchase.contract), 'maturity': purchase.contract.bond.maturity, 'purchase_date': purchase.time.strftime("%Y-%m-%d %H:%M:%S"), 'change_in_value': self.change_in_value(purchase)} for purchase in user.purchases.all() if purchase.contract.trades.latest().buyer == user]
        return JsonResponse({'investments':context_dict})    

class Contract(View):

    def average_return(self,list_of_cashflows,contract):
        annualized_returns = [(1 + i['amount'] / contract.face) ** 2 - 1  for i in list_of_cashflows]
        if len(annualized_returns) == 0:
            return 0
        else:    
            average_return = sum(annualized_returns)/len(annualized_returns)
            return round(average_return*100,3)  

    def get(self, request):
        contract = Residual.objects.get(id = request.GET['contract'])
        cashflows = CashflowCreator(contract.bond).residual_cashflows()
        cashflows_since_purchase = [cashflow for cashflow in cashflows if cashflow['date'] > contract.trades.latest().time.date()]
        total = (sum(item['amount'] for item in cashflows_since_purchase))
        return JsonResponse({'data':{'cashflows':cashflows_since_purchase,'total':total, 'average_return': self.average_return(cashflows_since_purchase,contract), 'current_value':Investments().current_value(contract)}})   

class Trades(View):

    def get(self, request):
        investor_purchases = request.user.purchases.all()
        investor_purchases = [{'id':purchase.contract.id, 'proceeds':round(purchase.price * purchase.contract.face, 2), 'time':purchase.time.strftime("%Y-%m-%d %H:%M:%S"), 'buyer':purchase.buyer.username, 'seller':purchase.seller.username} for purchase in investor_purchases]
        return JsonResponse({'investor_purchases':investor_purchases})

class Account(View):
    form = PasswordChangeForm

    def get(self, request):
        return render(request, "flex/account.html", {'form':self.form(user=request.user)})

class Purchase(View):

    def post(self, request):
        bond = Bond.objects.get(id=request.POST['tranche_id'])
        for count in range(int(request.POST['num_contracts'])):
            Trader.make_first_trade(request.user, bond)
        return redirect("/flex/investing/")

    def get(self, request):
        pass