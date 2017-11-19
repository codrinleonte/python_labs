#Scrieti o functie care converteste un sir de caractere scris UpperCamelCase in lowercase_with_underscores.

def convertString(string):
    result=""
    for c in string:
        if c==c.upper():
            c=c.lower()
            result+="_"
        result+=c

    return result

print(convertString("convertThisFuckingString"))