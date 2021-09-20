def batch_norm(alist,batch_size):
    sublistas = []
    sublista = []
    for index,i in enumerate(alist):
        if len(sublista) < batch_size and index != len(alist)-1:
            sublista.append(i)
        elif len(sublista) < batch_size and index == len(alist)-1:
            sublista.append(i)
            sublistas.append(sublista)
        elif len(sublista) == batch_size and index == len(alist)-1:
            sublistas.append(sublista)
            sublista = [i]
            sublistas.append(sublista)
        else:
            sublistas.append(sublista)
            sublista = [i]
    for lista in sublistas:
        if len(lista) % 2 != 0:
            mediana = sorted(lista)[len(lista)//2]
            lista = list(map(lambda x: x-mediana,lista))
            yield lista
        else:
            mediana = (sorted(lista)[len(lista)//2] + sorted(lista)[(len(lista)//2)-1])/2
            lista = list(map(lambda x: x-mediana,lista))
            yield lista