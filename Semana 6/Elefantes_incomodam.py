def incomodam(n):
    valor_inteiro = int(n)
    if n < 1 or n != valor_inteiro:
        return ""
    else:
        return "incomodam " + incomodam(n-1)

def elefantes(n):
    if n == 1:
        return "Um elefante incomoda muita gente"
    elif n == 2:
        return elefantes(n-1) + f"\n{n} elefantes "+ incomodam(n) +"muito mais" 
    elif n > 2:
        frase1 = f"\n{n-1} elefantes incomodam muita gente"
        frase2 = f"\n{n} elefantes "+ incomodam(n) +"muito mais"
        return elefantes(n-1) + frase1 +frase2
    else:
        return ""
