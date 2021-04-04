def sort(data):
    """
    return list of strings based on
    the list of strings in parameter data
    """
    data = sorted(data)
    data = sorted(data, key=data.count, reverse=True)

    order = []
    for entry in data:
        if entry not in order:
            order.append(entry)

    return order
