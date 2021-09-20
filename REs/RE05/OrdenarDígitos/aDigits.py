def adigits(n1,n2,n3):
    n1=int(n1)
    n2=int(n2)
    n3=int(n3)
    if(n2>=n1)and(n1>=n3):
        result=str(n2)+str(n1)+str(n3)
    elif(n1>=n2)and(n2>=n3):
        result=str(n1)+str(n2)+str(n3)
    elif(n3>=n2)and(n2>=n1):
        result=str(n3)+str(n2)+str(n1)
    elif(n3>=n1)and(n1>=n2):
        result=str(n3)+str(n1)+str(n2)
    elif(n2>=n3)and(n3>=n1):
        result=str(n2)+str(n3)+str(n1)
    elif(n1>=n3)and(n3>=n2):
        result=str(n1)+str(n3)+str(n2)
    return(result)
n1=input('Enter a number with 1 digit: ')
n2=input('Enter another number with 1 digit: ')
n3=input('Enter another number with 1 digit: ')
result=adigits(n1,n2,n3)
print(result)