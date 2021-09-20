def ugly (n):
    list_fatores = []
    list_fatores_primos = []
    for i in range (1,n+1):
        if n%i==0:
            list_fatores.append(i)
    for i in list_fatores:
        contador = 0
        for j in range(1,i+1):
            if i%j==0:
                contador +=1
        if contador == 2:
            list_fatores_primos.append(i)
    print (list_fatores)
    print (list_fatores_primos)
    if n == 1:
        return True
    else:
        for o in list_fatores_primos:        
            if o != 2 and o != 3 and o != 5:
                return False
        return True