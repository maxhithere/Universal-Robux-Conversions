
from helpers import conversion, locale as lc

get_locale = lc.get_locale()
set_locale = lc.set_locale(get_locale)

get_exchange_rate = conversion.get_exchange_rate(get_locale)

def main():
    print('Robux to Currency Converter (universal)\nCreated by @maxhithere\n\n\n1) Robux to Currency\n2) Currency to Robux\n3) Robux to Currency (DevEx)\n4) Currency to Robux (DevEx)\n\n\nEnter your choice: ')
    choice = int(input(">> "))

    if choice == 1:
        print('Enter the amount of Robux you want to convert to currency: ')
        robux = int(input(">> "))
        conver = conversion.robux_to_usd(robux)
        conver = conversion.convert_to_currency(conver, get_exchange_rate)
        print('Converted to currency: ' + str(conver))

    elif choice == 2:
        print('Enter the amount of currency you want to convert to Robux: ')
        currency = int(input(">> "))
        conver = conversion.currency_to_usd(currency, get_exchange_rate)
        conver = conversion.usd_to_robux(currency)
        print('Converted to Robux: ' + str(conver))

    elif choice == 3:
        print('Enter the amount of Robux you want to convert to currency: ')
        robux = int(input(">> "))
        conver = conversion.robux_to_usd_devex(robux)
        conver = conversion.convert_to_currency(conver, get_exchange_rate)
        print('Converted to currency: ' + str(conver))

    elif choice == 4:
        print('Enter the amount of currency you want to convert to Robux: ')
        currency = int(input(">> "))
        conver = conversion.currency_to_usd(currency, get_exchange_rate)
        conver = conversion.usd_to_robux_devex(currency)
        print('Converted to Robux: ' + str(conver))
        
    else:
        print('Invalid choice. Please try again.')
        main()

if __name__ == '__main__':
    main()
