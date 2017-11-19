# Scrieti o functie care primeste un integer char_len si un numar variabil de parametri
# (siruri de caractere) si verifica daca fiecare doua string-uri vecine respecta urmatoarea regula:
# al doilea string incepe cu ultimile char_len caractere a primului string (ca la fazan).

def fazanGame(char_len, *list):
    piece = list[0][-char_len:]
    for string in list[1:]:
        if piece != string[0:char_len]:
            return False
        piece = string[-char_len:]
    return True

print(fazanGame(2,'rata','tara','ratoi'))