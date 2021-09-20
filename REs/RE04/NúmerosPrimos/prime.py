n=int(input('Enter a number: '))
divisores=0
for i in range(1,n+1):
    if(n%i==0):
        divisores+=1
    else:
        continue
if(divisores==2):
    result=True
else:
    result=False