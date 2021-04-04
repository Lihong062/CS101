def minimumVotes(votes):
    """
    returns minimum number of votes(int) to change
    using values in votes (integer list)
    """

    if len(votes) == 1:
        return 0

    buy = 0
    while max(votes) != votes[0]:
        votes[votes.index(max(votes))] += (-1)
        votes[0] += 1
        buy += 1

    if sorted(votes)[-1] == sorted(votes)[-2]:
        return buy+1
    return buy
