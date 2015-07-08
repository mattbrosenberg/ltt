from django.core.management.base import BaseCommand, CommandError
from trancheur.seed import Seed

class Command(BaseCommand):
    help = "seeds the database with bonds, contracts and users"

    def handle(self, *args, **options):
        scenario = {
            'scenario1': Seed.scenario1,
            'scenario2': Seed.scenario2,
            'create_flex_user': Seed.flex_investor_user,
        }

        for arg in args:
            scenario[arg]()
            self.stdout.write('{} seeded'.format(scenario[arg]))

