def budgeting(budget,products,wishlist):
    def valor_compras(budget,products,wishlist):
        custo_total = 0
        for produto,numero in wishlist.items():
            custo_total += products[produto]*wishlist[produto]
        if custo_total <= budget:
            return wishlist
        else:
            return
    nova_wishlist = wishlist.copy()
    while valor_compras(budget,products,nova_wishlist) == None:
        precos = [products[i] for i in wishlist.keys()]
        mais_barato = min(precos)
        for produt,value in wishlist.items():
            if products[produt] == mais_barato:
                if nova_wishlist[produt] == 1:
                    del nova_wishlist[produt]
                    del wishlist[produt]
                    break
                else:
                    nova_wishlist[produt] -= 1
                    wishlist[produt] -= 1
                    break
        
    return nova_wishlist