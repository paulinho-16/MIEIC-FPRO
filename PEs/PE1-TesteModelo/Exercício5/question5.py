lower=int(input('Enter the lower number: '))
upper=int(input('Enter the upper number: '))
primos=''
for i in range(lower,upper+1):
    if (i>1):
        for n in range(2,i):
            if (i%n==0):
                break
        else:
            primos+=(str(i)+' ')
print('Prime numbers between',str(lower),'and',str(upper),'are:',primos)