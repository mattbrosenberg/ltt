from django.db import models
from trancheur.models import Bond
from trancheur.trancheur import Trancheur
import json

class BondCache(models.Model): 
    bond = models.OneToOneField(Bond)
    is_available = models.BooleanField(default=True)
    data = models.TextField()

    def save(self, *args, **kwargs):
        if self.bond.num_available_residuals() > 0:
            data = dict(
                funded =  float(self.bond.percent_residuals_funded()),
                est_yield = float(Trancheur(self.bond).est_yield()),
                term = int(self.bond.term()),
                tranche = float(Trancheur(self.bond).residual_investment()),
                amount_left = int(self.bond.amount_left_of_residuals()),
                time_left = int(self.bond.days_to_auction()),
                tranche_id = self.id,
                maturity_day = str(self.bond.maturity.day).zfill(2),
                maturity_month = str(self.bond.maturity.month).zfill(2),
                maturity_year = str(self.bond.maturity.year), 
                payments_per_year = self.bond.payments_per_year,
                face = self.bond.residual_face(),
                dated_date_day = str(self.bond.dated_date.day).zfill(2),
                dated_date_month = str(self.bond.dated_date.month).zfill(2),
                dated_date_year = str(self.bond.dated_date.year),
                num_available = self.bond.num_available_residuals(),
            )
            self.data = json.dumps(data)
        else:
            self.is_available = False
        super(BondCache, self).save(*args, **kwargs)

    @classmethod
    def get_all_unauctioned_bonds_as_json(cls):
        data = []
        for bond_cache in cls.objects.filter(is_available=True):
            data.append(json.loads(bond_cache.data))
        return dict(data=data)

    @classmethod
    def get_all_unauctioned_bonds_by_query_as_json(cls, queries):
        filtered_data = []
        print(queries)
        est_yield_query_reference = {
            "est_yield_11_15": dict(minimum=11.0, maximum=15.0),
            "est_yield_15_19": dict(minimum=15.0, maximum=19.0),
            "est_yield_19_23": dict(minimum=19.0, maximum=23.0),
            "est_yield_23_27": dict(minimum=23.0, maximum=27.0),
            }
        funded_query_reference = {
            "funded_0_25": dict(minimum=0.0, maximum=25.0),            
            "funded_25_50": dict(minimum=25.0, maximum=50.0),            
            "funded_50_75": dict(minimum=50.0, maximum=75.0),            
            "funded_75_100": dict(minimum=75.0, maximum=100.0),            
        }
        term_query_reference = {
            "term_200_250": dict(minimum=200, maximum=250),            
            "term_250_300": dict(minimum=250, maximum=300),            
            "term_300_350": dict(minimum=300, maximum=350),            
            "term_350_400": dict(minimum=350, maximum=400),            
        }
        time_left_query_reference = {
            "time_left_0_4": dict(minimum=0, maximum=4),            
            "time_left_4_8": dict(minimum=4, maximum=8),            
            "time_left_8_12": dict(minimum=8, maximum=12),            
            "time_left_12_16": dict(minimum=12, maximum=16),            
        }


        for bond_cache in cls.objects.filter(is_available=True):
            data = json.loads(bond_cache.data)
            for query in queries:
                if est_yield_query_reference.get(query):
                    if est_yield_query_reference[query]["minimum"] <= data["est_yield"] <= est_yield_query_reference[query]["maximum"]:
                        filtered_data.append(data)
                        break
                elif funded_query_reference.get(query):
                    if funded_query_reference[query]["minimum"] <= data["funded"] <= funded_query_reference[query]["maximum"]:
                        filtered_data.append(data)
                        break
                elif term_query_reference.get(query):
                    if term_query_reference[query]["minimum"] <= data["term"] <= term_query_reference[query]["maximum"]:
                        filtered_data.append(data)
                        break
                elif time_left_query_reference.get(query):
                    if time_left_query_reference[query]["minimum"] <= data["time_left"] <= time_left_query_reference[query]["maximum"]:
                        filtered_data.append(data)
                        break


        return dict(data=filtered_data)
            

