# Cel mai mare divizor comun a mai multor numere (definiti o functie cu numar variabil de parametri care sa rezolve acest lucru)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(*args):
    result = args[0]
    for n in args[1:]:
        result=gcd(n,result)
    return result

print (solve(10,25,30))

