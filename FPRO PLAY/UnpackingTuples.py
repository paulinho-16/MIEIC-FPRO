def unpack_rev (atuple):
    atuple = atuple[::-1]
    result = ''
    for i in atuple:
        result += str(i) + ' '
    return result[:len(result)-1]
        