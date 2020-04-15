import unicodedata as ud

def menor_nome(lista):
    len_lista = len(lista)
    lista_organizada =  [(ud.normalize('NFKD', s).encode('ASCII','ignore').decode()).strip() for s in  lista]
    lens = [len(s) for s in lista_organizada]
    min_len = min(lens)
    resultado = []
    
    for i in range(len_lista):
        s = lista_organizada[i]
        if len(s) == min_len:
          resultado.append(lista[i].strip().capitalize())

    return resultado[0] 
