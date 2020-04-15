# Soma matrizes
def dimensoes(matriz):
    linha = len(matriz)
    intermed = matriz[0]
    coluna = len(intermed)
    return(str(linha) + "X" + str(coluna))

def cria_matriz(tot_lin, tot_col, valor):
    matriz = []  #lista vazia
    for i in range(tot_lin):
        linha = []
        for j in range(tot_col):
            linha.append(valor)
        matriz.append(linha)
    return matriz
    
def soma_matrizes(m1, m2):
    dimensao_m1 = dimensoes(m1)
    dimensao_m2 = dimensoes(m2)
    if not dimensao_m1 == dimensao_m2:
        return False
    else:
        linha = len(m1)
        coluna = len(m1[0])
        C = cria_matriz(linha, coluna, 0)
        for lin in range(linha):
            for col in range(coluna):
                C[lin][col] = m1[lin][col] + m2[lin][col]
        return C       
