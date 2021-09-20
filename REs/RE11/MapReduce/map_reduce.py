from functools import reduce
def map_reduce(n1,n2):
    lista_impares = []
    for i in range(n1,n2+1):
        if i%2 != 0:
            quadrado = i**2
            lista_impares.append(quadrado)
    print(lista_impares)
    result = reduce(lambda j, y: y*j if y*j<50 else y+j,lista_impares)
    return result