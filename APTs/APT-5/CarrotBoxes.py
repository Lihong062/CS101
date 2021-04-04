def theIndex(carrots, amount):
    """
    carrots is list of integers representing
    boxes of carrots, amount is int value.
    return int that is the index/box number
    of the box from which the last of
    amount carrots are eaten
    """
    while amount > 0:
        index = carrots.index(max(carrots))
        carrots[index] += -1
        amount += -1
        if amount == 0:
            return index
