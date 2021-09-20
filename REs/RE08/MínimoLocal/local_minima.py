def local_minima(alist,n):
    if n % 2 != 0:
        minimo = n//2
        maximo = n//2
    else:
        minimo = n/2
        maximo = n/2 - 1
    result = []
    contador = 0
    for numero in alist:
        menor = contador - minimo
        maior = contador + maximo + 1
        if menor < 0:
            menor  = 0
        if maior > (len(alist) - 1):
            maior = len(alist)
        minimo_local = min(alist[menor:maior])
        contador2 = 0
        for i in alist[menor:maior]:
            if i == minimo_local:
                contador2 += 1
        if contador2 > 1:
            index = alist.index(minimo_local)
        else:
            index = contador
        if numero == minimo_local and ((minimo_local,index) not in result):
            result.append((numero,contador))
        contador += 1
    return result