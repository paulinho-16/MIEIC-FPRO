def treasure(clues):
    pos = (0,0)
    while pos in clues:
        (pos_anterior,pos) = (pos,clues[pos])
        del clues[pos_anterior]
    return pos