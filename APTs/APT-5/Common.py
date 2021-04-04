def count(a, b):
    """
    return the integer number of characters in common
    to Strings a and b as described below
    """

    repeated = set(a) & set(b)
    common = 0
    for char in repeated:
        common += min(a.count(char), b.count(char))

    return common