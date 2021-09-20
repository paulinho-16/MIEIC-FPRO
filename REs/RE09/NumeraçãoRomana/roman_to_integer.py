def roman_to_integer(astring):
    dicionario = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result = 0
    for i in range(len(astring)):
        if i == len(astring) - 1:
            result += dicionario[astring[i]]
        elif dicionario[astring[i]] < dicionario[astring[i+1]]:
            result -= dicionario[astring[i]]
        else:
            result += dicionario[astring[i]]
    return result