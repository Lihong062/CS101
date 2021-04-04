def maxPoints(toss):
    """
    return int representing the maximal Yahtzee
    score based on rolls in integer list toss
    """

    score = 0
    for num in range(7):
        if num*toss.count(num) > score:
            score = num*toss.count(num)
    return score
