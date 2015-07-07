from trancheur.models import Bond, Contract, Residual, MoneyMarket, Trade
from users.models import User
from libor.models import Libor
from trancheur.create_contracts import Contract_originator
from trancheur.trancheur_calculator import Trancheur
import datetime

muni_bond = Bond(
    cusip = 'FLEXBOND2',
    face = 5000000,
    coupon = 0.05,
    initial_price = 1.15,
    dated_date = datetime.date(2015, 7, 17),
    auction_date = datetime.date(2015, 7, 17) - datetime.timedelta(days=7),
    maturity = datetime.date(2040, 7, 17),
    payments_per_year = 2,
    )

# flex = User(
#     type_of = 'flex',
#     name = 'flex',
#     email = 'flex@flex.com',
#     password = 'flex',
# )

# residual_investor = User(
#     type_of = 'residual',
#     name = 'William Mantly',
#     email = 'wmantly@gmail.com',
#     password = 'william',
# )

def seed():
    muni_bond.save()
    flex = User.objects.get(email = 'flex@flex.com')
    residual_investor = User.objects.get(email = 'wmantly@gmail.com')
    Contract_originator(muni_bond).originate_contracts()
    residuals = Residual.objects.filter(bond = muni_bond)
    residual_trade = Trade(
        buyer = residual_investor,
        seller = flex,
        contract = residuals[0],
        price = 1.00,
        time = datetime.datetime.now(),
    )
    residual_trade.save()

# seed()
