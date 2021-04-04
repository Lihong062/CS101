def minutesNeeded(numCakes, capacity):
    """
    return integer representing time to cook pancakes
    based on integer parameters as described below
    """

    sides = numCakes * 2
    if sides%capacity == 0: 
    	return(int(5 * sides/capacity))
    else: 
    	return(int(5 * (sides//capacity) + 5))
