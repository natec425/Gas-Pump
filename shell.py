GAS_PRICE = 2.00


def main():
    print('Gas costs ${:.2f} per gallon.'.format(GAS_PRICE))
    gallons = float(input('How many gallons of gas would you like to buy: '))
    print('Thank you for your purchase. That will be ${:.2f}.'.format(gallons * GAS_PRICE))


if __name__ == '__main__':
    main()
