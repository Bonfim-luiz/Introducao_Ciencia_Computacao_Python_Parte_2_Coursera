# Ordena lista
def ordenada(lista):
    lista_new = []
    for i in lista:
        lista_new.append(i) 
        
    fim = len (lista_new)
    for i in range(fim-1):
        posicao_minima = i
        for j in range(i+1,fim):
            if lista_new[j] < lista_new[posicao_minima]:
                posicao_minima = j
        lista_new[i], lista_new[posicao_minima] = lista_new[posicao_minima], lista_new[i]

    if lista == lista_new:
        return True
    else:
        return False
