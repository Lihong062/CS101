def winners(ballot):
    """
    return list of winners based on votes
    in list ballot
    """

    candidates ={person:0 for i in range(len(ballot)) for person in ballot[i].split()}
    for entry in ballot:
        persons = entry.split()
        for i in range(len(persons)):
            candidates[persons[i]] += len(persons) - i

    topVotes = candidates[max(candidates, key=candidates.get)]
    winners = []
    for person in candidates:
        if candidates[person] == topVotes:
            winners.append(person)

    return sorted(winners)

