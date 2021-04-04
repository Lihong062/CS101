def calculate(readpages, totalpages, numdays, amazon):
    """
    readpages - number of pages read
    totalpages - number of pages in the book
    numdays - number of days read book
    amazon - book rating on amazon
    
    Return the result of the formula shown.
    Calculate the answer as a float, then 
    return it as a truncated int
     """


    temp = (readpages / totalpages) * 1000
    temp = (temp / numdays)

    return int((temp ** 2 + amazon ** 2) ** (1 / 2))

print (calculate(356, 356, 10, 4.12))