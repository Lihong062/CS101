def howMany(meals, restaurant):
    """
    Parameter meals a list of strings with each in the format
    "name:place-ate". Parameter restaurant is a string
    return # unique name values where place-ate == restaurant
    """

    customers = set()
    for meal in meals:
        meal = meal.split(':')
        if meal[1] == restaurant:
            customers |= set([meal[0]])
            # print (customers)
    return len(customers)
