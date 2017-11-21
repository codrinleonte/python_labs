#Sa se scrie o functie care primeste ca parametru un sir de caractere regex, un sir de caractere
# text si un numar intreg x si returneaza acele substring-uri de lungime maxim x care fac match pe expresia regulata data.

import re
def getMatches(regexExpr,text,x):
    return [y for y in re.findall(regexExpr, text) if len(y) <= x]


print(getMatches("[a-z0-9A-Z]+","Foo Bar",3))