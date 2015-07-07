#originates contracts that belong to the user flex

from .trancheur_calculator import Trancheur
from .models import Bond, Contract, Residual, MoneyMarket
import datetime
from libor.models import Libor

# flex = User.objects.get(name = 'flex')
# bond = Bond.objects.get(cusip = '64966JNF9')

class Contract_originator():
	def __init__(self,bond):
		self.bond = bond

	def money_market_coupon(self):
		libor = Libor()
		libor_rate = libor.get_rate_by_date(self.bond.auction_date - datetime.timedelta(days = 14))
		return libor_rate + Trancheur(self.bond).money_market_spread

	def originate_contracts(self):
		number_of_contracts = Trancheur(self.bond).number_of_residual_contracts()
		for n in range(number_of_contracts):
			residual_contract = Residual(
					face = Trancheur(self.bond).residual_face,
					issuance_date = self.bond.auction_date - datetime.timedelta(days = 14),
					maturity = self.bond.maturity,
					bond = self.bond,
					payments_per_year = 2)
			residual_contract.save()
		money_market_contract = MoneyMarket(
			face = Trancheur(self.bond).money_market_investment(),
			issuance_date = self.bond.auction_date - datetime.timedelta(days = 14),
			maturity = self.bond.dated_date + datetime.timedelta(days = 30),
			bond = self.bond,
			coupon = self.money_market_coupon())
		money_market_contract.save()
