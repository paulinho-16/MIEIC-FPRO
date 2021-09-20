def collisions(alist):
    dicionario = {}
    for number in alist:
        digitos = []
        for digit in str(number):
            digitos += [int(digit)]
        hsh = sum(digitos)%8
        if hsh not in dicionario:
            dicionario[hsh] = 1
        else:
            dicionario[hsh] += 1
    return dicionario