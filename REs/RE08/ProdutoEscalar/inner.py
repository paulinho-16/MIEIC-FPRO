def inner(u,v):
    result = 0
    for index,number in enumerate(u):
        result += number * v[index]
    return result