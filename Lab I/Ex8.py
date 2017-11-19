#Se da un sir de caractere care reprezinta un polinom
# (Ex: "3x^3 + 5x^2 - 2x - 5") si un numar (intreg sau float). Sa se evalueze polinomul respectiv pentru valoarea data.

import re


def solve_polynomial(p, x):
    compound_terms = re.findall("[+-]?[0-9]+x[\^]?[0-9]*", p)
    terms = re.findall("[ ]*[+-]?[ ]x", p)

    compound_terms = "".join(compound_terms)
    compound_terms = compound_terms.replace('x', '*' + str(x))
    compound_terms = compound_terms.replace('^', '**')

    terms = "".join(terms)
    terms = terms.replace('x', str(x))

    numbers = "".join(p.rsplit(compound_terms + terms))
    numbers = numbers if numbers != p else ""

    print
    numbers

    return eval(compound_terms + terms + numbers)


print(solve_polynomial("2x^2 + x", 2))