lado1=int(input('Introduza o comprimento do primeiro lado do triângulo: '))
lado2=int(input('Introduza o comprimento do segundo lado do triângulo: '))
lado3=int(input('Introduza o comprimento do terceiro lado do triângulo: '))
if((lado1+lado2<=lado3)or(lado2+lado3<=lado1)or(lado1+lado3<=lado2)):
    result='Not a triangle'
else:
    if (lado1==lado2==lado3):
        result='Equilateral'
    if(lado1==lado2!=lado3) or (lado1!=lado2==lado3) or (lado1==lado3!=lado2):
        result='Isosceles'
    if(lado1!=lado2!=lado3):
        result='Scalene'