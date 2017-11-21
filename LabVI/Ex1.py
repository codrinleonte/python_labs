#Sa se scrie o functie care
#  extrage cuvintele dintr-un text dat ca parametru.
#  Un cuvant este definit ca o secventa de caractere alfa-numerice.

import re
def extractAllWords(text):
  print(re.findall("[a-z0-9A-Z]+", text))

extractAllWords("Let us compile and run the above program, this will scan all the directories and subdirectories bottom-to-up")