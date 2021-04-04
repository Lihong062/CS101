def whichOrder(available, orders):
    """
    return zero-based index of first
    sandwich in orders, list of strings
    that can be made from ingredients
    in available, list of strings
    """

    for i in range(len(orders)):
        order = orders[i].split()
        if set(available) & set(order) == set(order):
            return i
    return -1
