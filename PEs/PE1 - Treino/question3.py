names = ['bart','marie','jo']
ages = [23,75,19]
index = 0
result = ''
for name in names:
    index2 = 0
    for age in ages:
        if index == index2:
            result += name + '-' + str(age) + ' '
        index2 += 1
    index += 1
print(result)