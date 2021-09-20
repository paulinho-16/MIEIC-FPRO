num = int(input('Enter a number: '))
soma = 0
copia_num = num
while num != 0:
    digit = num%10
    soma += digit**3
    num = num//10
if soma == copia_num:
    print(True)
else:
    print(False)