def winners(data):
    """
    return String list based on String list data
    """
    tracker = {}
    for entry in data:
        person = entry.split()[0]
        time = float(entry.split()[1].split(':')[0]) + float(entry.split()[1].split(':')[1])/60
        if person not in tracker:
            tracker[person] = [0,0]
        tracker[person][0] += 1
        tracker[person][1] += time
    return sorted(tracker, key = lambda x: (-tracker[x][0], tracker[x][1]))

