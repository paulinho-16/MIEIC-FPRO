def is_orthogonal(mx):
    transposta = []
    for i in range(len(mx[0])):
        nova_linha = []
        for linha in mx:
            nova_linha += [linha[i]]
        transposta.append(nova_linha)
    print(transposta)
    matriz_produto = []
    for i in range(len(mx)):
        linha_nova = []
        for j in range(len(transposta[0])):
            produto = 0
            for k in range(len(transposta)):
                produto += mx[i][k] * transposta[k][j]
            linha_nova.append(produto)
        matriz_produto.append(linha_nova)
    print(matriz_produto)
    identidade = []
    for l in range(len(mx)):
        linha_identidade = []
        for m in range(len(mx)):
            linha_identidade.append(0)
        identidade.append(linha_identidade)
    for n in range(len(identidade)):
        identidade[n][n] += 1
    if identidade == matriz_produto:
        return True
    else:
        return False