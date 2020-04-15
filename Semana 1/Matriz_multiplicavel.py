# Matriz multiplicaveis

def sao_multiplicaveis(m1, m2):
    coluna_m1 = len(m1[0])
    linha_m2 = len(m2)
    if coluna_m1 == linha_m2:
        return True
    else:
        return False
