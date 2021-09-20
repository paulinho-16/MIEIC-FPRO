def override(l1,l2):  
    result = l2
    lista_diferentes = []
    for i in range(len(l1)):
        for tuplo in l2:
            if tuplo[0] == l1[i][0]:
                break
        else:
            lista_diferentes.append(l1[i])
    print(lista_diferentes)   
    result += lista_diferentes
    result = sorted(list(set(result)))
    return result        