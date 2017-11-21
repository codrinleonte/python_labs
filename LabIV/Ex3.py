#3. Scrieti o functie care primeste ca parametru un nume de fisier. Aceasta va scrie in
#  fisier datele din os.environ, fiecare linie continand cate o intrare din acest dictionar,
#  sub forma cheie [tab] valoare.

import os
def writeInFileData(file):
    try:
        file = open(file, 'w')
        for key,value in  os.environ.items():
            line = "[" + key + "]" + "=>" + os.environ[key] + "\n"
            file.write(line)
    except Exception as e:
        print(e)

writeInFileData("fisier.txt")
