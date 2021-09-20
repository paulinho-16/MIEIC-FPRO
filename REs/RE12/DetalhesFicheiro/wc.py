def wc(filename):
    tuplo = ()
    with open(filename) as texto:
        ler_linhas = texto.readlines()
    numero_caracteres = 0
    numero_linhas = 0
    numero_palavras = 0
    for linha in ler_linhas:
        for i in linha:
            numero_caracteres += 1
        numero_palavras += len(linha.split())
        numero_linhas += 1
    tuplo += (numero_linhas,numero_palavras,numero_caracteres)
    return tuplo