from trancheur.models import Trade, Contract
from users.models import User
from django.utils import timezone
from bank.models import Transaction

class Trader:

    @staticmethod
    def get_available_residual(bond):
        contracts = Contract.objects.filter(bond=bond, is_sold=False)
        for contract in contracts:
            if hasattr(contract, "residual"):
                print(contract)
                return contract

    @staticmethod
    def make_first_trade(buyer, bond, price=1):
        seller = User.objects.get(username="flex")
        try:
            contract = get_available_residual(bond)
            trade = Trade(
                buyer=buyer,
                seller=User.objects.get(username="flex"),
                contract=contract, 
                price=price, 
                time=timezone.now()
            )
            trade.save()
            print("1 of 4 - Trade Saved.")
            transaction = Transaction(
                user=buyer,
                amount= -(contract.face * trade.price),
                category= "PURCHASE",
                description= "Primary purchase of {} contract".format(bond.__str__()),
            )
            transaction.save()
            print("2 of 4 - Transaction Saved.")
            contract.save()
            print("3 of 4 - Contract Saved.")
            bond.bondcache.save()
            print("4 of 4 - Bondcache Saved.")
            return trade
        except:
            return None