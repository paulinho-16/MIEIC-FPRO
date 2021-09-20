def count_exceptions(f,n1,n2):
    contador = 0
    for i in range(n1,n2+1):
        try:
            f(i)
        except Exception:
            contador += 1
    return contador