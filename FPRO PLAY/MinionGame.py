def minion(astring):
    vowels = 'AEIOU'
    stuart=0
    kevin=0
    vogais=[]
    astring=astring.upper()
    consoantes=[]
    contador=[]
    contador2=[]
    vog=[]
    con=[]
    b=''
    d=''
    for i in range(0, len(astring)+1):
        for j in range(0, len(astring)+1):
            a=astring[i:j]
            if i!=j and i<=j:
                if a[0] in vowels:
                    vogais.append(a)
                if a[0] not in vowels:
                    consoantes.append(a)
    vogais = sorted(vogais, key=lambda x: len(x))
    consoantes = sorted(consoantes, key=lambda x: len(x))
    for n in range(0, len(vogais)):
        if vogais[n] == vogais[n-1]:
            continue
        if vogais[n] != vogais[n-1]:
            conta=vogais.count(vogais[n])
            contador.append(conta)
            vog.append(vogais[n])
            for c in vog:
                kevin= sum(contador)
    for p in range(0, len(consoantes)):
        if consoantes[p] == consoantes[p-1]:
            continue
        if consoantes[p] != consoantes[p-1]:
            conta2=consoantes.count(consoantes[p])
            contador2.append(conta2)
            con.append(consoantes[p])
            for c in con:
                stuart= sum(contador2)
    for f in range(0,len(con)):
        b += '\n ' + '- ' + con[f] + ': ' + str(contador2[f])
    for g in range(0,len(vog)):
        d += '\n ' + '- ' + vog[g] + ': ' + str(contador[g])
#            final=
    if kevin<stuart:
        return 'The winner was Stuart with a total of ' + str(stuart) + ' points:' + b
    if kevin>stuart:
        return 'The winner was Kevin with a total of ' + str(kevin) + ' points:' + d
    if kevin==stuart:
        return 'It was a draw!'