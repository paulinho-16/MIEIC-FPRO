from functools import reduce
def map_filter_reduce(lst,f1,f2,f3):
    filtro = filter(f1,lst)
    mapa = map(f2,filtro)
    reduzido = reduce(f3,mapa)
    return reduzido