def order(preferences, size, yarn):
    '''
    preferences (list of strings) - the colors the customer prefers by order
        of preference
    size (int) - the number of balls of yarn needed
    yarn (list of strings) - list of strings of two values where the first is
        the color of yarn and the second is how much yarn is available

    Return a list of strings of two values where the first element is a color
        and the second is how much yarn is needed sorted by the color.
    '''

    reserve = {ball.split()[0]: int(ball.split()[1]) for ball in yarn}
    reserve = [[ball, reserve[ball]] for ball in reserve if ball in preferences]
    reserve = sorted(reserve, key = lambda ball: preferences.index(ball[0]))
    if sum([ball[1] for ball in reserve]) < size:
        return []

    order = {}
    while True:
        for ball in reserve:
            color = ball[0]
            amount = ball[1]
            if color not in order and amount > 0:
                order[color] = 1
                ball[1] += (-1)
                size += (-1)
            elif amount > 0:
                order[color] += 1
                ball [1] += (-1)
                size += (-1)
            if size == 0:
                break
        if size == 0:
            break

    return sorted([' '.join([ball, str(order[ball])]) for ball in order])


