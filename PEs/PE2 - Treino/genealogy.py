def genealogy(l):
    familia = ['sibling','parent','cousin','grandparent']
    l = sorted(l,key = lambda x: x[0])
    ordenado = sorted(l,key = lambda x: familia.index(x[1]))
    return ordenado