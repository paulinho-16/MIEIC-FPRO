def recursive_dot(l1,l2):
    result = 0
    for index,element in enumerate(l1):
        if type(element) != list:
            result += l1[index]*l2[index]
        else:
            result += recursive_dot(l1[index],l2[index])
    return result