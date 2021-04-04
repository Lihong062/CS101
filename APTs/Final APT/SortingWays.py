def calculate(phrase):
    '''
    phrase is a string of words with
    each word in a special format that has
    four parts.

    Returns the words in a String in sorted order:
    sorting the first part of the word in alphabetical order,
    breaking ties with the second part of the word in reverse
    numeric order, breaking those ties with the third
    part of the word in reverse alphabetical order, and
    breaking those ties with the fourth part of the word
    sorted in numeric order.
    '''

    phrase = phrase.split()
    formatted = []
    for word in phrase:
        part1, part2, part3, part4 = '', '', '', ''
        for char in word.split('-')[0]:
            if char.isalpha():
                part1 += char
            else:
                part2 += char
        for char in word.split('-')[1]:
            if char.isalpha():
                part3 += char
            else:
                part4 += char
        formatted.append([word, part1, part2, part3, part4])

    formatted = sorted(formatted, key = lambda x: int(x[4]))
    formatted = sorted(formatted, key=lambda x: x[3], reverse=True)
    formatted = sorted(formatted, key=lambda x: int(x[2]), reverse=True)
    formatted = sorted(formatted, key=lambda x: x[1])

    ret = [word[0] for word in formatted]
    return ' '.join(ret)
