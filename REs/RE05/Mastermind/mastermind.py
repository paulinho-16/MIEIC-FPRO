def mastermind(g1,g2,g3,c1,c2,c3):
    pontos=0
    if g1==c1:
        pontos+=3
    elif g1!=c1 and (g1==c2 or g1==c3):
        pontos+=1
    if g2==c2:
        pontos+=3
    elif g2!=c2 and (g2==c1 or g2==c3):
        pontos+=1
    if g3==c3:
        pontos+=3
    elif g3!=c3 and (g3==c1 or g3==c2):
        pontos+=1
    return(pontos)
c1=input('Enter the first letter (b,w,y) of the correct key: ')
c2=input('Enter the second letter (b,w,y) of the correct key: ')
c3=input('Enter the third letter (b,w,y) of the correct key: ')
g1=input('Enter the letter b,w or y: ')
g2=input('Enter the letter b,w or y: ')
g3=input('Enter the letter b,w or y: ')
result=mastermind(g1,g2,g3,c1,c2,c3)
print(result)