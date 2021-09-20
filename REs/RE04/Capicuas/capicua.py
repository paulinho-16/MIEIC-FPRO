num=int(input('Enter a number: '))
contador=0
num_final=0
divisao=num
num_reverso=num
while(divisao%10!=0):
    contador+=1
    divisao=(divisao//10)
for i in range(contador,-1,-1):
    algarismos = num_reverso % 10
    num_final += algarismos*10**i
    num_reverso = num_reverso//10
num_final = num_final//10

if (num == num_final):
    result= ('%d is a palindrome.') %num
else:
    result= ('%d is not a palindrome.') %num