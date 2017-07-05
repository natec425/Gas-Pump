REGULAR_PRICE = 2.00
MEDIUM_PRICE = 2.50
PREMIUM_PRICE = 3.00


def main():
    print('Gas costs: Regular (${:.2f}), Medium (${:.2f}), Premium (${:.2f})'.format(
        REGULAR_PRICE, MEDIUM_PRICE, PREMIUM_PRICE))

    gas_type = input('Which type of gas would you like to buy: ')

    if gas_type == 'Regular':
        gas_price = REGULAR_PRICE
    elif gas_type == 'Medium':
        gas_price = MEDIUM_PRICE
    elif gas_type == 'Premium':
        gas_price = PREMIUM_PRICE
    else:
        print('Invalid gas type... Program exitting...')
        exit()

    gallons = float(input('How many gallons of gas would you like to buy: '))

    print('Thank you for your purchase. That will be ${:.2f}.'.format(gallons * gas_price))


if __name__ == '__main__':
    main()
