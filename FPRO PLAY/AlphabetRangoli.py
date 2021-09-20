def rangoli(N):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    final=''
    final2=''
    contador=0
    

    lista=[]
    if N==1:
        return('a')
    if N!=1:  
        for i in range(N-1,-1,-1):             
            final2 += alfabeto[i] + '-'
            final=final2[1:]
            final=final2[::-1]
            contador += 1
            if contador == 1:  
                a=( ('-'*(((4*(N-contador)-3)//2)+2))   +  final2 + final[3:len(final)] + ('-'*(((4*(N-contador)-3)//2)+1)))
                lista.append(a)
            if contador != 1:
                b=( ('-'*(((4*(N-contador)-3)//2)+2))   +  final2 + final[3:len(final)] + ('-'*(((4*(N-contador)-3)//2)+2)))
                lista.append(b)
        for i in range(len(lista)-2,-1,-1):
            lista.append(lista[i])
        return("\n".join(lista))