import turtle
campo=turtle.Screen()
campo.bgcolor('blue')
tartaruga=turtle.Turtle()
tartaruga.color('white')
tartaruga.shape('circle')
tartaruga.pensize(3)
lados=int(input('Introduza o número de lados da estrela: '))
angulo=float(360/lados)
for n in range(lados):
    tartaruga.forward(150)
    tartaruga.stamp()
    tartaruga.backward(150)
    tartaruga.right(angulo)
campo.exitonclick()