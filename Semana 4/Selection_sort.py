# Ordena sem comparar
def ordena(lista):
    fim = len (lista)
    for i in range(fim-1):
        posicao_minima = i
        for j in range(i+1,fim):
            if lista[j] < lista[posicao_minima]:
                posicao_minima = j
        lista[i], lista[posicao_minima] = lista[posicao_minima], lista[i]
    return lista
