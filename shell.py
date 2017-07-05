import core


def print_menu(inventory):
    '''Inventory -> None

    Prints a menu for the given inventory.

    >>> print_menu([['Regular', 2.0], ['Premium', 3.0]])
    Gas Costs:
    Regular - $2.00
    Premium - $3.00
    '''
    print('Gas Costs:')
    for name, cost in inventory:
        print('{} - ${:.2f}'.format(name, cost))


def get_gas_price(gas_type):
    price = core.gas_price(gas_type)
    if price is None:
        print('Invalid gas type... Program exiting...')
        exit()
    return price


def log_transaction(gas_type, gas_price, gallons):
    with open('log.txt', 'a') as logfile:
        logfile.write('{}, {}, {}\n'.format(gas_type, gas_price, gallons))


def pay_after(gas_type, gas_price):
    gallons = float(input('How many gallons of gas would you like to buy: '))
    print('Thank you for your purchase. That will be ${:.2f}.'.format(gallons * gas_price))
    log_transaction(gas_type, gas_price, gallons)


def prepay(gas_type, gas_price):
    total_cost = float(input('How much gas would you like to buy: $'))
    gallons = total_cost / gas_price
    print('Thank you for your purchase. That will be {:.2f} gallons.'.format(gallons))
    log_transaction(gas_type, gas_price, gallons)


def main():
    print_menu(core.INVENTORY)
    gas_type = input('Which type of gas would you like to buy: ')
    gas_price = get_gas_price(gas_type)
    prepaying = input('Will you be prepaying (y/n): ')
    if prepaying == 'n':
        pay_after(gas_type, gas_price)
    else:
        prepay(gas_type, gas_price)


if __name__ == '__main__':
    main()
