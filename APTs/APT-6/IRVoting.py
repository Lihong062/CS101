def winner3(data):
    '''
    data (list of strs): A list of strings, each string represents a voter's
        ranked preference for the three candidates. Each candidate is separated
        by a semicolon ";"

    Implement instant runoff voting when there are only three candidates to
    choose from. Return the candidate that wins or 'Tie' if there is a tie.
    '''

    candidateA = data[0].split(';')[0]
    candidateB = data[0].split(';')[1]
    candidateC = data[0].split(';')[2]
    voteA = 0
    voteB = 0
    voteC = 0

    for ballot in data:
        if ballot.split(';')[0] == candidateA:
            voteA += 1
        elif ballot.split(';') [0] == candidateB:
            voteB += 1
        elif ballot.split(';')[0] == candidateC:
            voteC += 1

    if voteA > 0.5*len(data):
        return candidateA
    elif voteB > 0.5*len(data):
        return candidateB
    elif voteC > 0.5*len(data):
        return candidateC

    low = min(voteA, voteB, voteC)
    if voteA == low:
        for ballot in data:
            if ballot.split(';')[0] == candidateA:
                if ballot.split(';')[1] == candidateB:
                    voteB += 1
                elif ballot.split(';')[1] == candidateC:
                    voteC += 1
    if voteB == low:
        for ballot in data:
            if ballot.split(';')[0] == candidateB:
                if ballot.split(';')[1] == candidateA:
                    voteA += 1
                elif ballot.split(';')[1] == candidateC:
                    voteC += 1
    if voteC == low:
        for ballot in data:
            if ballot.split(';')[0] == candidateC:
                if ballot.split(';')[1] == candidateB:
                    voteB += 1
                elif ballot.split(';')[1] == candidateA:
                    voteA += 1

    if voteA > 0.5*len(data):
        return candidateA
    elif voteB > 0.5*len(data):
        return candidateB
    elif voteC > 0.5*len(data):
        return candidateC

    print(candidateA, voteA, candidateB, voteB, candidateC, voteC)
    return 'Tie'

