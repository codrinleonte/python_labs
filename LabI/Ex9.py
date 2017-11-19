# Scrieti o functie care sa returneze cel mai mare numar
# prim dintr-un sir de caractere dat ca parametru sau -1 daca sirul de caractere
#  nu contine nici un numar prim. Ex: input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda'; output: 271

import re


def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def getBiggestPrime(expr):
    max = 0
    numbers = [int(n) for n in re.findall("\d+", expr)]
    if len(numbers) == 0:
        return -1
    for n in numbers:
        if isPrime(n) and n > max:
            max = n
    if max == 0:
        return -1
    return max


print(getBiggestPrime("ahsfaisd35biaishai23isisvdsh67cbsi271cidsbfsd97sidsda"))
