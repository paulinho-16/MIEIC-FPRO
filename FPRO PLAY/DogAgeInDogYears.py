def dogs(h_age):
    if h_age <= 2:
        idade = h_age*10.5
        return idade
    else:
        idade = 2*10.5 + (h_age-2)*4
        return idade