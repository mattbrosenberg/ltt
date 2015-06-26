from .forms import LiborForm
from .quandl import Quandl
from .models import Libor

def seed_libor_database():
    libor_list = Quandl().get_all_libor_rates_and_dates()
    for libor_dict in libor_list:
        form = LiborForm(libor_dict)
        if form.is_valid():
            libor = Libor(
                date=form.cleaned_data['date'],
                rate=form.cleaned_data['rate']
            )
            libor.save()