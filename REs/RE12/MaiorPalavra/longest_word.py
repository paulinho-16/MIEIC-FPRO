import urllib.request
def longest_word(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    palavras = set(html.split())
    print(palavras)
    lista_palavras = []
    with open('words') as texto:
        ler_linhas = texto.readlines()
        for linha in ler_linhas:
            lista_palavras += linha.split()
        lista_palavras = set(lista_palavras)
        palavras_comuns = palavras.intersection(lista_palavras)
        comprimento = 0
        for word in palavras_comuns:
            if len(word) > comprimento:
                comprimento = len(word)
                maior_palavra = word
            elif len(word) == comprimento:
                lista = sorted([maior_palavra,word])
                maior_palavra = lista[0] 
    return maior_palavra