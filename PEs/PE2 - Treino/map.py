def map(pos,steps):
    x = pos[0]
    y = pos[1]
    steps = steps.split('-')
    for instruction in steps:
        if instruction == 'up':
            y += 1
        elif instruction == 'down':
            y -= 1
        elif instruction == 'left':
            x -= 1
        elif instruction == 'right':
            x += 1
    result = (x,y)
    return result