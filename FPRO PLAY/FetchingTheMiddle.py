def fetch_middle(lists):
    result = []
    for lista in lists:
        if len(lista)%2 != 0:
            result.append(lista[len(lista)//2])
        else:
            result.append((lista[len(lista)//2] + lista[len(lista)//2 - 1])/2)
    return result