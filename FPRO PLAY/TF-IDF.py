import math
def tfidf(documents):
    palavras = []
    for string in documents:
        string = string.lower()
        string_separada = string.split()
        for palavra in string_separada:
            if palavra not in palavras:
                palavras.append(palavra)
            else:
                continue
    tf = {}
    for word in palavras:
        lista_documentos = []
        for string in documents:
            string = string.lower()
            string_separada = string.split()
            vezes = string_separada.count(word)
            lista_documentos.append(vezes)
        tf[word] = lista_documentos
    for key, value in tf.items():
        n_documentos = 0
        nova_lista = []
        for valor in value:
            if valor != 0:
                n_documentos += 1
        x = len(documents)/n_documentos
        idf = math.log(x)
        for valor in value:
            nova_lista.append(round(valor*idf,3))
        tf[key] = nova_lista
    return tf