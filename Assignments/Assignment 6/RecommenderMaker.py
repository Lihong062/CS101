'''
@author: Lihong Wang
'''

import RecommenderEngine

def makerecs(name, items, ratings, numUsers, top):
    '''
    This function calculates the top recommendations and returns a two-tuple consisting of two lists. 
    The first list is the top items rated by the rater called name (string).
    The second list is the top items not seen/rated by name (string)
    '''

    ranked = [item[0] for item in RecommenderEngine.recommendations(name, items, ratings, numUsers)]
    scores = [item[1] for item in RecommenderEngine.recommendations(name, items, ratings, numUsers)]

    seen = []
    unseen = []
    i, j = 0, 0
    for k in range(len(ranked)):
        index = items.index(ranked[k])
        if ratings[name][index] != 0 and i < top:
            seen.append((ranked[k], float(scores[k])))
            i += 1
        elif ratings[name][index] == 0 and j < top:
            unseen.append((ranked[k], float(scores[k])))
            j += 1
        if i == top and j == top:
            break
    return (seen, unseen)

if __name__ == '__main__':
    name = 'student1367'
    items = ['127 Hours', 'The Godfather', '50 First Dates', 'A Beautiful Mind',
             'A Nightmare on Elm Street', 'Alice in Wonderland',
             'Anchorman: The Legend of Ron Burgundy',
             'Austin Powers in Goldmember', 'Avatar', 'Black Swan']
    ratings = {'student1367': [0, 3, -5, 0, 0, 1, 5, 1, 3, 0],
               'student1046': [0, 0, 0, 3, 0, 0, 0, 0, 3, 5],
               'student1206': [-5, 0, 1, 0, 3, 0, 5, 3, 3, 0],
               'student1103': [-3, 3, -3, 5, 0, 0, 5, 3, 5, 5]}
    numUsers = 2
    top = 3

    print(makerecs(name, items, ratings, numUsers, top)[0])
    print(makerecs(name, items, ratings, numUsers, top)[1])

             



