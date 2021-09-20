def rec_gcd(n1,n2):
    if n1%n2 == 0:
        return n2
    else:
        return rec_gcd(n2,n1%n2)