def academy_awards(alist):
    dicionario = {}
    for tuplo in alist:
        if tuplo[1] not in dicionario:
            dicionario[tuplo[1]] = 1
        else:
            dicionario[tuplo[1]] += 1
    return dicionario