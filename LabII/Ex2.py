#Sa se scrie o functie care primeste o lista de numere si returneaza o lista cu numerele prime care se gasesc in ea.

import sys
from LabI.Ex9 import isPrime


def getPrimesList(x):
    result = list()
    for n in x:
        if(isPrime(n)):
            result.append(n)
    return result


print(getPrimesList([123,12,1231,41,51,21]))

