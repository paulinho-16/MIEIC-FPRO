def media (notas):
        soma=0
        contador=0
        for i in notas[2]:
            soma += i
            contador += 1
        return(soma/contador)
def sort_grades (records):
    records = sorted(records, key = lambda x: x[1])
    records = reversed(sorted(records, key = lambda x: x[0]))
    records = reversed(sorted(records, key = media))
    records = tuple(records)
    return(records)