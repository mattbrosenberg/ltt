from trancheur.models import Trade
from users.models import User

class Trader:

    @staticmethod
    def make_first_trade(buyer, contract, price, time):
        seller = User.objects.get(username="flex")
        Trade(buyer=buyer, contract=contract, price=price, time=time)

        
