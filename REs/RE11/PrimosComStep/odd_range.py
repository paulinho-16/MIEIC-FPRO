def odd_range(start,stop,step):
    lista = []
    if start%2 == 0:
        start += 1
    for i in range(start,stop+1):
        if i%2 != 0:
            lista.append(i)
        else: 
            continue
    for j in range(0,len(lista),step):
        yield (lista[j])