from faker import Faker
from trancheur.models import Bond, Contract, Residual, MoneyMarket, Trade
from users.models import User, Investor, Analyst
import datetime

fake = Faker()

#create users

class Seed_users():
	def __init__(self,bond):
		self.bond = bond
		self.contracts = Residual.objects.filter(bond = self.bond)
		self.owner = User.objects.get(username = 'flex')

	#the number of users is equal to a number of residual contracts in a bond
	def create_users_and_sell_contracts(self):

		for contract in self.contracts:
			new_user = Investor(user=User.objects.create_user(
				username = fake.first_name(),
				email = fake.email(),
				password = fake.password())
				)
			)
			new_user.save()
			today = datetime.datetime.today()
			dt = today.replace(year = contract.issuance_date.year, month = contract.issuance_date.month, day = contract.issuance_date.day)
			contract_sale = Trade(buyer = new_user, seller = self.owner, contract = contract, price = 1, time = dt)
			contract_sale.save()
