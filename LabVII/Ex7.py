# Sa se simuleze extragerea 6/49.

import random


def loteryExtraction():
    result = []
    currentExtraction = 0
    for i in range(0, 6):
        while currentExtraction in result or currentExtraction == 0:
            currentExtraction = random.randint(1, 49)
        result.append(currentExtraction)
    return result


def lottoResult(ticket):
    # if sorted(ticket) == random.sample(range(1, 50), 6):
    count = 0;
    extraction = loteryExtraction()
    print("Extragerea : " + str(extraction))
    if len(ticket) != 6:
        return "Introduceti 6 numere pe bilet!"
    for number in ticket:
        if int(number) < 1 or int(number) > 49:
            return "numerele trebuie sa fie cuprinse intre 1 si 49!"
        if int(number) in extraction:
            count += 1
    print("Felicitari, ati nimerit " + str(count) + " numere !")
    if sorted(ticket) == sorted(extraction):
        print("Winner")
    print("Loser")
    return count


# print(loteryExtraction())
res = []
for i in range(0, 100 ):
    c = lottoResult([27, 21, 29, 23, 38, 17])
    if c > 3:
        res.append(c)
print(res)
