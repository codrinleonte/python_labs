# 5. Scrieti un script care primeste 2 parametri de la consola reprezentand un path
# catre un director de pe sistem si un nume de fisier. Scriptul va parcurge recursiv structura
# de fisiere si directoare din directorul dat ca parametru, utilizand os.walk si va scrie in fisierul
#  dat ca parametru toate path-urile pe care le-a parcurs si tipul acestuia (FILE, DIRECTORY, UNKNOWN),
# separate de |. Fiecare path va fi scris pe cate o linie.

import os


def writeFilesType(path, file):
    try:
        fisier = open(file, 'w')
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files + dirs:
                line = os.path.join(root, name)
                line.replace('\\', '/')
                if os.path.isfile(line):
                    line += " | " + "FILE \n"
                elif os.path.isdir(line):
                    line += " | " + "DIRECTORY \n"
                else:
                    line += " | " + "UNKNOWN \n"

                fisier.write(line)
    except Exception as e:
        print(e)


writeFilesType("D:/facultate/anul III/sem I/Inteligenta Artificiala/TemaIII", "fis.txt")
