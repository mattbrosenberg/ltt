from django.test import TestCase, Client
from trancheur.models import Bond, Contract, Trade, MoneyMarket, Residual, BondPrice
from django.utils import timezone
from trancheur.fixtures import BondFactory, ContractFactory, TradeFactory, MoneyMarketFactory, ResidualFactory, BondPriceFactory

# Create your tests here.

class Trancheur_app_tests(TestCase):
    def setUp(self):
        self.bond = BondFactory(
            cusip='FLEXBOND0',
            face = 10000.00,
            coupon = 0.035,
            initial_price = 1.02,
            auction_date = timezone.now() + timezone.timedelta(days=3),
            dated_date = timezone.now() + timezone.timedelta(days=10),
            maturity = timezone.now() + timezone.timedelta(days=10960),
            payments_per_year = 2,
        )

        self.residual = ResidualFactory(
            face = 10000.00,
            bond = self.bond,
            payments_per_year = 2,
        )

        self.money_market = MoneyMarketFactory(
            face = 8000000.00,
            bond = self.bond,
            coupon = 0.0025,
            issuance_date = timezone.now() + timezone.timedelta(days=10),
            maturity = timezone.now() + timezone.timedelta(days=40),
        )

        self.client = Client()

        print ("=====SETTING UP=====")

    def test_is_instance(self):
        self.assertIsInstance(self.bond, Bond)
        self.assertIsInstance(self.residual, Residual)
        self.assertIsInstance(self.money_market, MoneyMarket)

    def test_maturity(self):
        self.assertGreater(self.bond.maturity, timezone.now())
        self.assertGreater(self.money_market.maturity, timezone.now())

    def test_coupon(self):
        self.assertGreater(self.bond.coupon, 0)
        self.assertGreater(self.money_market.coupon, 0)

    def test_payments_per_year(self):
        self.assertEqual(self.bond.payments_per_year, 2)
        self.assertEqual(self.residual.payments_per_year, 2)

    def test_get_request(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
