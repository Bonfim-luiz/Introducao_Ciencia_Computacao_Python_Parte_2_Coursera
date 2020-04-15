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
