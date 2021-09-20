ints = [1,2,2,3,5,9,13,21,34]
num = int(input('Enter a number: '))
maiores = 'Greater: '
menores = 'Less: '
for number in ints:
    if number>num:
        maiores += str(number) + ' '
    elif number<num:
        menores += str(number) + ' '
print(menores)
print(maiores)