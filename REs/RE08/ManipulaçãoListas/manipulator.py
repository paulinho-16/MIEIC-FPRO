def manipulator(l,cmds):
    result = ''
    for comando in cmds:
        comando = comando.split()
        if comando[0] == 'insert':
            l.insert(int(comando[1]),int(comando[2]))
        if comando[0] == 'remove':
            l.remove(int(comando[1]))
        if comando[0] == 'append':
            l.append(int(comando[1]))
        if comando[0] == 'sort':
            l.sort()
        if comando[0] == 'pop':
            l.pop()
        if comando[0] == 'reverse':
            l.reverse()
        if comando[0] == 'print':
            result += str(l) + ' '
    return result