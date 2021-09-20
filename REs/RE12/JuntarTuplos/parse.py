def parse(filename):
    result = ''
    with open(filename) as texto:
        ler_linhas = texto.readlines()
    print(ler_linhas)
    for linha in ler_linhas:
        palavras = linha.split()
        print(palavras)
        for palavra in palavras:
            if palavra == '(':
                result += palavra
            else:
                result += palavra + ','
    return eval('(' + result + ')')