def rm_letter_rev(l,astr):
    contador=len(astr)
    result=''
    for i in range(contador):
        if (astr[i]!=l):
            result = astr[i]+ result
    return(result)