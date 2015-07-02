from django.shortcuts import render

# Create your views here.
class Bond():
	def __init__(self, price, face_value, maturity, coupon):
		self.price = price
		self.face_value = face_value
		self.maturity = maturity
		self.coupon = coupon

class Trancheur():
	def __init__(self,bond,libor):
		self.bond = bond
		self.libor = libor
		self.money_market_spread = 0.0005
		self.floater_allocation = 0.80
		self.residual_allocation = 0.20
		self.floater_face = 1000
		self.residual_face = 50000

	def number_of_floater_contracts(self):
		return int((self.bond.price - self.bond.face_value * (1-self.floater_allocation)) / self.floater_face)

	def number_of_residual_contracts(self):
		return int((self.bond.face_value * self.residual_allocation)/ self.residual_face)

	def money_market_coupon(self):
		return (self.libor + self.money_market_spread)


# nyc = Bond(1000000, 1000000, 20, 0.05)
# t = Trancheur(nyc, 0.0015)	
# print ("---number of floater contracts----")
# print(t.number_of_floater_contracts())
# print ("---number of residual contracts----")
# print(t.number_of_residual_contracts())	
# print ("---money market coupon---")
# print (t.money_market_coupon())