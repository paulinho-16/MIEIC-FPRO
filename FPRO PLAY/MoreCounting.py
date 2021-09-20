def count_elems (tup):
    nova_tup = ()
    for i in tup:
        if type(i) == tuple or type(i) == list:
            nova_tup += (len(i),)
        elif type (i) == str:
            nova_tup += (len(i),)
        else:
            nova_tup += (1,)
    return nova_tup