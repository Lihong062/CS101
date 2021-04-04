def freqs(data):
    """
    return list of int values corresponding
    to frequencies of strings in data, a list
    of strings
    """
    data = sorted(data)

    counted = []
    order = []
    for entry in data:
        if entry not in counted:
            counted.append(entry)
            order.append(1)
        else:
            order[-1] += 1

    return order
