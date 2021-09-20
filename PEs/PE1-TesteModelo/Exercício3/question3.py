num=int(input('Enter a number: '))
x0=num
x1=(x0+num/x0)/2
while (round(x0,2)!=round(x1,2)):
    x0=x1
    x1=(x0+num/x0)/2
result=(format(x1,'.3f'))
print(result)