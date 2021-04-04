def ratio(dna):
    """
    return float that's the cg ratio of the
    nucleotides in the string parameter dna
    """

    cytosine = 0
    guanine = 0

    for char in dna:
        if char == 'c':
            cytosine += 1
        elif char == 'g':
            guanine += 1
    return ((cytosine+guanine)/len(dna))
