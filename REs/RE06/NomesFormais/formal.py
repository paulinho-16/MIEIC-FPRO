def formal(name):
    lista=name.split()
    nomes=len(name.split())
    pontos=''
    ultimo_nome = lista[nomes-1]
    if ultimo_nome[0]!=ultimo_nome[0].upper():
        ultimo_nome=ultimo_nome[0].upper()+ultimo_nome[1:]
    abreviaturas = lista[:nomes-1]
    for i in abreviaturas:
        pontos+= i[0].upper()+'. '
    result=ultimo_nome+', '+ pontos
    return(result)