## default used for 1st conversion is en_US.UTF-8

import locale

def get_locale():
    return locale.getlocale()[0]

def set_locale(lang_code):
    return locale.setlocale(locale.LC_ALL, lang_code)

def monetary_format(number):
    return locale.currency(number, grouping=True)