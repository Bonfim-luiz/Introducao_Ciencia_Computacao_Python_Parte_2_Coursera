def maiusculas(frase):
    '''A função recebe uma frase (uma string) como parâmetro e 
    devolve uma string com as letras maiúsculas que existem nesta
    frase, na ordem em que elas aparecem'''
    resultado = ""
    for letra in frase:
        if ord(letra) >= 65 and ord(letra) <= 90:
            resultado = resultado + letra
    return resultado
