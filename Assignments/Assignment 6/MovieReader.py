'''
@author: Lihong Wang
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''

    f = open('data/movies.txt', 'r')
    data = []
    movies = []
    for line in f:
        data.append(line.split(','))
        movies.append(line.split(',')[1])
    movies = sorted(set(movies))

    ratings = {}
    for i in range(len(data)):
        person = data[i][0]
        movie = data[i][1]
        rating = float(data[i][2])
        if person not in ratings:
            ratings[person] = [0]*len(movies)
        index = movies.index(movie)
        ratings[person][index] = rating

    return(movies, ratings)




