def translate(astring,table):
    result=''
    for i in range(len(astring)):
        for j in range(len(table)):
            if astring[i] == table[j][0]:
                result += str(table[j][1])
                break
        else: 
            result += astring[i]
    return result