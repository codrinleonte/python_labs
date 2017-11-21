#2. Scrieti un script care primeste ca parametru de la linia de comanda un path si
# afiseaza primii 4096 bytes daca path-ul duce la un fisier, intrarile din acesta daca
#  path-ul reprezinta un director si un mesaj de eroare daca path-ul nu este unul valid.


import os
import sys
def readPath(path):
    try:
        if os.path.isfile(path):
            file = open(path, 'rb')
            data = file.read(4096)
            return data
        elif os.path.isdir(path):
            entries = os.listdir(path)
            return entries
        else:
            return "Path invalid"
    except TypeError as e:
        print("Argument invalid")

print(readPath("D:/facultate/anul III/sem I/Inteligenta Artificiala/TemaIII"))