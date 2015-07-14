from flex.views import InvestingApi
from trancheur.models import Bond, Trancheur
from django.http import JsonResponse
from django.core.cache import caches

def get_deals():
    bonds = Bond.get_all_unauctioned_bonds()
    data = []
    for bond in bonds:
        data.append(
            {
            'funded' : bond.percent_residuals_funded(),
            'est_yield' : round(Trancheur(bond).est_yield(),3),
            'term' : bond.term(),
            'tranche' : Trancheur(bond).residual_investment(),
            'amount_left' : int(bond.amount_left_of_residuals()),
            'time_left' : bond.days_to_auction(),
            }
        )
        dict(
            funded=bond.percent_residuals_funded(),
            )
        print(data)
    return {'data': data}

def fetch_cached_data():
    data = cache.get(data)
    if data is None:
        data = get_deals()
        cache.set(data, 60*15)
    # data = cache.get(data)
    print(data)
    return data

fetch_cached_data()
