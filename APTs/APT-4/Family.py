def grandchildren(parents, children, person):
    '''
    parents (list of strings) - list of parent names corresponding to the
        children list
    children (list of strings) - list of child names corresponding to the
        parents list
    person (string) - a person listed in parents

    Return the number of grandchildren for the person in the person variable
    '''

    grandchildren = set()
    for i in range(len(parents)):
        if parents[i] == person: # if p is c's parent
            for j in range(len(parents)):
                if parents[j] == children[i]: # if c is g's parent
                    grandchildren.add(children[j])
    return len(grandchildren)
