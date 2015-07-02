from django.shortcuts import render
from .models import Bond 

#bond = Bond.objects.filter(cusip = '64966JNF9')		

class Trancheur():
	def __init__(self,bond):
		self.bond = bond
		self.floater_allocation = 0.80
		self.residual_allocation = 0.20
		self.residual_face = 10000
		self.money_market_spread = 0.0005

	def money_to_be_raised(self):
		return float(self.bond.face * self.bond.initial_price)

	def number_of_residual_contracts(self):
		return int((self.money_to_be_raised() * self.residual_allocation) // self.residual_face)

	def money_market_investment(self):
		return self.money_to_be_raised() - self.number_of_residual_contracts() * self.residual_face

