# Sa se compare doua dictionare fara a folosi operatorul "==" si sa se returneze un tuplu de
# liste de diferente astfel: (cheile_comune_dar_cu_valori_diferite, cheile_care_se_gasesc_doar_
# in_primul_dict, cheile_care_se_gasesc_doar_in_al_doilea_dict). (Atentie, dictionarele trebuiesc
# parcurse recursiv deoarece la randul lor pot contine alte containere, cum ar fi dictionare, liste, set-uri, etc)

def valuesComparator(a, b):
    types = [dict, set, list, tuple]
    indici = [list, tuple]
    if type(a) == type(b):
        if type(a) not in types:
            return a == b
        if len(a) != len(b):
            return False
        if type(a) in indici:
            for i in range(0, len(a)):
                if valuesComparator(a[i], b[i]) == False:
                    return False
            return True
        else:
            a, b, c = dictionarComarator(a, b)
            if len(a) + len(b) + len(c) == 0:
                return True
            return False
    else:
        return False


def dictionarComarator(d1, d2):
    commonKeysWithDifferentValues = []
    keysFoundJustInFirstDictionary = []
    keysFoundJustInSecondDictionary = []

    for e1 in d1:
        if e1 not in d2:
            keysFoundJustInFirstDictionary.append(e1)
    for e2 in d2:
        if e2 not in d1:
            keysFoundJustInSecondDictionary.append(e2)
    for e1 in d1:
        if e1 in d2:
            if valuesComparator(d1[e1],d2[e1]) == False :
                commonKeysWithDifferentValues.append(e1)
    return (commonKeysWithDifferentValues,keysFoundJustInFirstDictionary,keysFoundJustInSecondDictionary)


print (dictionarComarator({'a': 1, 'b': 1}, {'a': 1, 'b': [1, 2], 'c': 3}))
