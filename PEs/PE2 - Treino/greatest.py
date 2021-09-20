def greatest(num):
    num = '.'.join(str(num)).split('.')
    num_ordenado = sorted(num,reverse = True)
    result = ''.join(num_ordenado)
    return int(result)