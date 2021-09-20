integers = [0,2,9,15,64]
reals = [0.0,3.2,8.4,15.5,128.0]
result = ''
index1 = 0
if integers == [] and reals == []:
    print([])
for num1 in integers:
    index2 = 0
    for num2 in reals:
        if index1 == index2:
            if num1>=num2:
                result += str(num1) + ' '
            else:
                result += str(num2) + ' '
        index2 += 1
    index1 += 1
print(result)