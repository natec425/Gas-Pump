import core

REGULAR_PRICE = 2.00
MEDIUM_PRICE = 2.50
PREMIUM_PRICE = 3.00


def main():
    print('Gas costs: Regular (${:.2f}), Medium (${:.2f}), Premium (${:.2f})'.format(
        REGULAR_PRICE, MEDIUM_PRICE, PREMIUM_PRICE))

    gas_type = input('Which type of gas would you like to buy: ')

    gas_price = core.gas_price(gas_type)
    if gas_price is None:
        print('Invalid gas type... Program exitting...')
        exit()

    gallons = float(input('How many gallons of gas would you like to buy: '))

    print('Thank you for your purchase. That will be ${:.2f}.'.format(gallons * gas_price))


if __name__ == '__main__':
    main()
