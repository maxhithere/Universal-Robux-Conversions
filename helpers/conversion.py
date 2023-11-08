import json
from helpers import locale as lc

with open('./exchange_rates.json') as file:
    exchange_rates = json.load(file)

def get_exchange_rate(user_locale):
    if user_locale in exchange_rates:
        return exchange_rates.get(user_locale)
    else:
        return 'Unsupported locale'
    

def robux_to_usd(number):
    return round(number * 0.0125, 2)

def usd_to_robux(number):
    return round(number / 0.0125, 2)

def robux_to_usd_devex(number):
    return round(number * 0.0035, 2)

def usd_to_robux_devex(number):
    return round(number / 0.0035, 2)


def convert_to_currency(number, exchange_rate):

    converted = number * exchange_rate
    converted = round(converted, 2)
    formatted_currency = lc.monetary_format(converted)
    
    return formatted_currency

def currency_to_usd(number, exchange_rate):
    return round(number / exchange_rate, 2)
