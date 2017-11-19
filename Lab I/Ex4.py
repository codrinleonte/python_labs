#Scrieti o functie care primeste
# ca parametri doua siruri de caractere si care returneaza numarul de aparitii ale primului sir de caractere in al doilea.

def numberOfOccurences(string,substring):
    count = 0
    while 1:
        idx = string.find(substring)
        if idx == -1:
            break
        count += 1

        string = string[idx + 1:]
    return count
print (numberOfOccurences("mamaaremeremamama","mama"))