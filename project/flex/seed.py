from trancheur.models import Bond, Contract, Residual, MoneyMarket, Trade
from users.models import User, Investor, Analyst
from libor.models import Libor
from trancheur.create_contracts import Contract_originator
from trancheur.trancheur_calculator import Trancheur
import datetime

muni_bond1 = Bond(
    cusip = 'FLEXBOND1',
    face = 10000000,
    coupon = 0.0325,
    initial_price = 1.00,
    dated_date = datetime.date(2015, 7, 15),
    auction_date = datetime.date(2015, 7, 15) - datetime.timedelta(days=7),
    maturity = datetime.date(2045, 7, 15),
    payments_per_year = 2,
    )

muni_bond2 = Bond(
    cusip = 'FLEXBOND2',
    face = 5000000,
    coupon = 0.05,
    initial_price = 1.15,
    dated_date = datetime.date(2015, 7, 17),
    auction_date = datetime.date(2015, 7, 17) - datetime.timedelta(days=7),
    maturity = datetime.date(2040, 7, 17),
    payments_per_year = 2,
    )

flex = Investor(user=User.objects.create_user(
    username = 'flex',
    email = 'flex@flex.com',
    password = 'flex',
    )
)

residual_investor = Investor(user=User.objects.create_user(
    username = 'William Mantly',
    email = 'wmantly@gmail.com',
    password = 'william',
    )
)

def seed():
    muni_bond1.save()
    muni_bond2.save()
    flex.save()
    residual_investor.save()
    # flex = User.objects.get(email = 'flex@flex.com')
    # residual_investor = User.objects.get(email = 'wmantly@gmail.com')
    Contract_originator(muni_bond1).originate_contracts()
    Contract_originator(muni_bond2).originate_contracts()
    residuals = Residual.objects.filter(bond = muni_bond1)
    residual_trade = Trade(
        buyer = residual_investor,
        seller = flex,
        contract = residuals[0],
        price = 1.00,
        time = datetime.datetime.now(),
    )
    residual_trade.save()

# seed()
