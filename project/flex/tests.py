from django.test import TestCase, Client
from trancheur.models import Bond, Contract, Trade, MoneyMarket, Residual
from trancheur.trancheur import Trancheur
from django.utils import timezone
from trancheur.fixtures import BondFactory, ContractFactory, TradeFactory, MoneyMarketFactory, ResidualFactory, BondPriceFactory
import json
import pprint

# Create your tests here.

pp = pprint.PrettyPrinter(indent=4)
kwargs = {'HTTP_X_REQUESTED_WITH':'XMLHttpRequest'}

class FlexTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'adickens'
        self.password = 'password'
        self.old_password = 'old'
        self.new_password = 'new'

        print ("=====SETTING UP=====")

    def test_investing_view(self):
        response = self.client.get('/flex/investing/')
        self.assertEqual(response.status_code, 200)

    def test_portfolio_view(self):
        response = self.client.get('/flex/portfolio/')
        self.assertEqual(response.status_code, 200)

    def test_account_view(self):
        response = self.client.get('/flex/account/')
        self.assertEqual(response.status_code, 200)

    def test_client_registration(self):
        response = self.client.post('/register/', {'username':self.username, 'password':self.password}, **kwargs)
        self.assertEqual(response.request['REQUEST_METHOD'],'POST')
        self.assertEqual(response.request['PATH_INFO'], '/register/')
        self.assertEqual(response.status_code, 200)

    def test_client_login(self):
        response = self.client.post('/login/', {'username':self.username, 'password':self.password}, **kwargs)
        # pp.pprint(response.request)
        self.assertEqual(response.request['REQUEST_METHOD'],'POST')
        self.assertEqual(response.request['PATH_INFO'], '/login/')
        self.assertEqual(response.status_code, 200)

    # def test_update_account(self):
    #     response = self.client.post('/flex/account/', {'username':self.username, 'password':self.password}, **kwargs)
    #     self.assertEqual(response.request['REQUEST_METHOD'],'POST')
    #     self.assertEqual(response.request['PATH_INFO'], '/register/')
    #     self.assertEqual(response.status_code, 200)


    # def test_client_login(self, **kwargs):
    #     response = self.client.post('/login/', {'username':'adickens', 'password':'password'}, **kwargs)
    #     response_content = response.content
    #     pp.pprint(response_content)
    #     response_content = json.loads(response_content.decode())
        # pp.pprint(response_content['item'])
