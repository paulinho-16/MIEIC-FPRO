d = int(input('Enter a digit: '))
num = int(input('Enter a number: '))
result = 0
copia_num = num
while copia_num != 0:
    digito = copia_num%10
    if digito > d:
        result += 2*digito 
    copia_num = copia_num//10
print(result)