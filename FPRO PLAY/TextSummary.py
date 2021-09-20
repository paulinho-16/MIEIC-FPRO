def summary(text):
    result_tup = ()
    text = text.lower()
    text_list = text.split()
    contador = 0
    for word in text_list:
        if 'e' in word:
            contador += 1
    palavras_e = contador
    result_tup += (len(text_list), palavras_e)
    return result_tup