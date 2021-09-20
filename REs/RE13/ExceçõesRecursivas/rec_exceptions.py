def rec_exceptions(l):
    resultado = []
    for ch in l: 
        try:
           type(ch()) == type([])
        except Exception as r:
            resultado.append(r)      
        else:
            resultado += rec_exceptions(ch())        
    return resultado