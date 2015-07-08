from .models import Bond, Contract, Residual, MoneyMarket, Trade 
from django.contrib.auth.models import User, Group

from faker import Faker
import datetime
from django.utils import timezone
fake = Faker()

class Seed_users:
	def __init__(self,bond):
		self.bond = bond
		self.contracts = Residual.objects.filter(bond = self.bond)
		self.owner = User.objects.get(username = 'flex')

	#the number of users is equal to a number of residual contracts in a bond
	def create_users_and_sell_contracts(self):
		print("Creating users and selling each one contract...")
		for contract in self.contracts:
			username = fake.user_name()
			user = User(username=username)
			user.set_password("password")
			try:
				user.save()
			except:
				user = User.objects.get(username=username)
			group = Group.objects.get(name='Investor')
			user.groups.add(group)
			today = timezone.now()
			dt = today.replace(year = contract.bond.auction_date.year, month = contract.bond.auction_date.month, day = contract.bond.auction_date.day)
			contract_sale = Trade(buyer = user, seller = self.owner, contract = contract, price = 1, time = dt)
			contract_sale.save()
