from .models import Bond, BondPrice

import csv
import datetime

def raw_date_to_date_object(string):
    parsed_date = string.split('/')
    month = int(parsed_date[0].zfill(2))
    day = int(parsed_date[1].zfill(2))
    year = int('20' + parsed_date[2])
    return datetime.date(year, month, day)

def seed_bond_prices_from_csv(bond, filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            date = raw_date_to_date_object(row[0])
            price = float(row[1])
            bond_price = BondPrice(
                date=date,
                price=price,
                bond=bond,
            )
            bond_price.save()

bonds = [
    {'filename':'trancheur/seeds/64966JNF9.csv',
     'instance': Bond(
            cusip='64966JNF9',
            face=5000000,
            coupon=.05,
            dated_date=datetime.date(2011, 8, 9),
            auction_date = datetime.date(2011, 8, 9) - datetime.timedelta(days=7),
            maturity=datetime.date(2032, 8, 1),
            payments_per_year=2,
            initial_price = 1.04884,
            )
    },
    {'filename':'trancheur/seeds/650035VB1.csv',
     'instance': Bond(
            cusip='650035VB1',
            face=10000000,
            coupon=.05838,
            dated_date=datetime.date(2010, 12, 8),
            auction_date = datetime.date(2010, 12, 8) - datetime.timedelta(days=7),
            maturity=datetime.date(2040, 3, 15),
            payments_per_year=2,
            initial_price = 1,
            )
    },
]

def seed():
    BondPrice.objects.all().delete()
    # Bond.objects.all().delete()
    for bond in bonds:
        bond['instance'].save()
        seed_bond_prices_from_csv(bond['instance'], bond['filename'])

# seed()
