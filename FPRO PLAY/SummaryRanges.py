def summary_ranges(astring):
    astring = astring.split(',')
    list_sequencias = []
    while len(astring)>0:
        for i in range(len(astring)):
            if len(astring)-1 == i:
                pass
            else:
                if int(astring[i]) + 1 != int(astring[i+1]):
                    break
        if astring[0] == astring[i]:
            list_sequencias.append(astring[i])
        else:
            list_sequencias.append(astring[0] + '->' + astring[i])
        astring = astring[i+1:]
    return ','.join(list_sequencias)