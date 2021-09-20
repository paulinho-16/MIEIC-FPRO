def rec_to_base(n,base):
    digits = '0123456789ABCDEF'
    if n < base:
        return digits[n]
    else:
        return rec_to_base(n//base,base) + digits[n%base]