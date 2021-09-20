import string
def caesar(message):
    abecedario = string.ascii_uppercase
    message = message.upper()
    result = ''
    for index,letter in enumerate(message):
        if letter in abecedario:
            shift = int(((1+5**(1/2))**index - (1-5**(1/2))**index)/((2**index)*5**(1/2)))
            novo_index = (abecedario.find(letter) - shift)%len(abecedario)
            result += abecedario[novo_index]
        else:
            result += letter
    return result