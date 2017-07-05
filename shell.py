import core


def print_menu():
    print('Gas costs: Regular (${:.2f}), Medium (${:.2f}), Premium (${:.2f})'.format(
        core.REGULAR_PRICE, core.MEDIUM_PRICE, core.PREMIUM_PRICE))


def main():
    print_menu()

    gas_type = input('Which type of gas would you like to buy: ')

    gas_price = core.gas_price(gas_type)
    if gas_price is None:
        print('Invalid gas type... Program exiting...')
        exit()

    gallons = float(input('How many gallons of gas would you like to buy: '))

    print('Thank you for your purchase. That will be ${:.2f}.'.format(gallons * gas_price))

    with open('log.txt', 'a') as logfile:
        logfile.write('{}, {}, {}\n'.format(gas_type, gas_price, gallons))


if __name__ == '__main__':
    main()
