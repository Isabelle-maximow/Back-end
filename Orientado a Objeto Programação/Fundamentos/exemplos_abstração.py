'''Abstração: Ocultar a complexidade dos detalhes internos,
expõe apenas o que é necessário para o uso'''

# para abstração é preciso importar um metodo de abstração:
from abc import ABC, abstractmethod

class Forma:
    # dizer que é uma classe abstrata:
    @abstractmethod
    def area(self):
        pass
    
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.altura*self.largura
    
class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio
    def area (self):
        return 3.14*(self.raio*22)
# com a abstração. nos não precisamos intanciar  a clase pai para funcionar 
# abtração da classe pai
retangulo = Retangulo(10,5)
circulo = Circulo(7)

print(f"Área do retângulo: {retangulo.area()}")
print(f"Área do circulo: {circulo.area()}")