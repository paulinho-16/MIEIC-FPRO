def get_positions(word_list,sentence):
    for i in range(len(word_list)):
        for n in range(len(word_list)):
            frase = word_list[i]+' '+word_list[n]
            if i!=n:
                if frase==sentence:
                    positions= str(i)+' '+str(n)
                    return positions