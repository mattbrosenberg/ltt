from faker import Faker
from .models import Bond, Contract, Residual, MoneyMarket, Trade 
import datetime
from django.contrib.auth.models import User
from users.models import Investor

fake = Faker()

#create users

class Seed_users():
	def __init__(self,bond):
		self.bond = bond
		self.contracts = Residual.objects.filter(bond = self.bond)
		self.owner = Investor.objects.get(username = 'flex')

	#the number of users is equal to a number of residual contracts in a bond 
	def create_users_and_sell_contracts(self):

		for contract in self.contracts:
			new_user = User(
				username = fake.first_name())
			new_user.set_password(fake.password())
			new_user.save()
			investor = Investor(user = new_user)
			investor.save()
			today = datetime.datetime.today()
			dt = today.replace(year = contract.issuance_date.year, month = contract.issuance_date.month, day = contract.issuance_date.day)
			contract_sale = Trade(buyer = investor, seller = self.owner.investor, contract = contract, price = 1, time = dt)
			contract_sale.save()

