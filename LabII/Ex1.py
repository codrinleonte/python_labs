# Sa se scrie o functie care sa returneze o lista cu primele n numere din sirul lui Fibonacci.

def fibonacci(n):
    a = list()
    if n < 0:
        return "Bad Agument"
    if n == 0:
        a.insert(0,0)
        return a
    a.insert(0,0)
    a.insert(1,1)
    if n == 1:
        return a
    for i in range(2, n):
        a.insert(i, a[i - 1] + a[i - 2])
    return a

print(fibonacci(-1))
