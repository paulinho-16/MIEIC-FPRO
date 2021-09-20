num=int(input('Enter a number: '))
result=0
for i in range(1,num+1):
    if (num%i==0):
        result+=i
    else:
        continue
print('The sum of its divisors is:',result)