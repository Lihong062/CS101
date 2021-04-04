def maximumFacts(suspects):
    """
    return int based on information in
    parameter results, a list of strings
    """
    intersections = []
    for i in range(len(suspects)):
        for j in range(len(suspects)):
            if i != j:
                intersection = set(suspects[i].split(',')) & set(suspects[j].split(','))
                intersections.append(len(intersection))
    if len(intersections) == 0:
        return 0
    return max(intersections)
