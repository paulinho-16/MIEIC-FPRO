def is_perfect(n):
    num=n
    soma=0
    result=''
    for i in range(1,n):
        if(num%i==0):
            soma+=i
        else:
            continue
    if (soma==n):
        result=True
    else:
        result=False
    return(result)
n=int(input('Enter a number: '))    
result=is_perfect(n)
print(result)