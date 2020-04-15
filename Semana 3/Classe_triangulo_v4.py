class Triangulo:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimetro(self):
        soma = self.a + self.b + self.c
        return soma
    
    def tipo_lado(self):
        if self.a == self.b and self.a == self.c:
            return "equilátero"
        if self.a != self.b and self.a != self.c and self.c != self.b:
            return "escaleno"
        if (self.a == self.b and self.a != self.c) or (self.c == self.b and self.a != self.c) or (self.a == self.c and self.a != self.b):
            return "isósceles"
    
    def retangulo(self):
        if (self.a**2 == self.b**2 + self.c**2) or (self.b**2 == self.a**2 + self.c**2) or (self.c**2 == self.b**2 + self.a**2):
            return True 
        else:
            return False
    def semelhantes(self, triangulo):
        lista1 = [self.a, self.b, self.c]
        lista2 = [triangulo.a, triangulo.b, triangulo.c]
        lista1 = sorted(lista1)
        lista2 = sorted(lista2)
        
        if lista1[0] > lista2[0]:
            if lista1[0] % lista2[0] == 0 and lista1[1] % lista2[1] == 0 and lista1[2] % lista2[2] == 0:
                return True
            else:
                return False
        else:
            if lista2[0] % lista1[0] == 0 and lista2[1] % lista1[1] == 0 and lista2[2] % lista1[2] == 0:
                return True
            else:
                return False
        
