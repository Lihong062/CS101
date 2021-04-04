def nameDonor(contributions):
    """
    The parameter contributions is a list of strings, 
    return stringthat is name of most
    generous donor. See description for details.
    """

    donors = {}
    for entry in contributions:
        donor = entry.split(':')[0]
        amount = float(entry.split(':')[1])
        if donor not in donors:
            donors[donor] = amount
        else:
            donors[donor] += amount

    maxdonors = []
    maxdonations = donors[max(donors, key = donors.get)]
    for donor in donors:
        if donors[donor] == maxdonations:
            maxdonors.append(donor)

    return min(maxdonors)


