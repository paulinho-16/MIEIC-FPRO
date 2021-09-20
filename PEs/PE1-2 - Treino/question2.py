number = input('Enter a non negative number: ')
index = 1
contador = 0
for digit in number[1:]:
    if digit == number[index-1]:
        contador += 1
    index += 1
print(contador)