def average(sentenceList):
    """
    returns the average sentence length
    of all the sentences in sentenceList, a
    list of white-space delimited strings.
    """
    totalLength = 0 # Start the counter
    for sentence in sentenceList:
        sentenceSplit = sentence.split()
        totalLength = totalLength + int(len(sentenceSplit))
    return (totalLength/len(sentenceList))

