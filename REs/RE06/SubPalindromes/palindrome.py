def palindrome(astring):
    caracteres = len(astring)
    contador = 0
    substrings = [astring[i:j+1] for i in range(caracteres) for j in range(i,caracteres)]
    num_substrings=len(substrings)
    for k in range(num_substrings):
        cada_substring = substrings[k]
        if (len(cada_substring) != 1):
            reverso = cada_substring[::-1]
            if (reverso == cada_substring):
                contador+=1
    result = "For string '{0}': {1} palindrome substrings"
    return result.format(astring, contador)