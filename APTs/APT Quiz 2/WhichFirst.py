def popular(names):
    '''
    Given the String parameter names
    which contains first and last names
    for one or more people, return the
    string of sorted first names that
    are more popular as a first name
    then as a last name.
    '''

    names = names.split(',')
    firstNames = [name.split()[0] for name in names]
    lastNames = [name.split()[1] for name in names]

    ret = [name for name in firstNames if firstNames.count(name) > lastNames.count(name)]
    ret = sorted(set(ret))

    return ' '.join(ret)

