from django.core.management.base import BaseCommand, CommandError
from trancheur.seed import Seed

class Command(BaseCommand):
    help = "seeds the database with bonds, contracts and users"

    def handle(self, *args, **options):
        Seed.flex_investor_user()
        Seed.scenario1()

        self.stdout.write('scenario1 seeded')

