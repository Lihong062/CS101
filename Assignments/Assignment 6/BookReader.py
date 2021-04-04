'''
@author: Lihong Wang
'''


def getdata():
    '''
    This function reads data from a file and returns the data in the form of a two-tuple.
    The first element of the two-tuple is a list of strings, the second element is a 
    dictionary.
    '''

    f = open('data/books.txt', 'r')
    data = []
    for line in f:
        line = line.split(',')
        entry = []
        for i in range(len(line)):
            if i == 0:
                entry.append(line[i])
            elif i%2 == 1:
                entry.append([line[i], line[i+1]])
        data.append(entry)

    books = []
    for entry in data:
        for rating in entry[1:]:
            if rating[0] not in books:
                books.append(rating[0])

    ratings = {}
    for entry in data:
        person = entry[0]
        if person not in ratings:
            ratings[person] = [0]*len(books)
        for rating in entry[1:]:
            book = rating[0]
            score = rating[1]
            index = books.index(book)
            ratings[person][index] = int(score)

    return(books, ratings)