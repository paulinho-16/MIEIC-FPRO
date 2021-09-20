def remover(lista):
    result = []
    for i in lista:
        if i not in result:
            result.append(i)
    return result
def permuta(alist,step=0):
    resultados = []
    if step != len(alist):
        for i in range(step,len(alist)):
            nova_lista = alist.copy()
            nova_lista[step] = alist[i]
            nova_lista[i] = alist[step]
            resultados.append(nova_lista)
            resultados += permuta(nova_lista,step+1)
    return remover(resultados)