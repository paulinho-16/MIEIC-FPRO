def sort_by_field(filename,field):
    with open(filename) as texto:
        ler_linhas = texto.read()
        linhas = ler_linhas.split('\n')
        primeira_linha = linhas[0].split(',')
        linhas = linhas[1:]
        for i in range(len(primeira_linha)):
            if primeira_linha[i] == field:
                index = i
                break
        ordenado = sorted(linhas,key= lambda x: x.split(',')[index])
        first_line = ''
        for i in primeira_linha:
            first_line += i + ','
        first_line = first_line[:-1]
        resultado = ''
        for data in ordenado:
            resultado += data + '\n'
        resultado = resultado[:-1]
        result = first_line + '\n' + resultado
        return result