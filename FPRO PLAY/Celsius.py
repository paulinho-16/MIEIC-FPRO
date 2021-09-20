def to_celsius(t):
    nova_lista = list(map(lambda x: (round((x-32)/1.8,1)),t))
    return nova_lista