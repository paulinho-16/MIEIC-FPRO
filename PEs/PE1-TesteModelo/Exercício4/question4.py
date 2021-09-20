le=int(input("Enter your LE's grade, from 0 to 100: "))
re=int(input("Enter your RE's grade, from 0 to 100: "))
pe=int(input("Enter your PE's grade, from 0 to 100: "))
te=int(input("Enter your TE's grade, from 0 to 100: "))
if ((pe<40)or(te<40)):
    print('RFC')
elif ((0<=le<=100)and(0<=re<=100)and(0<=pe<=100)and(0<=te<=100)):
    grade=int((le+re+4*pe+4*te)/50)
    print(grade)
else:
    print('Input error')  