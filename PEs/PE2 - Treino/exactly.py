def exactly(s):
    tuplo = ()
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i].isdigit() and s[j].isdigit() and int(s[i]) + int(s[j]) == 10:
                substring = s[i:j+1]
                contador = 0
                for letter in substring:
                    if letter == '?':
                        contador += 1
                if contador != 3:
                    return 'The sequence {0} is NOT OK with first violation with pair: {1}'.format(s,(s[i]+s[j],))
                else:
                    tuplo += (s[i]+s[j],)
    return 'The sequence {0} is OK with the pairs: {1}'.format(s,tuplo)