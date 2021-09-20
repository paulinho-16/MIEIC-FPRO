dec = int(input('Enter a decimal number: '))
copia_dec = dec
index = 0
binario = 0
while copia_dec != 0:
    binario += (copia_dec%2)*10**index
    index += 1
    copia_dec //= 2
print(binario)