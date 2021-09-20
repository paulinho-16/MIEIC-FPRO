def soup(matrix,word):
    for linha in range(len(matrix)):
        for letter in range(len(matrix[linha])):
            if matrix[linha-1][letter-1] == word[0]:
                if checksoup(matrix,linha-1,letter-1,word[1:]):
                    return "{0}{1}".format(chr(ord("A")+linha-1),letter)


def checksoup(matrix,linha,letra,word):
    if word == "":
        return True
    else:
        for r in range(linha-1,linha+2):
            for l in range(letra-1,letra + 2):
                if r>=0 and l>=0 and r<len(matrix) and l<len(matrix) and word[0] == matrix[r][l]:
                    matrix[r][l] == ""
                    if checksoup(matrix,r,l,word[1:]):
                        return checksoup(matrix,r,l,word[1:])
                    else:
                        continue