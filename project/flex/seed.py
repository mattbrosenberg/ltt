from trancheur.models import Bond, Contract, Residual, MoneyMarket, Trade
from users.models import User
from libor.models import Libor
from trancheur.create_contracts import Contract_originator
from trancheur.trancheur_calculator import Trancheur
import datetime

muni_bond = Bond(
    cusip = 'FLEXBOND1',
    face = 10000000,
    coupon = 0.0325,
    initial_price = 1.00,
    dated_date = datetime.date(2015, 7, 15),
    auction_date = datetime.date(2015, 7, 15) - datetime.timedelta(days=7),
    maturity = datetime.date(2045, 7, 15),
    payments_per_year = 2,
    )

flex = User(
    type_of = 'flex',
    name = 'flex',
    email = 'flex@flex.com',
    password = 'flex',
)

residual_investor = User(
    type_of = 'residual',
    name = 'William Mantly',
    email = 'wmantly@gmail.com',
    password = 'william',
)

def seed():
    muni_bond.save()
    flex.save()
    residual_investor.save()
    Contract_originator(muni_bond).originate_contracts()
    residual_trade = Trade(
        buyer = residual_investor,
        seller = User.objects.first(),
        contract = Contract.objects.first(),
        price = 1.00,
        time = datetime.datetime.now(),
    )
    residual_trade.save()

# seed()
