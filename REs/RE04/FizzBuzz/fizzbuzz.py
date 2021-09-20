n=int(input('Enter a number: '))
result=""
for i in range(0,n+1):
    if (i%3==0 and i%5!=0):
        result+='Fizz '
    if (i%3!=0 and i%5==0):
        result+='Buzz '
    if (i%3==0 and i%5==0):
        continue
    if(i%3!=0 and i%5!=0):
        result+= str(i)+ ' '