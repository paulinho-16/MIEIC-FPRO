a = input('Player A: ')
b = input('Player B: ')
if a == b:
    print("That's a draw")
elif a == 'scissors':
    if b == 'rock':
        print('The winner is B')
    elif b == 'paper':
        print('The winner is A')
elif a == 'rock':
    if b == 'scissors':
        print('The winner is A')
    elif b == 'paper':
        print('The winner is B')
elif a == 'paper':
    if b == 'rock':
        print('The winner is A')
    elif b == 'scissors':
        print('The winner is B')