def collatz (n):
    result = str(n) + ','
    while n != 1:
        if n%2==0:
            n = round(n/2)
            result += str(n) + ','
        else:
            n = round(n*3+1)
            result += str(n) + ','
    return result[:len(result)-1]