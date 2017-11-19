# Scrieti o functie care returneaza
# numarul de cuvinte care exista intr-un string. Cuvintele sunt separate de spatii, semne de punctuatie (, ;, ? ! . )
import re
def wordCounter(string):
    x=re.split(r'[ ?.!;]+',string)
    return len(x)

print(wordCounter("mama are mere, si pere"))
