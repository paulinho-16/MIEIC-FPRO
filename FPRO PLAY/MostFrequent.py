def most_frequent(alist):
    dicionario = {}
    for numero in alist:
        if numero not in dicionario:
            dicionario[numero] = 1
        else:
            dicionario[numero] += 1
    filtro = list(filter(lambda x: x[1] == max(dicionario.values()),dicionario.items()))
    if len(filtro) == 1:
        return filtro[0][0]
    else:
        novo_filtro = sorted(filtro, key= lambda x: x[0], reverse = True)
        return novo_filtro[0][0]