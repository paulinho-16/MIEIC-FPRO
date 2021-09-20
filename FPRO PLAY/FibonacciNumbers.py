def fib(n):
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        lista = [0,1]
        while len(lista) != n:
            lista.append(lista[-2] + lista[-1])
    return lista