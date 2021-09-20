interest_rate_1=float(input('Enter the interest rate of the first payment method: '))
frequency1= int(input('Enter the payment frequency of the first payment method: '))
interest_rate_2=float(input('Enter the interest rate of the second payment method: '))
frequency2= int(input('Enter the payment frequency of the second payment method: '))
P=1000
t=1
final_amount_1= P*(1+interest_rate_1/frequency1)**(frequency1*t)
final_amount_2= P*(1+interest_rate_2/frequency2)**(frequency2*t)
print('For r='+str(interest_rate_1)+' and n='+str(frequency1)+" you'll have "+str(final_amount_1))
print('For r='+str(interest_rate_2)+' and n='+str(frequency2)+" you'll have "+str(final_amount_2))