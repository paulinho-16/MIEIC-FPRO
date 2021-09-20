def longest (s):
    list_string = s.split()
    print(list_string)
    list_comp = []
    for word in list_string:
        list_comp.append(len(word))
    list_comp = sorted(list_comp, reverse = True)
    return list_comp[0]