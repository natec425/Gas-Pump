INVENTORY = [
    ['Regular', 2.0],
    ['Medium', 2.5],
    ['Premium', 3.0]
]

def gas_price(inventory, gas_type):
    '''String -> Float

    Returns the price per gallon of the provided gas type.
    If an invalid gas type is provided, None is returned.

    >>> gas_price(['Regular', 2.0],
    ... ['Medium', 2.5],
    ... ['Premium', 3.0], 'Regular')
    2.0
    >>> gas_price('Medium')
    2.5
    >>> gas_price('Premium')
    3.0
    >>> gas_price('something else') is None
    True
    '''
    if gas_type == 'Regular':
        return inventory[0][1]
    elif gas_type == 'Medium':
        return inventory[1][1]
    elif gas_type == 'Premium':
        return inventory[2][1]
