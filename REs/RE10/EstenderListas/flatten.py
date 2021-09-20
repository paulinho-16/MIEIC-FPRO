def flatten(alist):
    result = []
    for elemento in alist:
        if type(elemento) == list:
            result += flatten(elemento)
        else:
            result.append(elemento)
    return result