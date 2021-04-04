def networth(transactions):
    """
    return list of strings based on transactions,
    which is also a list of strings
    """

    names = set()
    for entry in transactions:
        entry = entry.split(':')
        for i in range(2):
            names |= set([entry[i]])
    # print (names)

    netCashFlow = []
    for name in names:
        net = 0
        for entry in transactions:
            entry = entry.split(':')
            if name == entry[0]:
                net += -float(entry[2])
            elif name == entry[1]:
                net += float(entry[2])
        netCashFlow.append(name+':'+str(round(net,2)))
    return sorted(netCashFlow)
