#Scrieti o functie care#  primeste ca parametru un sir de caractere si returneaza un
# dictionar in care cheile sunt caracterele dn componenta sirului de caractere iar valorile sunt
# reprezentate de numarul de aparitii ale caracterului respectiv in textul dat.
#Exemplu: Pentru sirul "Ana are mere." dat ca parametru functia va returna dictionarul:
# {'A': 1, ' ': 2, 'n': 1, 'a': 2, 'r': 2, 'e': 3, 'm': 1, '.': 1}.


def numberOfApparition(text):
    result = {}
    for c in text:
        result.setdefault(c,0)
    for c in text:
        result[c]+=1
        result.setdefault(c, result[c])
    return result


print(numberOfApparition("Ana are mere."))