def percent(names, number):
    '''
    names is a String of names of people
    in clubs, with each club separated by
    a ":", and number is a decimal number.

    Returns in sorted order, a String
    of the names that are in at least
    number percent of the clubs.
    '''
    # you write code here

    names = names.split(':')

    tracker = {}
    for entry in names:
        entry = entry.split()
        for name in entry:
            if name not in tracker:
                tracker[name] = 1
            else:
                tracker[name] += 1

    ret = []
    for name in tracker:
        if tracker[name]/len(names) >= number:
            ret.append(name)

    return ' '.join(sorted(ret))
