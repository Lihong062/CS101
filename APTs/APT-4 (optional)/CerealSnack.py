import math

def computeCups(calplan, eaten, calperserv, servsize):
    '''
    Here are the parameters for the function computeCups.
    calplan is an integer representing the number of
       calories you want to eat each day.
    eaten is an integer representing the number of
       calories you have eaten so far for a day
    calperserv is an integer representing the number of
       calories per serving for the cereal you would like
       to eat at the end of the day
    servsize is a float and represents the serving size
       in cups for this cereal
    Given these four parameters, return the number of full cups
       of cereal you could eat for a snack so that you won't go over
       the number of calories you want to eat each day.
    '''

    calleft = calplan - eaten
    if calleft < 0:
        return 0
    servleft = calleft/calperserv
    cupsleft = servleft*servsize
    fullcupsleft = int(cupsleft)

    return  fullcupsleft
