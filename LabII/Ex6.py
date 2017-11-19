# Sa se scrie o functie care primeste ca parametru un numar variabil de liste si un numar intreg x.
#  Sa se returneze o lista care sa contina elementele care apar de exact x ori in listele primite.
# Exemplu: pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2 se va
# returna [1, 2, 3, 4] # 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 se afla
#  in listele 1 si 2, 4 se afla in listele 2 si 3.

def xOccurencesInLists(x, *listOfLists):
    occurences = {}
    for list in listOfLists:
        for e in list:
            occurences.setdefault(e, 0)
    for list in listOfLists:
        for e in list:
            occurences[e] += 1
            occurences.setdefault(e, occurences[e])
    result = []
    for e in occurences:
        if occurences[e] == x:
            result.append(e)
    return result


print(xOccurencesInLists(2, [1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"]))
