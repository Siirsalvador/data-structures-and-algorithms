def find_grants_cap(grantsArray, newBudget):
    if len(grantsArray) < 1:
        return 0
    grantsArray.sort()
    min_cap = float(newBudget) / float(len(grantsArray))

    for i, x in enumerate(grantsArray):
        if x < min_cap:
            newBudget = float((newBudget - x))
            min_cap = float(newBudget) / float((len(grantsArray) - (i + 1)))

    return min_cap


print(find_grants_cap([2, 45, 100, 120, 1000], 190))
