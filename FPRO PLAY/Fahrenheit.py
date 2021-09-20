def to_fahrenheit(t):
    nova_lista = list(map(lambda x: round(x*1.8 + 32,2),t))
    return nova_lista