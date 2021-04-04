def bestInvitation(first, second):
    """
    return int based on string list
    parameters first and second
    """

    first.extend(second)
    return first.count(max(first, key = lambda x: first.count(x)))
