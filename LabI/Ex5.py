# Scrieti o functie care verifica daca un sir de caractere contine caractere speciale (\r, \t, \n, \a, \b, \f, \v)

def hasSpacialChars(string):
    for c in string:
        if c in "\r\t\n\a\b\f\v":
            return True

    return False

print(hasSpacialChars("asdasda"))