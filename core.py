REGULAR_PRICE = 2.00
MEDIUM_PRICE = 2.50
PREMIUM_PRICE = 3.00


def gas_price(gas_type):
    '''String -> Float

    Returns the price per gallon of the provided gas type.
    If an invalid gas type is provided, None is returned.

    >>> gas_price('Regular')
    2.0
    >>> gas_price('Medium')
    2.5
    >>> gas_price('Premium')
    3.0
    >>> gas_price('something else') is None
    True
    '''
    if gas_type == 'Regular':
        return REGULAR_PRICE
    elif gas_type == 'Medium':
        return MEDIUM_PRICE
    elif gas_type == 'Premium':
        return PREMIUM_PRICE
