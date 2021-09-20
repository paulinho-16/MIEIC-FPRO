def rearrange(l):
    negativos = list(filter(lambda x: x<=0,l))
    positivos = list(filter(lambda x: x>0,l))
    return negativos + positivos