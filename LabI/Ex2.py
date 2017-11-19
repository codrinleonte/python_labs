#Scrieti o functie care calculeaza cate vocale sunt intr-un sir de caractere

def vowelsCounter(word):
    count = 0
    for c in word:
        if c in "aeiouAEIOU":
            count = count + 1
    return count

print (vowelsCounter("taticu"))