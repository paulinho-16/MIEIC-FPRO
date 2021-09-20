def add_item (tup,idx,item):
    if idx > len(tup)-1:
        return 'Not possible'
    nova_tuple = ()
    if (idx == 0):
        nova_tuple = (item,) + tup[1:]
        return nova_tuple
    if (idx == len(tup)-1):
        nova_tuple = tup[:len(tup)-1] + (item,)
        return nova_tuple
    else:
        nova_tuple = tup[:idx] + (item,) + tup[idx:]
        return nova_tuple