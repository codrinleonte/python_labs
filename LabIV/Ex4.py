# 4. Scrieti o functie care primeste ca parametru un path ce reprezinta un
#  director de pe sistem, parcurge recursiv structura de fisiere si directoare pe care acesta
# le contine si afiseaza in consola toate path-urile pe care le-a parcurs. NU aveti voie sa folositi os.walk.

import os


def listFilesAndFoldersRecursevely(path):
    try:
        if os.path.isfile(path):
            print("fisier : " + (os.path.basename(path)))
        if os.path.isdir(path):
            print("Director :" + (os.path.basename(path)))
            entries = os.listdir(path)
            for e in entries:
                listFilesAndFoldersRecursevely(path + "/" + e)
        else:
            return "Path invalid"
    except TypeError as ex:
        print("Argument invalid")


listFilesAndFoldersRecursevely("D:/facultate/anul III/sem I/Inteligenta Artificiala/TemaIII")
