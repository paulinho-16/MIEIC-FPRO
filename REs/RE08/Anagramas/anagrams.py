def anagrams(alist):
    def ordenar(x):
        strng = str(x[0]).replace(' ','').lower()
        return strng
    result = []
    anagramas = ()
    for string in alist:
        string_original = string
        anagrama = str(string.lower().replace(' ',''))
        letras = sorted(list(anagrama))
        anagrama = ''
        for letra in letras:
            anagrama += letra
        anagrama_tuplo = (string_original,anagrama)
        anagramas += (anagrama_tuplo,)
    for anagram in anagramas:
        lista_anagramas = []
        lista_anagramas.append(anagram[0])
        for anagram2 in anagramas:
            if anagram2[0] != anagram[0]:
                if anagram2[1] == anagram[1]:
                    lista_anagramas.append(anagram2[0])
        result.append(lista_anagramas)
    result.sort()
    outra_lista = []
    for i in result:
        i = sorted(i)
        if i not in outra_lista:
            outra_lista.append(i)
    outra_lista = sorted(outra_lista,key = lambda x: ordenar(x))
    return outra_lista