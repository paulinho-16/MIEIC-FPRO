def count_until(tup):
    contador = 0
    for i in tup:
        contador += 1
        if type(i) == tuple:
            return contador-1
    return -1