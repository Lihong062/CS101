def edit(entry):
    """
    Return list of String values based on
    entry (list of Strings) as
    described below
    """

    entry = [set(phrase.split()) for phrase in entry]

    for k in range(len(entry)):
        for i in range(len(entry)):
                for j in range(len(entry)):
                    if i < len(entry) and j < len(entry) and i != j:
                        if len(entry[i] & entry[j]) > 1:
                            entry[i] |= entry[j]
                            entry.remove(entry[j])

    return sorted([' '.join(sorted(phrase)) for phrase in entry])

