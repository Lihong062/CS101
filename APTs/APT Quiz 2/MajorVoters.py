def compute(info, num):
    '''
    info is a string of names and how many
    times each person has voted,
    num is an integer

    Returns the names in sorted order of people
    who have voted at least num times.
    '''

    info = info.split(':')
    voteBook = {}
    for entry in info:
        name = entry.split()[0]
        vote = int(entry.split()[1])
        voteBook[name] = vote

    ret = []
    for person in voteBook:
        if voteBook[person] >= num:
            ret.append(person)

    ret = sorted(ret)
    return ' '.join(ret)

