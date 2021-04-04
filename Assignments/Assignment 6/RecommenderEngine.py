'''
@author: Lihong Wang
'''

def averages(items, ratings):
    '''
    This function calculates the average ratings for items. 
    A two-tuple is returned, where the first element is a string and the second element is a float.
    '''

    ret = []
    for i in range(len(items)):
        numerator = 0
        denominator = 0
        for person in ratings:
            if ratings[person][i] != 0:
                numerator += ratings[person][i]
                denominator += 1
        if denominator == 0:
            ret.append((items[i], float(0)))
        else:
            ret.append((items[i], float(numerator/denominator)))
    ret = sorted(ret)
    ret = sorted(ret, key = lambda x: x[1], reverse=True)
    return ret

def similarities(name, ratings):
    '''
    This function calculates how similar the rater called name is to all other raters.
    A two-tuple is returned, where the first element is a string and the second element is an integer.
    '''

    ret = []
    for person in ratings:
        if person != name:
            ret.append((person, sum([i*j for (i,j) in zip(ratings[person], ratings[name])])))
    ret = sorted(ret)
    ret = sorted(ret, key = lambda x: x[1], reverse=True)
    return ret
 
def recommendations(name, items, ratings, numUsers):
    '''
    This function calculates the weighted average ratings and makes recommendations 
    based on the parameters and weighted average. A two-tuple is returned, where 
    the first element is a string and the second element is a float.
    '''

    newRatings = {}
    for entry in similarities(name, ratings)[0:numUsers]:
        person, weight = entry[0], entry[1]
        newRatings[person] = [float(weight*rating) for rating in ratings[person]]
    return averages(items, newRatings)
        

if __name__ == '__main__':
    pass