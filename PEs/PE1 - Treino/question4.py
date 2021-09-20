tS = float(input('Enter swimming time: '))
tC = float(input('Enter cycling time: '))
tR = float(input('Enter running time: '))
velocidade_swimming = 1.5/tS
velocidade_cycling = 40/tC
velocidade_running = 10/tR
if tS+tC+tR >= 4:
    print('Time')
elif velocidade_swimming < 2:
    print('Swimming')
elif velocidade_cycling < 20:
    print('Cycling')
elif velocidade_running < 8:
    print('Running')
else:
    print(tS+tC+tR)