def grade(total, availablePoints, cutOff):
    """
    return a student's reading quiz grade as a float percentage based on
    the integer values in total, availablePoints, and cutOff.
    """

    if total >= (0.01*cutOff)*availablePoints:
        # Gives 100% if score is above cutoff
        return(1.00*100)
    else:
        # otherwise give score equal to the percentage over the cutoff
        return((total*100)/(availablePoints*(cutOff*0.01)))
