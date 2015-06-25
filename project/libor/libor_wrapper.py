import requests
import json
import pprint
from pprint import PrettyPrinter
from getenv import env

class Quandl:
    def __init__(self):
        self.libor_url = 'https://www.quandl.com/api/v1/datasets/FED/RILSPDEPM01_N_B.json?auth_token='
        self.api_key = env('API_KEY')

    def get_libor_rates(self):
        results_array = []
        search_result = requests.get(self.libor_url + self.api_key)
        printer = PrettyPrinter()
        if search_result.json() != []:
            libor_rates_dict = search_result.json()
            # parsed = json.loads(libor_rates_dict)
            pp = pprint.PrettyPrinter(indent=4)
            for libor_rate in range(0, len(libor_rates_dict['data'])):
                # print(libor_rates_dict['data'][libor_rate])
                results_array.append(libor_rates_dict['data'][libor_rate])
            pp.pprint(results_array)
            return results_array
        else:
            print("No libor rates found.")


if __name__ == '__main__':
    pass

q = Quandl()
q.get_libor_rates()
