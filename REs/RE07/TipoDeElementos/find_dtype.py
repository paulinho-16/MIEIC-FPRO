def find_dtype(atuple, data_type):
    result=()   
    for i in range(len(atuple)):
        if (type(atuple[i]).__name__) == (data_type):
            result += (atuple[i],)
    return(result)