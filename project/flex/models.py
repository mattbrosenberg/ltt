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
