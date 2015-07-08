from .models import Bond, Contract, Residual, MoneyMarket
from libor.models import Libor

import datetime

class Trancheur:
    def __init__(self, bond, residual_to_floater_gearing=4, residual_face=10000, money_market_spread=.0005):
        self.bond = bond
        self.floater_allocation = residual_to_floater_gearing / (residual_to_floater_gearing + 1)
        self.residual_allocation = 1 / (residual_to_floater_gearing + 1)
        self.residual_face = residual_face
        self.money_market_spread = money_market_spread

    def total_cost(self):
        return float(self.bond.face * self.bond.initial_price)

    def residual_investment(self):
        return self.total_cost * self.residual_allocation

    def number_of_residual_contracts(self):
        return int(self.residual_investment() // self.residual_face)

    def money_market_investment(self):
        return self.total_cost() - self.number_of_residual_contracts() * self.residual_face

    def money_market_coupon(self):
        libor_rate = Libor().get_rate_by_date(self.bond.auction_date - datetime.timedelta(days = 14))
        return libor_rate + self.money_market_spread

    def originate_contracts(self):
        for i in range(self.number_of_residual_contracts()):
            residual_contract = Residual(
                    face = self.residual_face,
                    
                    # why not just the auction date?
                    issuance_date = self.bond.auction_date - datetime.timedelta(days = 14),

                    maturity = self.bond.maturity,
                    bond = self.bond,
                    payments_per_year = 2)
            residual_contract.save()

        money_market_contract = MoneyMarket(
            face = self.money_market_investment(),

            # why not just the auction date?
            issuance_date = self.bond.auction_date - datetime.timedelta(days = 14),

            maturity = self.bond.dated_date + datetime.timedelta(days = 30),
            bond = self.bond,
            coupon = self.money_market_coupon())
        money_market_contract.save()
