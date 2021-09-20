def count(word,phrase):
    word=word.lower()
    phrase=phrase.lower()
    palavras=phrase.split()
    contador=0
    for i in palavras:
        if (i==word):
            contador+=1          
    return(contador)