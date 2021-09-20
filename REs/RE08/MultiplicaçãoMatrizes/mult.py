def mult(M,N):
    if len(M[0]) != len(N):
        return []
    else:
        matriz = []
        for i in range(len(M)):
            linha = []
            for j in range(len(N[0])):
                produto = 0
                for k in range(len(M[0])):
                    produto += M[i][k]*N[k][j]
                linha.append(produto)
            matriz.append(linha)
        return matriz