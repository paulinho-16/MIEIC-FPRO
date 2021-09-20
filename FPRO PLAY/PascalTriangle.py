def pascal(n):
    result = ''
    def factorial(n):
        fatorial = 1
        if n<=0:
            return 1
        for i in range(n,0,-1):
            fatorial *= i
        return int(fatorial)
    def combinacoes(n,r):
        return int((factorial(n))/(factorial(r)*factorial(n-r)))
    for j in range(n):
        for r in range(j+1):
            result += str(combinacoes(j,r)) + ' '
        result = result[:(len(result)-1)]
        result += '\n'
    result = result[:(len(result)-1)]
    return result