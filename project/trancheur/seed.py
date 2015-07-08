from .models import Bond, BondPrice
from trancheur.create_contracts import Contract_originator
from trancheur.seed_users import Seed_users
import csv
import datetime
from django.contrib.auth.models import User, Group
from trancheur.trancheur import Trancheur


class Seed:

    @classmethod
    def raw_date_to_date_object(cls, string):
        parsed_date = string.split('/')
        month = int(parsed_date[0].zfill(2))
        day = int(parsed_date[1].zfill(2))
        year = int('20' + parsed_date[2])
        return datetime.date(year, month, day)

    @classmethod
    def seed_bond_prices_from_csv(cls, bond, filename):
        with open(filename) as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                date = cls.raw_date_to_date_object(row[0])
                price = float(row[1])
                bond_price = BondPrice(
                    date=date,
                    price=price,
                    bond=bond,
                )
                bond_price.save()

    @classmethod
    def flex_investor_user(cls):
        user = User(username="flex")
        user.set_password("password")
        user.save()
        group = Group.objects.get(name='Investor')
        user.groups.add(group)

    @classmethod
    def scenario1(cls):
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
        "This creates bonds issued in the past. Seeds users, one for each contract created."
        for bond in bonds:
            bond['instance'].save()
            cls.seed_bond_prices_from_csv(bond['instance'], bond['filename'])
            Trancheur(bond['instance']).originate_contracts()
            Seed_users(bond['instance']).create_users_and_sell_contracts()


    @classmethod
    def scenario2(cls):
        bond_data = [
            {
                'cusip' : 'FLEXBOND1',
                'face' : 10000000,
                'coupon' : 0.0325,
                'initial_price' : 1.00,
                'auction_date' : datetime.date.today() + datetime.timedelta(days=3),
                'dated_date' : datetime.date.today() + datetime.timedelta(days=10),
                'maturity' : datetime.date.today() + datetime.timedelta(days=10960),
                'payments_per_year' : 2,
            },
            {
                'cusip' : 'FLEXBOND2',
                'face' : 5000000,
                'coupon' : 0.05,
                'initial_price' : 1.15,
                'auction_date' : datetime.date.today() + datetime.timedelta(days=3),
                'dated_date' : datetime.date.today() + datetime.timedelta(days=10),
                'maturity' : datetime.date.today() + datetime.timedelta(days=7310),
                'payments_per_year' : 2,
            },
            {
                'cusip' : 'FLEXBOND3',
                'face' : 230000,
                'coupon' : 0.04,
                'initial_price' : 1.09,
                'auction_date' : datetime.datetime.today() + datetime.timedelta(days=1),
                'dated_date' : datetime.date.today() + datetime.timedelta(days=8),
                'maturity' : datetime.date.today() + datetime.timedelta(days=10958),
                'payments_per_year' : 2,
            },
        ]
        for data in bond_data:
            bond = Bond(**data)
            bond.save()
            Contract_originator(bond).originate_contracts()














