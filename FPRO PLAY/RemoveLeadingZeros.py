def remove_leading (ip):
    list_numeros = ip.split(".")
    print (list_numeros)
    string_final = ""
    for i in list_numeros:
        number = int(i)
        string_final += str(number) + "."
    string_final = str(string_final[:(len(string_final) -1)])
        
    return string_final