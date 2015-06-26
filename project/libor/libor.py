from .seed import seed_libor_database
from .models import Libor
import datetime

def get_most_recent_libor_object():
    day = 0
    while day < 5:
        date = datetime.date.today() - datetime.timedelta(day)
        try:
            return Libor.objects.get(date=date)
        except:
            day += 1
    seed_libor_database()
    return Libor.objects.latest('date')

def most_recent_libor_rate():
    libor = get_most_recent_libor_object()
    return float(libor.rate)

def most_recent_libor_date():
    libor = get_most_recent_libor_object()
    return libor.date

def most_recent_libor_as_dict():
    libor = get_most_recent_libor_object()
    return {'date':libor.date, 'rate':float(libor.rate)}

def get_rate_by_date(date_object):
    """
    Takes a datetime.date object,
    returns the corresponding libor rate as a float.
    If does not exist, returns None.
    """
    try:
        libor = Libor.objects.get(date=date_object)
        return float(libor.rate)
    except:
        try:
            seed_libor_database()
            libor = Libor.objects.get(date=date_object)
            return float(libor.rate)
        except:
            return None