def encontra_impares(lista):
    if len(lista) == 0:
        return []
    primeiro_elemento = lista.pop(0)
    impares = []
    if primeiro_elemento % 2 != 0:
        impares.append(primeiro_elemento)
    return impares + encontra_impares(lista)
