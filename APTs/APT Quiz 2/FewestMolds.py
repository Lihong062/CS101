def smallest(current, future):
    '''
    Both current and future are Strings of phrases
    representing signs.
    For each letter in a phrase in current, a mold was made to
    create the letter for the sign,
    and molds can be reused.
    Return the phrase in future that needs the fewest
    new molds created to turn
    that phrase into a sign.
    Note that a letter mold can be used over again.
    '''

    def moldsNeeded(molds, phrase):
        newMolds = set()
        for char in phrase:
            if char != ' ' and char not in molds:
                newMolds |= set(char)
        return newMolds

    current = current.split('=')
    molds = set([char for phrase in current for char in phrase if char != ' '])

    future = future.split('+')
    tracker = []
    for phrase in future:
        tracker.append(len(moldsNeeded(molds, phrase)))

    for i in reversed(range(len(future))):
        if tracker[i] == min(tracker):
            return future[i]