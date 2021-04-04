def shorten(name):
    """
    return the name with the middle name(s) removed.
    name has at least one word.
    """
    nameSplit = name.split()
    if len(nameSplit)<=2:
        # Returns name if it's only two words or less
        return name

    # Else returns first and last entry of split
    return(nameSplit[0]+' '+nameSplit[-1])
