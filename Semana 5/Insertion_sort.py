# Insertion Sort

def insertion_sort(lista):
    for i in range(1,len(lista)):
        valor = lista[i]
        posicao = i
        
        while posicao > 0 and lista[posicao-1] > valor:
            lista[posicao] = lista[posicao-1]
            posicao = posicao-1
            lista[posicao] = valor
    return lista

