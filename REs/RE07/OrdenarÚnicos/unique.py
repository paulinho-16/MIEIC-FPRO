def unique(atuple):
    ordenado = sorted(atuple)
    result = (ordenado[0],)
    n_membros = len(ordenado)
    
    for i in range(1,n_membros):
        if ordenado[i] != ordenado[i-1]:
            result += (ordenado[i],)
    return result
    
