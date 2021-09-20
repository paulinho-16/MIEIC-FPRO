def interleave(alist1,alist2):
    result = []
    for index,element in enumerate(alist1):
        if type(element) != list:
            result += [element] + [alist2[index]]
        else:
            result += (interleave(element,alist2[index]))
    return result