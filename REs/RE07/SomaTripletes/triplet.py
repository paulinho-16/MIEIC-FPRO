def triplet(atuple):
    for i in atuple:
        for j in atuple:
            for k in atuple:                
                if (i+j+k == 0) and (atuple.index(i)!=atuple.index(j)!=atuple.index(k)):
                    result = (i,j,k)
                    return(result)
                else:
                    result=()
    return (result)
