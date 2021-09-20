def rec_sum_digits(n):
    if len(str(n)) == 1:
        return n
    else:
        resto = n%10
        return rec_sum_digits(n//10) + resto