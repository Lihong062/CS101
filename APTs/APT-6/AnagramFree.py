def getMaximumSubset(words):
    """
    return int value that represents
    size of largest anagram-free subset
    of values in words, a list of strings
    """

    def transform(word):
        return ''.join(sorted(word))

    transformed = [transform(word) for word in words]

    def clean(transformed):
        for word1 in transformed:
            for word2 in transformed:
                if word1 is not word2 and word1 == word2:
                    transformed.remove(word2)

    for i in range(int(50**(1/2))):
        clean(transformed)

    return len(transformed)
