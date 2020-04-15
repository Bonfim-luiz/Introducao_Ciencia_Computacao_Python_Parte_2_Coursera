import re
def conta_letras(frase, contar="vogais"):
    """A função conta_letras(frase, contar="vogais"), que recebe como 
    primeiro parâmetro uma string contendo uma frase e como segundo 
    parâmetro uma outra string. Este segundo parâmetro deve ser opcional."""
    consoantes = ''
    vogais = ''
    frase = re.sub('[!-.:-@]',' ', frase)
    a = 0
    for letra in frase:
        if letra not in ("A","E","I","O","U","a","e","i","o","u") and contar == "consoantes":
            consoantes = consoantes + letra
            consoantes = re.sub('[!-.:-@]', ' ', consoantes)
            consoantes = consoantes.strip()
            a = len(consoantes)
        elif letra in ("A","E","I","O","U","a","e","i","o","u") and contar == "vogais":
            vogais = vogais + letra
            vogais = re.sub('[!-.:-@]', ' ', vogais)
            vogais = vogais.strip()
            a = len(vogais)
        else:
            if letra in ("A","E","I","O","U","a","e","i","o","u") and contar != "consoantes":
                vogais = vogais + letra
                vogais = re.sub('[!-.:-@]', ' ', vogais)
                vogais = vogais.strip()
                a = len(vogais)
    return a
