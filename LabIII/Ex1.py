# 1. Sa se scrie o functie care
#  primeste ca parametri doua liste a si b si returneaza
#  un tuplu de seturi care sa contina: (a intersectat cu b, a reunit cu b, a - b, b - a)

def listOperations(a, b):
    operation = {}
    result = []
    operation = set([n for n in a + b])
    result.append(operation)
    operation = set([n for n in a + b if n in a and n in b])
    result.append(operation)
    operation = set([n for n in a if n not in b])
    result.append(operation)
    operation = [n for n in b if n not in a]
    result.append(operation)
    resultAsTuple = tuple(result)
    return resultAsTuple


print(listOperations([1, 2, 3], [3, 4, 5]))
