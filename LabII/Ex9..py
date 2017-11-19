# Să se scrie o funție ce va ordona o listă de tuple de string-uri în funcție de al 3-lea caracter
#  al celui de-al 2-lea element din tuplă. Exemplu: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def sortTuples(listOfTuples):
    result = []
    for t in listOfTuples:
        for e in t:
            y = sorted(t, key=lambda e: e[1])
            z = tuple(y)
            if z not in result:
                result.append(z)
    return result


print(sortTuples([('abc', 'bcd'), ('abc', 'zza'), ('abc', 'daa')]))
