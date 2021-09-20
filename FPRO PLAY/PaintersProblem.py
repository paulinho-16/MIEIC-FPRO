def paint(n, boards):
    if n == 1:
        return max(boards)
    else:
        tempo_minimo = sum(boards)
        for index,board in enumerate(boards[:-n+1]):
            nova_board = boards[index+1:]
            x = max(boards[:index+1]) + paint(n-1, nova_board)
            if x < tempo_minimo:
                tempo_minimo = x
        return tempo_minimo