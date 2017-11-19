#Sa se scrie o functie care primeste
# ca parametri doua liste a si b si returneaza: (a intersectat cu b, a reunit cu b, a - b, b - a)


def getOperations(a,b):
    a_b_union = list(set([n for n in a + b]))
    a_b_intersection = list(set([n for n in a + b if n in a and n in b]))
    a_b_minus = [n for n in a if n not in b]
    b_a_minus = [n for n in b if n not in a]
    return (a_b_union, a_b_intersection, a_b_minus, b_a_minus)


print(getOperations([1, 2, 3], [3, 4, 5]))