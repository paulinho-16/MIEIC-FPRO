dec = int(input('Enter a decimal number: '))
copia_dec = dec
result = 0
index = 0
while copia_dec != 0:
    digito = copia_dec % 8
    result += digito * 10**index
    copia_dec = copia_dec // 8
    index += 1
print(result)