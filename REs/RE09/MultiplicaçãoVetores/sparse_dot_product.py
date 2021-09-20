def sparse_dot_product(dict1,dict2):
    lista1 = list(dict1.items())
    lista2 = list(dict2.items())
    print(lista1)
    print(lista2)
    soma = 0
    for (index1,valor1) in lista1:
        produto = 0
        for (index2,valor2) in lista2:
            if index1 == index2:
                produto = valor1*valor2
        soma += produto
    return soma