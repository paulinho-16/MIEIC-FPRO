def calculator(expr):
    if type(expr) == int:
        return expr
    if type(expr[0]) == tuple:
        novo_n1 = calculator(expr[0])
    else:
        novo_n1 = expr[0]
    if type(expr[2]) == tuple:
        novo_n2 = calculator(expr[2])
    else:
        novo_n2 = expr[2]
    if expr[1] == '+':
        result = novo_n1 + novo_n2
    elif expr[1] == '-':
        result = novo_n1 - novo_n2
    elif expr[1] == '*':
        result = novo_n1 * novo_n2  
    return result