def sum_numbers(n):
    soma=0
    for i in range(1,n+1):
        soma+=i
    return(soma)
n=int(input('Enter a number: '))
result=sum_numbers(n)
print(result)