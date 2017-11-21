#Sa se scrie o functie care primeste ca parametru un sir de caractere text si o lista de expresii
#  si returneaza o lista de siruri de caractere care fac match pe cel putin o expresie regulata data ca parametru.

import re

def isMatching(text,regexList):
    result = []
    for regex in regexList:
        result.append(re.findall(regex,text))

    return [item for sublist in result for item in sublist]


print (isMatching("Foo bar", ["[a-z]+","[A-Za-z]+"]))