def generate(results):

    countries = list(set(x for field in results for x in field.split()))

    for i in range(len(countries)):
        countries[i] = [countries[i]]
        countries[i].append(0)
        countries[i].append(0)
        countries[i].append(0)
        for field in results:
            for j in range(3):
                if field.split()[j] == countries[i][0]:
                    countries[i][j+1] += 1

    countries = sorted(countries)
    countries = sorted(countries, key = lambda x: x[3], reverse=True)
    countries = sorted(countries, key=lambda x: x[2], reverse=True)
    countries = sorted(countries, key=lambda x: x[1], reverse=True)

    results = []
    for country in countries:
        for i in range(3):
            country[i+1] = str(country[i+1])
        results.append(' '.join(country))

    return results

