# achar a area de um retangulo e de um circulo
class Forma: # class pai, sem atributo
    # criar apenas o metodo
    def area(self): # area de uma orma geometrica
        pass
    # fim da classe
    
# subclass area do retangulo
class Retangulo(Forma):
    # atributo é criado na subclass
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    # metodo para achar a area 
    def area(self): # retorna o resultado
        return self.largura*self.altura

# obragtorio instranciar o objeto python
forma = Forma() # cria instancia
largura = int(input("Valor da largura: "))
altura = int(input("Valor da altura: "))

# CHAMAR A CLASSE FILHO PARA CIAR O POLIOMORFISMO:
retangulo = Retangulo(largura, altura)
print(f"Área o retangulo é: {retangulo.area()}")

class Circulo(Forma):
    def __init__(self, raio, pi):
        self.raio = raio
        self.pi = pi
    def area (self):
        return self.pi*self.raio**2
forma = Forma() # cria instancia
pi = 3.14
raio = int(input("Valor do raio: "))

circulo = Circulo(raio, pi)
print(f"Área do circulo é: {circulo.area()}")