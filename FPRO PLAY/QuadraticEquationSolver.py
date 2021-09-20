def solver(a,b,c):
    teste = (b**2-4*a*c)
    if teste < 0:
        return []
    elif teste == 0:
        result = -b/(2*a)
        return [result]
    else:
        result1 = (-b+(teste**0.5))/(2*a)
        result2 = (-b-(teste**0.5))/(2*a)
        return sorted([result1,result2])