def repeat(word, number):
    """
    return the word with the first part of it repeated
    if it is a valid part to repeat. The part to be
    repeated must be repeated "number" times.
    If the first letter is not a vowel, and the third
    letter is a vowel, then the part to repeat is the
    first three letters.
    If the first and third letters are not vowels, but
    the second letter is, then the part to repeat is
    the first two letters.
    Otherwise there is nothing to repeat.
    Only the first letter of the returned word may be
    a capital letter, if the original word started with
    a capital letter.
    """

    vowels = 'aeiouAEIOU'
    if word[0] in vowels:
        return word
    elif len(word) > 2 and word[2] in vowels:
        word = word[0:3] + word[0:3].lower()*(number-1) + word[3:]
        return word
    elif len(word) > 1 and word[1] in vowels:
        word = word[0:2] + word[0:2].lower()*(number-1) + word[2:]
        return word
    else:
        return word
    