def pattern_hunting(l1,l2,p):
    result = []
    def procurar(l_1,l_2):
        for index,string in enumerate(l_1):
            substrings = []
            for i in range(len(string)):
                for j in range(i,len(string)):
                    substrings += [string[i:j+1]]
            for substring in substrings:
                if substring == p:
                    result.append(l_2[index])
            else:
                continue
    procurar(l1,l2)
    procurar(l2,l1)
    result = sorted(result, reverse=True)
    return result