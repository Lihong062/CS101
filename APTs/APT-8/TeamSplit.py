def difference(strengths):
    """
    return int based on int list parameter strengths
    """

    team1 = []
    team2 = []
    for i in range(int(len(strengths)/2)+1):
        if strengths != []:
            team1.append(max(strengths))
            strengths.remove(max(strengths))
        if strengths != []:
            team2.append(max(strengths))
            strengths.remove(max(strengths))
    return(sum(team1)-sum(team2))
