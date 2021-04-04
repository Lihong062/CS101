def bagelCount(orders):
    """
    return number of bagels needed to fulfill
    the orders in integer list parameter orders
    """

    total = 0
    for order in orders:
        total += order + order//12
    return total
