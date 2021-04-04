def modify(name):
    """
    name is a string with zero or more spaces
    with one space between each "word"
    return string "last, first MI. MI. MI. ..."
    where MI is middle initial
    """

    nameList = name.split()
    if len(nameList) == 1:
        return name

    first = nameList[0]
    last = nameList[-1]
    middleList = nameList[1:-1]

    for i in range(len(middleList)):
        if len(middleList[i])>1:
            middleList[i] = middleList[i][0] + '.'

    name = ''
    name += last
    name += ', '
    name += first
    name += ' '
    for middle in middleList:
        name += middle + ' '
    name = name.strip()

    return name
