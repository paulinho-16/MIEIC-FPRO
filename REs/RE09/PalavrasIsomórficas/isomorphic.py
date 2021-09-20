def isomorphic(astring1,astring2):
    dicionario1 = {}
    dicionario2 = {}
    for i in range(len(astring1)):
        if astring1[i] not in dicionario1:
            dicionario1[astring1[i]] = 1
        else:
            dicionario1[astring1[i]] += 1
    for j in range(len(astring2)):
        if astring2[j] not in dicionario2:
            dicionario2[astring2[j]] = 1
        else:
            dicionario2[astring2[j]] += 1
    dicionario = {}
    for key1 in dicionario1:
        for key2 in dicionario2:
            if dicionario2[key2] == dicionario1[key1]:
                for tuplo in dicionario.items():
                    if key1 in tuplo[0] or key2 in tuplo[1]:
                        break
                else:
                    dicionario[key1] = key2
    letras_diferentes = []
    for k in astring1:
        if k not in letras_diferentes:
            letras_diferentes.append(k)
    print(letras_diferentes)
    if len(letras_diferentes) == len(dicionario):
        return "'{0}' and '{1}' are isomorphic because we can map: {2}".format(astring1,astring2,list(dicionario.items()))
    else:
        return "'{0}' and '{1}' are not isomorphic".format(astring1,astring2)
            
    
    
    
print(isomorphic('ab', 'aa'))
print(isomorphic('paper', 'title'))
print(isomorphic('foo', 'bar'))
print(isomorphic('turtle', 'tletur'))